import json
from kafka import KafkaConsumer
from kafka_conf.access_kafka import k_property
from kafka_logging.kafka_logger import kafka_log
# ------------------------------------


class Consumer:

    
    def __init__(self):
        self.topic = k_property.access_kafka_config('topic_name')
        self.bootstrap_server = k_property.access_kafka_config('server')
        self.consumer_group = k_property.access_kafka_config('consumer_group')


    def consume(self):
        try:
            # Logging starting execution of consume() 
            kafka_log.info(f'Started Execution of {self.consume.__name__}')
            
            # Create KafkaConsumer object as 'c'
            c = KafkaConsumer(
                f'{self.topic}',
                bootstrap_servers = f'{self.bootstrap_server}',
                group_id = f'{self.consumer_group}'
            )

            # Prints each consumed message
            for message in c:
                m = json.loads(message.decode('utf-8'))
                
                print(m)
        
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.consume.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of consume() 
            kafka_log.info(f'Finished Execution of {self.consume.__name__}')



# Created Consumer() object: con
con = Consumer()
con.consume()
