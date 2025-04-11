# app/main.py

from agents.farmer_agent import FarmerAgent
from agents.weather_agent import WeatherAgent
from agents.market_agent import MarketAgent
from agents.sustainability_agent import SustainabilityAgent
from utils.sqlite_handler import SQLiteHandler
from utils.sensor_data import get_soil_data, get_weather_data
from utils.voice_assist import speak

def main():
    # Initialize SQLite database
    db = SQLiteHandler("farm_data.db")

    # Create agent instances
    farmer = FarmerAgent(db)
    weather = WeatherAgent()
    market = MarketAgent()
    sustainability = SustainabilityAgent()

    # Collect sensor data
    soil_data = get_soil_data()
    weather_data = get_weather_data()

    # Agent decisions
    crop = farmer.recommend_crop(soil_data, weather_data)
    irrigation = weather.irrigation_schedule(weather_data)
    price_tip = market.suggest_market_crop()
    eco_tip = sustainability.get_sustainability_tip()

    # Voice alerts in local language (simulated)
    speak(f"Recommended Crop: {crop}")
    speak(f"Irrigation Advice: {irrigation}")
    speak(f"Market Suggestion: {price_tip}")
    speak(f"Eco Tip: {eco_tip}")

if _name_ == "_main_":
    main()
