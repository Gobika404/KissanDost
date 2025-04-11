### sensors/sensor_reader.py

python
import random

def get_sensor_data():
    """
    Simulates reading from soil moisture, temperature, and humidity sensors.
    In a real-world scenario, this would read data from connected sensors.
    """
    sensor_data = {
        "soil_moisture": round(random.uniform(20.0, 80.0), 2),  # in percentage
        "temperature": round(random.uniform(15.0, 40.0), 2),     # in Celsius
        "humidity": round(random.uniform(30.0, 90.0), 2)         # in percentage
    }
    return sensor_data


