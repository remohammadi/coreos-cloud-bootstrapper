import os

VERSION = None

def get_version():
    global VERSION
    if not VERSION:
        VERSION = os.environ.get('BOOTSTRAPPER_VERSION', 'unspecified')
    return VERSION
