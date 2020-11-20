# https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md
from requests import post
from configparser import ConfigParser

from times import toggl_input

config = ConfigParser()
config.read("CONFIG.ini")


def time_to_sec(time_yup):
    seconds = 0
    seconds += time_yup[0] * 3600
    seconds += time_yup[1] * 60
    seconds += time_yup[2]
    return seconds

api_url = "https://api.track.toggl.com/api/v8/time_entries"

for entry in toggl_input:
    r = post(
        api_url,
        auth=(config["TOGGL_API"]["key"], "api_token"),
        json={
            "time_entry": 
            {
                "description": entry['desc'],
                "created_with": "pyTogglTimes",
                "start": f"{entry['start']}T{entry['from']}:00+02:00",
                "duration": time_to_sec(entry['dur']),
                "billable": entry["billable"],
                "pid": entry["project"].value,
                "wid": config["TOGGL_API"]["wid"]
            }
        }
    )
    print("---------------------------------------")
    print(r.status_code)
    if r.status_code != 200:
        print(r.text)
