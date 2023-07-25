from .__request import Request as RequestModel
from .__request_property import RequestProperty as RequestPropertyModel
from .__log import Log as LogModel
from .__response import Response as ResponseModel
from .__response_property import ResponseProperty as ResponsePropertyModel

__model_list = [RequestModel, RequestPropertyModel, LogModel, ResponseModel, ResponsePropertyModel]
__model_name_list = [c.__class__.__name__ for c in __model_list]


class LoggerDBRouter(object):

    def db_for_read(self, model, **hints):
        if model in [RequestModel, RequestPropertyModel, LogModel, ResponseModel, ResponsePropertyModel]:
            return 'logger_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model in [RequestModel, RequestPropertyModel, LogModel, ResponseModel, ResponsePropertyModel]:
            return 'logger_db'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name in __model_name_list:
            return ('logger_db' == db)
        return ('default' == db)
