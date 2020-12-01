from configparser import ConfigParser
from datetime import datetime


def get_config(file_name="CONFIG.ini"):
    config = ConfigParser()
    config.read(file_name)
    return config


def get_delta_datetime(initial_stamp, end_stamp):
    init_dto = datetime.strptime(initial_stamp, '%Y-%m-%d %H:%M')
    end_dto = datetime.strptime(end_stamp, '%Y-%m-%d %H:%M')
    diff = end_dto-init_dto
    return int(diff.total_seconds())


def import_times(file_name="times.json"):
    import json
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data


# get_delta_datetime("2010-01-01 04:55", "2010-01-01 10:55")
# print(get_config()['TOGGL_API']['key'])
