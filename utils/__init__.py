import logging


def Loger(name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)
    return logger


