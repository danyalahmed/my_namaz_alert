import json
import requests
import time
from datetime import datetime
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.event import track_time_interval

API_URL = "{api_url}"

def get_namaz_timings():
    response = requests.get(API_URL)
    data = response.json()
    if "multiDayTimings" not in data or not data["multiDayTimings"]:
        raise HomeAssistantError("Invalid response from the API")

    timings = data["multiDayTimings"][0]
    date = datetime.fromtimestamp(timings["date"] / 1000).strftime("%Y-%m-%d")

    namaz_timings = {
        "Fajr": datetime.fromtimestamp(timings["prayers"][0]["time"] / 1000).strftime("%H:%M"),
        "Zuhr": datetime.fromtimestamp(timings["prayers"][2]["time"] / 1000).strftime("%H:%M"),
        "Asr": datetime.fromtimestamp(timings["prayers"][3]["time"] / 1000).strftime("%H:%M"),
        "Maghrib": datetime.fromtimestamp(timings["prayers"][5]["time"] / 1000).strftime("%H:%M"),
        "Isha": datetime.fromtimestamp(timings["prayers"][6]["time"] / 1000).strftime("%H:%M")
    }

    return date, namaz_timings

def create_namaz_alerts(hass):
    date, namaz_timings = get_namaz_timings()

    for namaz, timing in namaz_timings.items():
        time_obj = datetime.strptime(timing, "%H:%M")
        alert_time = datetime.combine(datetime.now().date(), time_obj.time())
        if alert_time > datetime.now():
            hass.services.call(
                "persistent_notification",
                "create",
                {
                    "message": f"{namaz} Namaz Alert for {date} at {timing}",
                    "title": "Namaz Alert"
                },
            )

def setup(hass, config):
    def run_interval(event_time):
        create_namaz_alerts(hass)

    interval = config.get("interval", 60)

    track_time_interval(hass, run_interval, interval)

    return True

