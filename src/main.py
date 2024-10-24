import time
from datetime import datetime
from typing import Dict, Any

from .config import Config
from .api_client import WeatherAPIClient
from .database import DatabaseManager
from .data_processor import DataProcessor
from .alerts import AlertSystem
from .visualization import Visualizer

def main():
    config = Config()
    api_client = WeatherAPIClient(config.API_KEY)
    db_manager = DatabaseManager(config)
    data_processor = DataProcessor(db_manager)
    alert_system = AlertSystem(config.ALERT_THRESHOLD, config.CONSECUTIVE_ALERTS)
    visualizer = Visualizer()
    
    while True:
        for city in config.CITIES:
            try:
                # Fetch and process weather data
                weather_data = api_client.get_weather_data(city)
                
                # Save to database
                db_manager.save_weather_data(weather_data)
                
                # Check for alerts
                alert_system.check_temperature_alert(
                    city, weather_data['temp']
                )
                
                # Calculate daily summary if it's the end of the day
                now = datetime.now()
                if now.hour == 23 and now.minute >= 55:
                    data_processor.calculate_daily_summary(city, now)
                
            except Exception as e:
                print(f"Error processing data for {city}: {str(e)}")
        
        # Sleep until next update
        time.sleep(config.UPDATE_INTERVAL)

if __name__ == "__main__":
    main()