import logging
import json
from datetime import datetime

def json_parse(file_path):
    events = []
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            for event in data.get("events", []):
                events.append({
                    "title": event["title"],
                    "start": datetime.fromisoformat(event["start"]),
                    "alert": datetime.fromisoformat(event["alert"]),
                })
        logging.info(f"Fisier JSON procesat: {file_path}")
    except Exception as e:
        logging.error(f"Fisier la procesarea fisierului JSON: {file_path}. Eroare: {e}")
    return events