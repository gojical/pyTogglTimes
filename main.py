# https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md
from requests import post
from tools import (
    get_config, import_times, get_delta_datetime
)

config = get_config()
times = import_times()

api_url = "https://api.track.toggl.com/api/v8/time_entries"

for entry in times:
    r = post(
        api_url,
        auth=(config["TOGGL_API"]["key"], "api_token"),
        json={
            "time_entry":
            {
                "description": entry['desc'],
                "created_with": "pyTogglTimes",
                "start": f"{entry['start']}T{entry['from']}:00{config['TOGGL_API']['timezone']}",
                "duration": get_delta_datetime(f"{entry['start']} {entry['from']}", f"{entry['start']} {entry['to']}"),
                "billable": entry["billable"],
                "pid": config['TOGGL_PROJECT_CODES'][entry["project"]],
                "wid": config["TOGGL_API"]["wid"]
            }
        }
    )
    if r.status_code != 200:
        print(
            f"[{r.text}] [{entry['start']} {entry['from']} -> {entry['to']}] [{entry['desc']}]")
    else:
        print(
            f"[{r.status_code}] [{entry['start']} {entry['from']} -> {entry['to']}] [{entry['desc']}]")
