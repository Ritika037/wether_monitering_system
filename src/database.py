from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class WeatherRecord(Base):
    __tablename__ = 'weather_records'
    
    id = Column(Integer, primary_key=True)
    city = Column(String)
    main_condition = Column(String)
    temperature = Column(Float)
    feels_like = Column(Float)
    timestamp = Column(DateTime)
    
class WeatherSummary(Base):
    __tablename__ = 'weather_summaries'
    
    id = Column(Integer, primary_key=True)
    city = Column(String)
    date = Column(DateTime)
    avg_temp = Column(Float)
    max_temp = Column(Float)
    min_temp = Column(Float)
    dominant_condition = Column(String)

class DatabaseManager:
    def __init__(self, config: Config):
        self.engine = create_engine(
            f'postgresql://{config.DB_USER}:{config.DB_PASSWORD}@'
            f'{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
        )
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def save_weather_data(self, data: dict):
        session = self.Session()
        try:
            record = WeatherRecord(
                city=data['city'],
                main_condition=data['main_condition'],
                temperature=data['temp'],
                feels_like=data['feels_like'],
                timestamp=data['timestamp']
            )
            session.add(record)
            session.commit()
        finally:
            session.close()