from sensors.sensor_reader import get_sensor_data
from ai.advisor import generate_advice
from voice.voice_alert import speak
from data.database import store_data
from utils.lorawan import send_data_lorawan

def main():
    print(" KisanDost Starting...")

    # Step 1: Collect data from sensors
    data = get_sensor_data()

    # Step 2: Store data to SQLite
    store_data(data)

    # Step 3: Generate advice using AI logic
    advice = generate_advice(data)

    # Step 4: Speak the advice
    speak(advice)

    # Step 5: Send data via LoRaWAN (mock)
    send_data_lorawan(data)

if __name__ == "__main__":
    main()
