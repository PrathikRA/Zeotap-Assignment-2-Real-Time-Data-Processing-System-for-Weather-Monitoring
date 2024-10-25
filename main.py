from weather_data_fetch import WeatherDataProcessor
from alerting_manager import AlertManager
from database_manage import DBManager
from runtest import TEMP_THRESHOLD

if __name__ == "__main__":
    processor = WeatherDataProcessor()
    db_manager = DBManager('weather.db')
    alert_manager = AlertManager(TEMP_THRESHOLD)

    while True:
        # latest weather data
        weather_data = processor.process_data()

        # Check for alert conditions
        alert_manager.check_for_alert(weather_data)
