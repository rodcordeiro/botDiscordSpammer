import logging
def Logger(name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)
    return logger

