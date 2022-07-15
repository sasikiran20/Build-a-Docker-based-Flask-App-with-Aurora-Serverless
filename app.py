from flask import Flask, request, jsonify
import os
import boto3
from botocore.config import Config

app = Flask(__name__)

my_config = Config(
    region_name = 'us-east-1'
)
rds_data = boto3.client('rds-data', config=my_config, aws_access_key_id='AKIARJKDIMSBDK5J6QRMWWB', aws_secret_access_key='rw3rlhZ5VMXKkgGy5q4KHWnP1ofqju3E91k+qaPhilp')


aurora_db_name = 'mydatabase' 
aurora_cluster_arn = 'arn:aws:rds:us-east-1:0882657756742:cluster:database-1' #os.environ['CLUSTER_ARN']
aurora_secret_arn = 'arn:aws:secretsmanager:us-east-1:0882657568742:secret:AuroraServerlessDemo-SZWWli23' #os.environ['SECRET_ARN']

@app.route('/getPerson') 
def getPerson():
    personId = request.args.get('personid')
    response = callDbWithStatement("select * from persons WHERE personid='" + str(personid) + "'" )
    person = {}
    records = response['records']
    for record in records:
        person['personid'] = record[0]['longValue']
        person['firstname'] = record[1]['stringValue']
        person['lastname'] = record[2]['stringValue']
    print(person)
    return jsonify(person)

@app.route('/createPerson',  methods=['POST']) 
def createPerson():
    request_data = request.get_json()
    personid = str(request_data['personid'])
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    callDbWithStatement("INSERT INTO persons(personid, firstname, lastname) VALUES ('" 
    + personid + "', '" + firstname + "', '" + lastname + "');")
    return ""
    
def callDbWithStatement(statement):
    response = rds_data.execute_statement(
            database = aurora_db_name,
            resourceArn = aurora_cluster_arn,
            secretArn = aurora_secret_arn,
            sql = statement,
            includeResultMetadata = True
        )
    print("Making Call " + statement)
    print(response)
    return response

if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8081)



