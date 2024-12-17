import logging
import json
from datetime import datetime

def json_parse(file_path):
    events = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for event in data.get("events, []"):
                events.append({
                    "title": event["title"],
                    "start": datetime.fromisoformat(event["start"]),
                    "alert": datetime.fromisoformat(event["alert"]),
                })
        logging.info(f"Fisierul JSON a fost procesat: {file_path}")
    except Exception as e:
        logging.error(f"Eroare la procesarea fisierului JSON: {file_path}, cu eroarea {e}")
    return events