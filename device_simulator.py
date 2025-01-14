import random
import time
import paho.mqtt.client as mqtt
import json
from datetime import datetime

class MedicalDeviceSimulator:
    def __init__(self, device_id):
        self.device_id = device_id
        # Specify callback_api_version to fix compatibility issue
        self.mqtt_client = mqtt.Client(client_id=f"medical_device_{device_id}", callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        self.mqtt_client.connect("localhost", 1883)  # Connect to the MQTT broker

    def generate_sensor_data(self):
        return {
            "device_id": self.device_id,
            "timestamp": datetime.now().isoformat(),
            "temperature": round(random.uniform(35.5, 37.5), 2),
            "heart_rate": random.randint(60, 100),
            "blood_pressure": {
                "systolic": random.randint(110, 140),
                "diastolic": random.randint(70, 90)
            },
            "oxygen_saturation": round(random.uniform(95.0, 100.0), 1)
        }

    def publish_data(self):
        print(f"Starting device simulator: {self.device_id}")
        while True:
            data = self.generate_sensor_data()
            print(f"Publishing: {data}")
            self.mqtt_client.publish("medical/device/data", json.dumps(data))
            time.sleep(5)  # Send data every 5 seconds

# Usage
if __name__ == "__main__":
    simulator = MedicalDeviceSimulator("dental_unit_001")
    simulator.publish_data()
