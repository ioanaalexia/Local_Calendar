import logging
from ics import Calendar
from datetime import timedelta

def ics_parse(file_path):
    events = []
    try:
        with open(file_path, 'r') as file:
            calendar = Calendar(file.read())
            for event in calendar.events:
                events.append({
                    "title": event.name,
                    "start": event.begin.datetime,
                    "alert": event.begin.datetime - timedelta(minutes=30),
                })
        logging.info(f"Fisierul ICS a fost procesat: {file_path}")
    except Exception as e:
        logging.error(f"Eroare la procesarea fisierului ICS: {file_path}, cu eroarea {e}")
    return events