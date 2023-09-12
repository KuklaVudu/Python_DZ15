import logging


def log_info(text: str):
    logging.basicConfig(filename='log_treagle.log',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(text)


def log_error(text: str):
    logging.basicConfig(filename='log_treagle.log',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.ERROR)
    logger = logging.getLogger(__name__)
    logger.error(text)