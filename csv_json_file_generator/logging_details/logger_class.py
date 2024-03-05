import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)


    def debug(self, message):
        try:
            self.logger.debug(message)
        except:
            pass

    def info(self, message):
        try:
            self.logger.info(message)
        except:
            pass

    def warning(self, message):
        try:
            self.logger.warning(message)
        except:
            pass

    def error(self, message):
        try:
            self.logger.error(message)
        except:
            pass

    def critical(self, message):
        try:
            self.logger.critical(message)
        except:
            pass


my_logger = Logger('logs.log')
my_logger.info('YAYYY I work')