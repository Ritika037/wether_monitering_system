from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class WeatherReading(Base):
    __tablename__ = 'weather_readings'
    
    id = Column(Integer, primary_key=True)
    city = Column(String, index=True)
    temperature = Column(Float, nullable=False)
    feels_like = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    wind_speed = Column(Float)
    main_condition = Column(String)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f"<WeatherReading(city='{self.city}', temp={self.temperature}°C)>"

class DailySummary(Base):
    __tablename__ = 'daily_summaries'
    
    id = Column(Integer, primary_key=True)
    city = Column(String, index=True)
    date = Column(DateTime, index=True)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    avg_humidity = Column(Float)
    dominant_condition = Column(String)
    reading_count = Column(Integer)
    
    def __repr__(self):
        return f"<DailySummary(city='{self.city}', date='{self.date.date()}')>"

class Alert(Base):
    __tablename__ = 'alerts'
    
    id = Column(Integer, primary_key=True)
    city = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    alert_type = Column(String)
    message = Column(String)
    reading_id = Column(Integer, ForeignKey('weather_readings.id'))
    reading = relationship("WeatherReading")