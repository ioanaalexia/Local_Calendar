import logging
from ics import Calendar
from datetime import timedelta

def ics_parse(file_path):
    events = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            calendar = Calendar(file.read())
            for event in calendar.events:
                alert_time = event.begin.datetime - timedelta(minutes=30)

                if event.alarms:
                    for alarm in event.alarms:
                        if alarm.trigger:
                            alert_time = event.begin.datetime + alarm.trigger

                events.append({
                    "title": event.name,
                    "start": event.begin.datetime,
                    "alert": alert_time,
                })
        logging.info(f"Fisierul ICS a fost procesat: {file_path}")
    except Exception as e:
        logging.error(f"Eroare la procesarea fisierului ICS: {file_path}, cu eroarea {e}")
    return events