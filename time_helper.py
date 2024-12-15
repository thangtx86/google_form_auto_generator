from datetime import datetime, timezone
import pytz

def convert_timestamp_to_custom_format(timestamp, timezone_name="Asia/Ho_Chi_Minh"):
    dt_object = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc) 
    local_tz = pytz.timezone(timezone_name)
    local_dt = dt_object.astimezone(local_tz)
    return local_dt.strftime("%d/%m/%Y %H:%M:%S")

def convert_to_timestamp(date_string, timezone_name="Asia/Ho_Chi_Minh"):
    local_tz = pytz.timezone(timezone_name)
    dt_object = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
    dt_object = local_tz.localize(dt_object)
    timestamp = dt_object.astimezone(pytz.utc).timestamp()
    return int(timestamp * 1000)

