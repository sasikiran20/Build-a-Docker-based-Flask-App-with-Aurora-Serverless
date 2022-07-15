# Build-a-Docker-based-Flask-App-with-Aurora-Serverless
## Services Used:
- AWS RDS
- Postman
- Docker
- AWS Secrets Manager 
- Flask
- Aurora Serverless
- pgAdmin

## Architectural Diagram:
![Architectural](https://user-images.githubusercontent.com/89773843/179214055-4a650f4c-af8f-419e-b140-9b173da719ca.png)

## Deployment:
#### Create a Database in RDS:
![Screenshot (1207)](https://user-images.githubusercontent.com/89773843/179214334-fb83bf26-e0bf-43d1-8421-6282e0a5f6b3.png)
![Screenshot (1208)](https://user-images.githubusercontent.com/89773843/179214363-cbfc9a1d-cd07-4442-b6b9-e03fcdffd6d0.png)
![Screenshot (1209)](https://user-images.githubusercontent.com/89773843/179214385-8759b50a-812a-44e5-bc58-b09641164fcd.png)
![Screenshot (1210)](https://user-images.githubusercontent.com/89773843/179214421-19a72785-7a16-4439-8923-329801a36413.png)
![Screenshot (1211)](https://user-images.githubusercontent.com/89773843/179214464-e49c110e-cab7-4852-bde8-981a8ac4b063.png)

#### Store the credentials in AWS Secret Manager:
![Screenshot (1213)](https://user-images.githubusercontent.com/89773843/179214612-c19acf96-6cfc-41bd-8506-e41e371bd821.png)

#### Connect the database using RDS Query Editor (or) pgAdmin:
![Screenshot (1231)](https://user-images.githubusercontent.com/89773843/179214853-ff7ee21f-edb2-4e46-a514-379e0fb4585e.png)

#### Create the Table for the Database:
![Screenshot (1219)](https://user-images.githubusercontent.com/89773843/179215424-5f353209-459c-4e7b-877b-7d1a0aa4d371.png)
![Screenshot (1220)](https://user-images.githubusercontent.com/89773843/179215453-420df645-32f4-4975-b18f-80a7822e09d9.png)
![Screenshot (1221)](https://user-images.githubusercontent.com/89773843/179215477-b4110a1c-a0cf-4c21-a580-85486ae8c510.png)

#### Build the flask app in the docker:
![Screenshot (1222)](https://user-images.githubusercontent.com/89773843/179215690-68fea88f-51fd-4c6a-ba32-50e0ab84decb.png)
![Screenshot (1224)](https://user-images.githubusercontent.com/89773843/179215772-f3f35041-dc33-495f-9639-2205768a5e00.png)

#### If it is succeeded we can start the docker app:
![Screenshot (1225)](https://user-images.githubusercontent.com/89773843/179216187-c4358289-fd9a-40b0-bb58-bb92d11f267b.png)
![Screenshot (1226)](https://user-images.githubusercontent.com/89773843/179216234-7f4cad38-1318-4ebc-bf01-74c14b841909.png)

#### Send the Data through the Postman:
![Screenshot (1227)](https://user-images.githubusercontent.com/89773843/179216372-2a60e775-1215-4008-a087-5239810c48c2.png)

#### The data is saved in the RDS:
![Screenshot (1228)](https://user-images.githubusercontent.com/89773843/179216623-37be0cba-2de8-46f1-8947-4d76fb36d4be.png)









