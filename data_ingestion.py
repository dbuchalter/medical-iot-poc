from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json

class DataIngestionService:
    def __init__(self):
        # MQTT Connection (Add callback_api_version parameter for compatibility)
        self.mqtt_client = mqtt.Client(client_id="data_ingestion_service", callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("localhost", 1883)

        # InfluxDB Connection
        self.influx_client = InfluxDBClient(
            url="http://localhost:8086", 
            token="_3Z2e9Z72x3EzujxBvSDbvTXpLDDUFPEcFJJ7C0j0viWQABwANm6KpY4F558o4JiU3qrbyuS7FxAAefLJlNB2Q==", 
            org="medical-org"
        )
        self.write_api = self.influx_client.write_api(write_options=SYNCHRONOUS)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT Broker")
        client.subscribe("medical/device/data")

    def on_message(self, client, userdata, message):
        try:
            data = json.loads(message.payload.decode())
            point = Point("medical_device_metrics") \
                .tag("device_id", data['device_id']) \
                .field("temperature", data['temperature']) \
                .field("heart_rate", data['heart_rate']) \
                .field("oxygen_saturation", data['oxygen_saturation'])
            
            self.write_api.write(bucket="medical_devices", record=point)
        except Exception as e:
            print(f"Error processing message: {e}")

    def start(self):
        self.mqtt_client.loop_forever()

# Usage
service = DataIngestionService()
service.start()