### ai/advisor.py

python
def analyze_data(sensor_data):
    """
    Provides basic farming advice based on sensor data.
    """
    recommendations = []

    # Soil moisture recommendation
    if sensor_data["soil_moisture"] < 30:
        recommendations.append("Soil moisture is low. Consider irrigating the field.")
    elif sensor_data["soil_moisture"] > 70:
        recommendations.append("Soil moisture is high. Avoid over-irrigation.")

    # Temperature recommendation
    if sensor_data["temperature"] > 35:
        recommendations.append("Temperature is high. Provide shade or increase watering for heat-sensitive crops.")
    elif sensor_data["temperature"] < 18:
        recommendations.append("Temperature is low. Consider protective measures for crops.")

    # Humidity recommendation
    if sensor_data["humidity"] > 80:
        recommendations.append("High humidity detected. Monitor for potential fungal infections.")

    if not recommendations:
        recommendations.append("All conditions are optimal. Keep monitoring regularly.")

    return recommendations


