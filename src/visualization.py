import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from typing import List, Dict
import seaborn as sns

class Visualizer:
    def create_temperature_trend(self, data: List[Dict]) -> str:
        plt.figure(figsize=(12, 6))
        for city in set(d['city'] for d in data):
            city_data = [d for d in data if d['city'] == city]
            plt.plot(
                [d['timestamp'] for d in city_data],
                [d['temp'] for d in city_data],
                label=city
            )
        
        plt.title('Temperature Trends Across Cities')
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid(True)
        
        # Save plot to file
        filename = f'temperature_trend_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
        plt.savefig(filename)
        plt.close()
        return filename