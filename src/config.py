# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    CITIES = [
        'Delhi', 'Mumbai', 'Chennai', 
        'Bangalore', 'Kolkata', 'Hyderabad'
    ]
    UPDATE_INTERVAL = 300  # 5 minutes in seconds
    TEMPERATURE_UNIT = 'celsius'  # or 'fahrenheit'
    ALERT_THRESHOLD = 35  # degrees Celsius
    CONSECUTIVE_ALERTS = 2
    
    # Database configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME', 'weather_db')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')

# api_client.py
import requests
from datetime import datetime
from typing import Dict, Any
from .config import Config

class WeatherAPIClient:
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def get_weather_data(self, city: str) -> Dict[str, Any]:
        params = {
            'q': f"{city},IN",
            'appid': self.api_key,
        }
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        return self._process_response(data)
    
    def _process_response(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'city': data['name'],
            'main_condition': data['weather'][0]['main'],
            'temp': self._kelvin_to_celsius(data['main']['temp']),
            'feels_like': self._kelvin_to_celsius(data['main']['feels_like']),
            'timestamp': datetime.fromtimestamp(data['dt'])
        }
    
    @staticmethod
    def _kelvin_to_celsius(kelvin: float) -> float:
        return kelvin - 273.15