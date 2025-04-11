### utils/lorawan.py

python
# utils/lorawan.py

import time
import random

class LoRaWAN:
    def __init__(self, device_id):
        self.device_id = device_id
        print(f"[LoRaWAN] Device {device_id} initialized.")

    def send_data(self, data):
        """
        Simulates sending data over a LoRaWAN network.
        """
        print(f"[LoRaWAN] Sending data: {data}")
        time.sleep(1)
        print(f"[LoRaWAN] Data sent successfully.")

    def receive_data(self):
        """
        Simulates receiving data from a remote node.
        """
        print("[LoRaWAN] Receiving data...")
        time.sleep(1)
        sample_data = {
            "soil_moisture": random.uniform(20, 60),
            "temperature": random.uniform(25, 40),
            "humidity": random.uniform(40, 80)
        }
        print(f"[LoRaWAN] Data received: {sample_data}")
        return sample_data

