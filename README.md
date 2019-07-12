# Rest API with connection to Autonomous Database from SaaS Application

## Objective

In this lab we will create REST APIs using Python Flask that is connected to Autonomous Database. 
It can be used by different SaaS applications. 

## Pre-requisites

- The following lab requires an Oracle Public Cloud account with Autonomous Data Warehouse Cloud Service.

- You need to have a connection to database through admin in your SQL Developer. 

    - Open up your SQL Developer and create a new connection for admin. If you already have a connection, skip this step. 

    - Enter the following details for admin:

        1.	Connection Name: GIve any connection name
        2.	Username: admin (or any DB user)
        3.	Password: Password you entered while creating database on cloud.
        4.	Connection Type: Cloud PDB
        5.	Configuration File: Path to your wallet
        6.	Keystore Password: Password entered while downloading wallet. 

        ![](Data/login.png)

    - Click on Test, if it shows success, click on save and then click on connect. 
    
- You should have your local environment configured with instant client and the wallet. 
    - Download Client Credentials (Wallets): Please follow this link to download the wallet:
    https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/user/connect-download-wallet.html#GUID-B06202D2-0597-41AA-9481-3B174F75D4B1

    - Download Instant Client - "Basic Package - All files required to run OCI, OCCI, and JDBC-OCI applications" from the           following link: https://www.oracle.com/technetwork/topics/intel-macsoft-096467.html. 
      NOTE: You need to accept the agreement first before downloading the package.  Unzip the file.

    - Unzip the Autonomous wallet downloaded, and navigate to sqlnet.ora. 
        Edit sqlnet.ora as follows:

        nano sqlnet.ora

        WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY=**$TNS_ADMIN**)))
    SSL_SERVER_DN_MATCH=yes
    
    - Set LD_LIBRARY_PATH. Type the following command in your command prompt:
    
        **export LD_LIBRARY_PATH=Path of your instant client folder:$LD_LIBRARY_PATH**
    
        Note: Repeat this everytime you restart the laptop. Or add the above command in your ~/.bash_profile.
    
    - Set env variables TNS_AMDIN to point to the wallet folder. Type the following command in your command prompt:
    
        **export TNS_ADMIN=Path of your unzipped wallet folder**

        Note: Repeat this everytime you restart the laptop. Or add the above command in your ~/.bash_profile.
        
### **Step 1**: Create channels table in Autonomous Database.

- Download the csv file. [channels.csv](Data/channels.csv)

- Upload data from the following csv file in your autonomous database.

    1. Right click on **table** and then **import data**.

        ![](importdata.png)
        
    2. Leave the source as **Local File**, click on Browse and select the downloaded csv file.
    
        ![](browse.png)
        
    3. Give table name as "channels".
    
        ![](Data/tablename.png)

    4. Click on next till you reach the review page and click on finish. Table is created and the data is loaded.
    
### **Step 2**: Download and configure the script.

- Download the following script [app.py](app.py)

- Open this script and change the following parameter in the code:

    **username = "Your username"  
    password = "Your password"  
    service_name = "Your service name"**
    
- now run the script as **python app.py**
  

### **Step 3**: Run the application.

- Set environment variable "FLASK_APP" to the path of the app.py
  
  **export FLASK_APP=path to app.py**
  
- Type following command in command line:

  **flask run --host=0.0.0.0 --port=5000**

- Now open any web browser and type **"localhost:5000/channels"**

  You will see channels information on the browser. 
  
  You can also deploy this application in a compute instance and can use the REST API in SaaS Applications.

