# Weather Monitoring System

This is a real-time weather monitoring system that collects data from OpenWeatherMap API for major Indian metros, processes it, and provides insights through rollups and aggregates.

## Features

- Real-time weather data collection for 6 major Indian metros
- Temperature conversion and processing
- Daily weather summaries with aggregates
- Configurable alerting system
- Data visualization
- Comprehensive test coverage

## Architecture

The system is built using a modular architecture with the following components:

1. **API Client**: Handles communication with OpenWeatherMap API
2. **Data Processor**: Processes raw weather data and calculates aggregates
3. **Database Manager**: Handles data persistence using PostgreSQL
4. **Alert System**: Monitors weather conditions and triggers alerts
5. **Visualization**: Creates graphs and charts for weather trends

## Prerequisites

- Docker and Docker Compose
- OpenWeatherMap API key
- Python 3.9 or higher (for local development)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-monitoring-system.git
   cd weather-monitoring-system
   ```

2. Create a `.env` file with your OpenWeatherMap API key:
   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```

3. Build and start the services:
   ```bash
   docker-compose up --build
   ```

## Configuration

The system can be configured through the `config.py` file or environment variables:

- `UPDATE_INTERVAL`: Frequency of API calls (default: 5 minutes)
- `TEMPERATURE_UNIT`: Preferred temperature unit (celsius/fahrenheit)
- `ALERT_THRESHOLD`: Temperature threshold for alerts
- `CONSECUTIVE_ALERTS`: Number of consecutive readings needed to trigger an alert

## Design Choices

1. **Data Storage**: PostgreSQL was chosen for:
   - ACID compliance
   - Rich querying capabilities
   - Time-series data support

2. **Containerization**: Docker is used to ensure:
   - Consistent development environment
   - Easy deployment
   - Scalability

3. **Modular Architecture**:
   - Loose coupling between components
   - Easy to test and maintain
   - Extensible for future features

4. **Alert System**:
   - Configurable thresholds
   - Support for multiple alert types
   - Console and email notification options

## Testing

Run the tests using:

```bash
docker-compose run app pytest
```

## Future Enhancements

1. Add support for more weather parameters
2. Implement weather forecast analysis
3. Add web interface for visualization
4. Implement more sophisticated alerting mechanisms
5. Add support for more cities and regions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.