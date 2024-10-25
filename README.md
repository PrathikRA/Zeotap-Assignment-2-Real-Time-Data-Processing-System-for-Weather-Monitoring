Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
Weather Monitoring System
Project Overview This real-time weather monitoring system continuously retrieves weather data from the OpenWeatherMap API for selected metro cities in India. The system processes the data, calculates rollups (average, max, min temperatures, dominant weather conditions), stores daily summaries, and triggers alerts if user-defined weather thresholds are breached.

Key Features
Real-time data retrieval from OpenWeatherMap API for cities like Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad. Daily weather summaries that calculate average, max, min temperatures, and dominant weather conditions. Alerting system to notify users when specific weather conditions (like high temperature) are met. Database storage of daily weather summaries for further analysis. Visualizations (optional) of weather trends and triggered alerts.

1. Setup Instructions
1.1 Get an API Key from OpenWeatherMap Go to OpenWeatherMap API. Sign up for a free account. Once logged in, navigate to the API keys section in your account. Copy your API key, which will be needed to access weather data.

1.2 Clone the Repository

--git clone https://github.com/your-username/weather-monitoring-system.git

--cd weather-monitoring-system

1.3 Configure the Project Update config.py with your API key, preferred cities, and polling intervals: Open src/config.py:

OPENWEATHER_API_KEY = 'your_openweather_api_key_here' # Replace with your actual API key

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad'] # You can modify the city list here

POLL_INTERVAL = 300 # Interval to fetch weather data in seconds (default: 5 minutes)

TEMP_THRESHOLD = 35 # Example threshold for triggering alerts in Celsius

Adjust the cities and interval as per your requirements.

2. Running the Application
2.1 Install Dependencies This project requires Python 3.9 or higher. Install the required dependencies using the following:

pip install -r requirements.txt

2.2 Running with Python After configuring the config.py file, you can run the application directly using Python:

python src/main.py

2.3 Running with Docker This project can be run in a Docker container for easy deployment.

Build the Docker image:

docker build -t weather-monitoring-system .

Run the Docker container:

docker run -d weather-monitoring-system

3. Dependencies
requests: To interact with the OpenWeatherMap API for retrieving weather data.

sqlite3: For local data storage of daily weather summaries (part of the Python standard library).

matplotlib (optional): To generate visualizations of weather trends and triggered alerts.

Docker (optional): For containerized deployment of the system.

4. Design Decisions
4.1 Python for Simplicity and Flexibility Python was chosen as the primary language due to its simplicity, extensive library support (such as requests for API interaction), and flexibility for handling data processing.

4.2 SQLite for Lightweight Data Storage SQLite is used as the database to store daily weather summaries due to its lightweight nature and ease of use. It doesn't require any setup or external dependencies, making it ideal for this type of project.

4.3 Modular Structure The code is split into multiple modules (weather_data_processor.py, alert_manager.py, db_manager.py) to ensure separation of concerns and make the system easier to extend and maintain.

4.4 Docker for Portability Docker was included to containerize the system, allowing it to run consistently across various environments. This makes the application easy to deploy, test, and scale if needed.

5. Additional Features and Extension Ideas
5.1 Extending Weather Parameters Additional weather parameters such as humidity, wind speed, and pressure can be retrieved from the API and incorporated into the daily summaries and alerting system.

5.2 Weather Forecast The system can be extended to fetch weather forecasts from the API and generate insights or alerts based on predicted conditions.

6. Testing the Application
Test cases are available in the tests/ folder. You can run the tests using any Python test runner, such as pytest:

pytest tests/Tests include:

Data retrieval and parsing

Temperature conversions

Daily rollup and aggregation logic

Alerting conditions
