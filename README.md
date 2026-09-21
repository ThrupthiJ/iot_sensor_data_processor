# IoT Sensor Data Processor

A serverless IoT sensor data processing project developed as part of **Serverless Function Assignment – 8**.

## Project Overview

The project collects simulated IoT sensor readings such as temperature and humidity.

The sensor data is processed using **AWS Lambda**, stored in **Amazon DynamoDB**, and checked against predefined threshold values.

When a sensor value crosses the threshold, **Amazon SNS** sends an email notification.

## Objective

The objective of this project is to implement an IoT sensor data processor that:

- Collects temperature and humidity readings
- Processes the sensor data
- Stores the readings in a database
- Checks threshold conditions
- Generates an alert when a threshold is exceeded

## Technologies Used

- **AWS Lambda** – Processes the IoT sensor data
- **Amazon DynamoDB** – Stores sensor readings
- **Amazon SNS** – Sends threshold alert notifications
- **AWS IAM** – Provides permissions for the Lambda function
- **Python** – Used to develop the Lambda function
- **AWS CLI** – Used to create, configure, deploy and test AWS resources
- **Windows Command Prompt** – Used to run AWS CLI commands

## Architecture

```text
Simulated Sensor Data
        |
        v
AWS Lambda
(IoTSensorProcessor)
        |
        +--------------------+
        |                    |
        v                    v
Amazon DynamoDB         Amazon SNS
(IoTSensorData)       (IoTSensorAlerts)
                             |
                             v
                       Email Alert

**Threshold Conditions**

The project uses the following threshold values:

Sensor Value	Threshold	Alert
Temperature	> 30°C	High Temperature
Humidity	> 70%	High Humidity

If neither threshold is exceeded, the alert status is:

Normal
**Sample Input**

The Lambda function was tested using the following sensor data:

{
  "sensor_id": "24UG00238",
  "temperature": 35,
  "humidity": 80
}
**Processing**

For the sample input:

Temperature = 35°C → exceeds 30°C
Humidity = 80% → exceeds 70%

Therefore, the system generates:

High Temperature, High Humidity
**Result**

The Lambda function successfully processed the test input with StatusCode 200.

The sensor record was stored in DynamoDB with:

Sensor ID: 24UG00238
Temperature: 35°C
Humidity: 80%
Alert: High Temperature, High Humidity

An SNS threshold alert email was also successfully received.

**AWS Resources**
AWS Service	Resource
AWS Lambda	IoTSensorProcessor
Amazon DynamoDB	IoTSensorData
AWS IAM	IoTSensorLambdaRole
Amazon SNS	IoTSensorAlerts
**Lambda Function**

The Python Lambda function:

Reads the sensor ID, temperature and humidity.
Checks the temperature threshold.
Checks the humidity threshold.
Creates the alert message.
Stores the sensor reading in DynamoDB.
Sends an SNS notification when a threshold is breached.
Returns the processed sensor information.
**Database**

Sensor readings are stored in the DynamoDB table:

IoTSensorData

The table uses:

Partition Key: sensor_id
Sort Key: timestamp

The stored data includes:

sensor_id
timestamp
temperature
humidity
alert
**Email Alert**

When a threshold is breached, Amazon SNS sends an email containing the sensor information and alert status.

Example:

IoT Sensor Alert

Sensor ID: 24UG00238
Temperature: 35 °C
Humidity: 80 %
Alert: High Temperature, High Humidity
**Project Structure**
iot_sensor_data_processor/
│
├── Assignment_8_IoT_Sensor_Data_Processor_Thrupthi_GitHub_Safe.pdf
│
├── lambda_function.py
│
└── event.json
**Assignment Report**

The complete assignment report is included in this repository as a PDF.

The report contains:

Objective
Assignment requirement
AWS architecture
AWS resource details
Threshold logic
Implementation steps
Python Lambda code
Test input
Lambda execution evidence
DynamoDB storage evidence
SNS email alert evidence
Conclusion
**Author**

Thrupthi J

Student ID: 24UG00238

Assignment: 8 – IoT Sensor Data Processor

Region: Asia Pacific (Mumbai) – ap-south-1
