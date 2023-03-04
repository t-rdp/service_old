import requests
import misc

def get_invite_code():
    r = requests.post(misc.config["misskey"]["host"] + '/api/invite',
                      json={"i": misc.config["misskey"]["i"]})
    value = r.json()
    return value['code']