# pyToggleTimes 🐍⌚📅

## Quick Start

1. Create a python3 virtual environment `virtualenv .env -p python3` use `pip install virtualenv` if you dont have virtualenv avalible, make sure that you're paths are setup properly
2. Enter environment `source .env/bin/activate` or `.env/Scripts/activate.ps1` on windows
3. Install packages `pip install -e .`
4. create a config from the sample config `cp SAMPLE_CONFIG.ini CONFIG.ini`
5. update the `CONFIG.ini` with your
   - toggl api key
   - timezone
   - toggl work_id
   - toggl project id's
6. add times to `times.json`
7. Once you are happy run `python ./main.py`
8. Sit back, relax and enjoy the magic 🎆🎇

## Extra Info

- Developed using this doc: [Toggl API](https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md)
- Uses Python3 and the request package
- Does not support tagging currenty
