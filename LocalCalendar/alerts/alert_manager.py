from datetime import datetime

def generate_alerts(events):
    current_time = datetime.now()
    alerts = []

    for event in events:

        event_alert = event["alert"].replace(tzinfo=None)
        event_start = event["start"].replace(tzinfo=None)

        if event_alert <= current_time <= event_start:
            alert_message = f"Alerta: {event['title']} incepe la {event['start']}"
            alerts.append(alert_message)
            print(alert_message)

    return alerts