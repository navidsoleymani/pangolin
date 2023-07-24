from datetime import datetime
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from pangolin.models import (
    RequestModel,
    RequestPropertyModel,
    LogModel,
    ResponseModel,
    ResponsePropertyModel,
)


class Log:
    def __init__(self):
        self.__repository: list = list()

        self.__ERROR = 'ERROR'
        self.__WARNING = 'WARNING'
        self.__DEBUG = 'DEBUG'
        self.__EXCEPTION = 'EXCEPTION'
        self.__INFO = 'INFO'

    def error(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': self.__ERROR,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )

    def warning(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': self.__WARNING,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )

    def debug(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': self.__DEBUG,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )

    def exception(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': self.__EXCEPTION,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )

    def info(self, message: str, extra: dict | None = None):
        self.__repository.append(
            {
                'typ': self.__INFO,
                'msg': message,
                'datetime': datetime.now(),
                'extra': extra or dict(),
            }
        )

    def export(self):
        return self.__repository


class Logger:
    __debug: bool | None = None

    def __init__(self):
        self.__request: dict | None = None
        self.log: Log = Log()
        self.__response: dict | None = None

    def set_request(self, value: HttpRequest):
        self.__request = {
            'path': value.path,
            'datetime': datetime.now(),
            'extra': {}
        }

    def set_response(self, value: HttpResponse):
        self.__response = {
            'status_code': value.status_code,
            'datetime': datetime.now(),
            'extra': {},
        }
        self.__add_to_db()

    def __add_to_db(self):
        self.__request_add_to_db()
        self.__logs_add_to_db()
        self.__response_add_to_db()

    __request_obj = None

    def __request_add_to_db(self):
        inst = RequestModel(**self.__request)
        inst.save()
        self.__request_obj = inst

    def __logs_add_to_db(self):
        LogModel.objects.bulk_create(
            [LogModel(request=self.__request_obj, **i) for i in self.log.export()])

    def __response_add_to_db(self):
        inst = ResponseModel(request=self.__request_obj, **self.__response)
        inst.save()

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value: bool):
        self.__debug = value

    @property
    def __django_debug(self):
        ret = None
        try:
            from django.conf import settings
            ret = str(settings.DEBUG).lower() == 'true'
        except:
            pass
        finally:
            return ret

    def __debug_status(self):
        if self.debug is not None:
            return self.debug
        if self.__django_debug is not None:
            return self.__django_debug

        return True
