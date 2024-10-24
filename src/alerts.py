import smtplib
from email.mime.text import MIMEText
from typing import List, Dict
from datetime import datetime, timedelta

class AlertSystem:
    def __init__(self, threshold: float, consecutive_alerts: int):
        self.threshold = threshold
        self.consecutive_alerts = consecutive_alerts
        self.alert_history = {}
    
    def check_temperature_alert(self, city: str, temp: float) -> bool:
        if city not in self.alert_history:
            self.alert_history[city] = []
        
        self.alert_history[city].append(temp)
        if len(self.alert_history[city]) > self.consecutive_alerts:
            self.alert_history[city].pop(0)
        
        if (len(self.alert_history[city]) == self.consecutive_alerts and
            all(t > self.threshold for t in self.alert_history[city])):
            self._send_alert(city, temp)
            return True
        return False
    
    def _send_alert(self, city: str, temp: float):
        message = (
            f"ALERT: Temperature in {city} has exceeded {self.threshold}°C "
            f"for {self.consecutive_alerts} consecutive readings. "
            f"Current temperature: {temp:.1f}°C"
        )
        print(message)