import logging

class KafkaLogger:
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
        except Exception as e:
            self.error(f'[!!!] CHECK {self.debug.__name__}, ERROR: {e}')
        finally:
            self.info(f'Finished Execution: {self.debug.__name__}')


    def info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            self.error(f'[!!!] CHECK {self.info.__name__}, ERROR: {e}')
        finally:
            pass # INFINITE LOOP: self.info(f'Finished Execution: {self.info.__name__}')


    def warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            self.error(f'[!!!] CHECK {self.warning.__name__}, ERROR: {e}')
        finally:
            self.info(f'Finished Execution: {self.warning.__name__}')


    def error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            self.error(f'[!!!] CHECK {self.error.__name__}, ERROR: {e}')
        finally:
            self.info(f'Finished Execution: {self.error.__name__}')


    def critical(self, message):
        try:
            self.logger.critical(message)
        except Exception as e:
            self.error(f'[!!!] CHECK {self.critical.__name__}, ERROR: {e}')
        finally:
            self.info(f'Finished Execution: {self.critical.__name__}')


kafka_log = KafkaLogger('wk4_kafka_project\kafka_logging\kafka_logs.log')