# app/agents/farmer_agent.py

class FarmerAgent:
    def _init_(self, db):
        self.db = db

    def recommend_crop(self, soil_data, weather_data):
        # Example logic based on moisture and temperature
        moisture = soil_data.get("moisture")
        temperature = weather_data.get("temperature")

        if moisture > 60 and 20 < temperature < 30:
            crop = "Rice"
        elif moisture < 40:
            crop = "Millets"
        else:
            crop = "Wheat"

        # Store the recommendation in the database
        self.db.save_crop_recommendation(crop)
        return crop
