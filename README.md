# Modify Instance Type using Lambda

## Introduction:
AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware 
cluster scaling logic, maintaining event integrations, or managing runtimes. Here I Am Going to explain how to automate the AWS EC2 
instance type at the scheduled times.

Following are the steps to be followed:
1. Define the Size to be modified
2. Define the Instance Id
3. Stop the Instance
4. Modify Instance Type
5. Start the Instance

## Step-by-Step explanation:
1. Create IAM Role-
      * Create IAM Role with the following policy: EC2FullAccess
      
2. Create a Lambda function-
      * Open Lambda Console, Create Function
      * Enter the function Name, Select Python 3.9, attach the IAM Role created here
      * Click on Create Function, will redirect to the Function page with Basic Lambda Code, copy the below Lambda code and paste it in the console.
      * [Refer This File](https://github.com/KAJOLMEHTAA/Modify_Instance_type/blob/main/modify_type.py)
