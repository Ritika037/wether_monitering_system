from collections import Counter
from datetime import datetime, timedelta
from typing import List, Dict
from sqlalchemy import func
from .database import DatabaseManager, WeatherRecord, WeatherSummary

class DataProcessor:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def calculate_daily_summary(self, city: str, date: datetime) -> Dict:
        session = self.db.Session()
        try:
            # Get all records for the specified city and date
            records = session.query(WeatherRecord).filter(
                WeatherRecord.city == city,
                func.date(WeatherRecord.timestamp) == date.date()
            ).all()
            
            if not records:
                return None
            
            temperatures = [r.temperature for r in records]
            conditions = [r.main_condition for r in records]
            
            summary = {
                'city': city,
                'date': date,
                'avg_temp': sum(temperatures) / len(temperatures),
                'max_temp': max(temperatures),
                'min_temp': min(temperatures),
                'dominant_condition': Counter(conditions).most_common(1)[0][0]
            }
            
            # Save summary to database
            self._save_summary(summary)
            return summary
        finally:
            session.close()
    
    def _save_summary(self, summary: Dict):
        session = self.db.Session()
        try:
            summary_record = WeatherSummary(
                city=summary['city'],
                date=summary['date'],
                avg_temp=summary['avg_temp'],
                max_temp=summary['max_temp'],
                min_temp=summary['min_temp'],
                dominant_condition=summary['dominant_condition']
            )
            session.add(summary_record)
            session.commit()
        finally:
            session.close()