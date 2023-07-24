from threading import local

from .__logger import Logger

__local = local()


def logger(action='get_or_create'):
    match action.lower():
        case 'get_or_create':
            if not hasattr(__local, 'logger'):
                __local.logger = Logger()
            ret = __local.logger
        case 'set':
            __local.logger = Logger()
            ret = __local.logger
        case _:
            ret = None
    return ret


