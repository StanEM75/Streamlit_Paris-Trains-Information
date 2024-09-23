import pandas as pd
from datetime import datetime
import pytz

# Convert UTC time to local time in Paris and extract only the hour
def convert_utc_to_local_hour(utc_str):
    utc_time = datetime.fromisoformat(utc_str.replace('Z', '+00:00'))  # Convert ISO string to datetime
    paris_tz = pytz.timezone('Europe/Paris')  # Paris timezone
    local_time = utc_time.astimezone(paris_tz)  # Convert to Paris timezone
    return local_time.strftime('%H:%M:%S')  # Format the time only