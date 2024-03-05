from jproperties import Properties
from kafka_logging.kafka_logger import kafka_log


class AccessKafka:
    def access_kafka_config(self, property_to_access):
        try:
            kafka_log.info(f'Started Execution: {self.access_kafka_config.__name__} (Class: {AccessKafka.__name__}, Property Accessed: {property_to_access})')
            
            config = Properties()
            with open('wk4_kafka_project\kafka_conf\kafka_config.properties', 'rb') as config_file:  
                config.load(config_file)
                
            prop = config[f'{property_to_access}'].data
            return prop
        except Exception as e:
            kafka_log.error(f'[!!!] CHECK: {self.access_kafka_config.__name__}, Error: {e}')
        finally:
            kafka_log.info(f'Finished Execution: {self.access_kafka_config.__name__}')
            
k_property = AccessKafka()
