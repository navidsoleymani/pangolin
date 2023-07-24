from datetime import datetime
import secrets


class Logger:
    def __init__(self):
        self.id_ = secrets.token_hex()
        self.__errors: list = list()
        self.__warnings: list = list()
        self.__debugs: list = list()

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

    def export(self):
        return {
            'errors': self.__errors,
            'warnings': self.__warnings,
            'debugs': self.__debugs,
        }
