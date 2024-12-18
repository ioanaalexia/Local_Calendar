import os
import json
import logging
from datetime import datetime, timedelta
from ics import Calendar
from parsers.ics_parser import ics_parse
from parsers.json_parser import json_parse
from alerts.alert_manager import generate_alerts

log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)

log_file_path = os.path.join(log_folder, "local_calendar.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    events = []
    input_folder = "events"

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if file_name.endswith(".ics"):
            events.extend(ics_parse(file_path))
        elif file_name.endswith(".json"):
            events.extend(json_parse(file_path))

    alerts = generate_alerts(events)
    if alerts:
        with open("alerts.log", "w", encoding="utf-8") as f:
            f.write("\n".join(alerts))
        logging.info("Alerte generate cu succes.")
    else:
        logging.info("Nu exista alerte pentru acest interval.")

if __name__ == "__main__":
    main()
