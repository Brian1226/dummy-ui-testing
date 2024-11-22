import logging
import os


class Logger:
    def logger(self, logger_level=logging.WARNING):
        logs_directory = os.path.join(os.getcwd(), 'logs')
        logger = logging.getLogger(__name__)
        logger.setLevel(logger_level)

        if logger.hasHandlers():
            logger.handlers.clear()
        
        fh = logging.FileHandler(os.path.join(logs_directory, 'logs.log'))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
