from django.utils.deprecation import MiddlewareMixin

from pangolin.repo.tools.loggers import logger


class LoggerInstanceMiddleware(MiddlewareMixin):

    def process_request(self, request):
        logger('set')
