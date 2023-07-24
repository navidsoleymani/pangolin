from django.utils.deprecation import MiddlewareMixin

from pangolin.repo.tools import logger


class LoggerInstanceMiddleware(MiddlewareMixin):

    def process_request(self, request):
        logger('set')
