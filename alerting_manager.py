class AlertManager:
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def check_for_alert(self, weather_data):
        """
        Check whether weather data exceeds user-configurable thresholds.
        """
        for data in weather_data:
            if data['temp_c'] > self.threshold:
                self.trigger_alert(data)

    def trigger_alert(self, data):
        """
        Trigger alert for weather conditions that exceed thresholds.
        """
        if not self.alert_triggered:
            print(f"ALERT! High temperature in {data['city']}: {data['temp_c']}°C")
            # Email notification logic can go here
            self.alert_triggered = True

    def reset_alert(self):
        self.alert_triggered = False
