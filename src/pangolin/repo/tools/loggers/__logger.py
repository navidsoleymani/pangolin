from datetime import datetime
import secrets


class Logger:
    def __init__(self):
        self.id_ = secrets.token_hex()
        self.__errors: list = list()
        self.__warnings: list = list()
        self.__debugs: list = list()
        self.__exceptions: list = list()

    def error(self, msg: str):
        self.__errors.append(
            {
                'message': msg,
                'datetime': datetime.now()
            }
        )

    def warning(self, msg: str):
        self.__warnings.append(
            {
                'message': msg,
                'datetime': datetime.now()
            }
        )

    def debug(self, msg: str):
        self.__debugs.append(
            {
                'message': msg,
                'datetime': datetime.now()
            }
        )

    def exception(self, msg: str):
        self.__exceptions.append(
            {
                'message': msg,
                'datetime': datetime.now()
            }
        )

    def export(self):
        return {
            'id': self.id_,
            'errors': self.__errors,
            'warnings': self.__warnings,
            'debugs': self.__debugs if self.__get_django_debug_variable else [],
            'exceptions': self.__exceptions if self.__get_django_debug_variable else [],
        }

    @property
    def __get_django_debug_variable(self):
        ret = True
        try:
            from django.conf import settings
            ret = settings.DEBUG.lower() == 'true'
        except:
            ret = True
        finally:
            return ret
