#  KisanDost: Smart AI-Based Farming Assistant

KisanDost is an AI-powered farming assistant designed to help farmers make better decisions using real-time data, AI suggestions, and rural-friendly communication methods. It supports eco-friendly practices and is designed for low-power environments with limited internet access.

---

##  Problem Statement

Farmers face challenges in making informed decisions about crop selection, irrigation, and sustainability due to:

- Lack of real-time weather and soil data  
- Limited access to market trends and expert advice  
- Overuse of water, fertilizers, and pesticides  
- No system to store and learn from past farming patterns  

---

##  Proposed Solution

KisanDost offers a multi-agent AI system that:

- Uses IoT sensors to collect real-time environmental data  
- Provides personalized suggestions for crops, irrigation, and markets  
- Sends voice alerts in the local language for better accessibility  
- Stores data using SQLite for long-term memory and learning  
- Works with Edge AI for offline decision support  
- Uses **LoRaWAN** for rural data transmission  

---

##  Features

- ✅ Real-time soil and weather monitoring  
- ✅ Personalized crop and irrigation advice  
- ✅ Eco-friendly farming tips  
- ✅ Voice-based interaction in local language  
- ✅ Edge AI support for offline usage  
- ✅ LoRaWAN integration for rural areas  
- ✅ Market and weather-aware crop planning  

---

##  Technologies Used

- Python  
- SQLite  
- LoRaWAN  
- Federated Learning  
- IoT (ESP32, Soil Moisture Sensor, DHT11)  
- Speech Recognition  
- Edge AI  
- Blockchain (for secure FL – optional module)

---

## Code Structure


kisandost/
├── agents/                 # AI agents for different tasks
├── sensors/                # Code to read sensor data
├── models/                 # AI and FL models
├── database/               # SQLite memory
├── utils/                  # Utility functions (voice, LoRa, etc.)
├── main.py                 # Main controller
└── README.md               # Project documentation


##  How to Run

1. Clone the repository  
   bash
   git clone https://github.com/Gobika404/kissanDost.git
   cd kisandost
   

2. Install required libraries  
   bash
   pip install -r requirements.txt
   

3. Run the project  
   bash
   python main.py
   

---

## Contributors

-Gobika.S - Developer,Idea Lead
-Abinaya.R – Developer, Idea Lead  



