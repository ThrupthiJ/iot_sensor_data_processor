import json
import boto3
from decimal import Decimal
from datetime import datetime, timezone
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("IoTSensorData")
sns = boto3.client("sns", region_name="ap-south-1")
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:ACCOUNT_ID:IoTSensorAlerts"
TEMPERATURE_LIMIT = 30
HUMIDITY_LIMIT = 70
def lambda_handler(event, context):
    sensor_id = event.get("sensor_id", "24UG00238")
    temperature = Decimal(str(event.get("temperature", 0)))
    humidity = Decimal(str(event.get("humidity", 0)))
    alerts = []
    if temperature > TEMPERATURE_LIMIT:
        alerts.append("High Temperature")
    if humidity > HUMIDITY_LIMIT:
        alerts.append("High Humidity")
    alert = ", ".join(alerts) if alerts else "Normal"
    timestamp = datetime.now(timezone.utc).isoformat()
    item = {"sensor_id": sensor_id, "timestamp": timestamp,
            "temperature": temperature, "humidity": humidity, "alert": alert}
    table.put_item(Item=item)
    if alerts:
        message = ("IoT Sensor Alert\n\n"
                   f"Sensor ID: {sensor_id}\n"
                   f"Temperature: {temperature} °C\n"
                   f"Humidity: {humidity} %\n"
                   f"Alert: {alert}\n"
                   f"Time: {timestamp}")
        sns.publish(TopicArn=SNS_TOPIC_ARN,
                    Subject="IoT Sensor Threshold Alert",
                    Message=message)
    return {"statusCode": 200,
            "body": json.dumps({"sensor_id": sensor_id,
                                "temperature": float(temperature),
                                "humidity": float(humidity),
                                "alert": alert})}
