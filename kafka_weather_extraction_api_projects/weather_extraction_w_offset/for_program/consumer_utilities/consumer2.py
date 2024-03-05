import json
from kafka import KafkaConsumer
from .to_postgres import to_pg
from .dict_extraction import dict_maker
from conf.access_config import property
from logging_utilities.logger import log
# ------------------------------------


class Consumer:

    
    def __init__(self): 
        self.c = KafkaConsumer(
            property.access_config('topic_name'),
            bootstrap_servers = property.access_config('server'),
            group_id = property.access_config('consumer_group')    
        )
        

    def consume(self):
        try:
            # Logging starting execution of consume() 
            log.info(f'Started Execution of {self.consume.__name__}')
            print('Started Consumer')

            # Prints each consumed message
            for message in self.c:
                print('[MESSAGE] -', message)
                print('[TYPE] -', type(message)) # Is this a KafkaConsumer object!?
                
                print('TOPIC -', message.topic, 
                      '\nPARTITION -', message.partition, 
                      '\nOFFSET -', message.offset, 
                      '\nTIMESTAMP -', message.timestamp,
                      '\nKEY -', message.key)

                message_val = json.loads(message.value.decode('ascii'))
                print('\nVAL_VALUE -', message_val, '\nVAL_TYPE -', type(message_val)) 
                
                
                dict_offset, dict_weather, dict_all = dict_maker.complete_extraction(message, message_val)
                to_pg.to_postres(dict_offset, dict_weather, dict_all)
                
                
                print('Thank you, next...')

        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.consume.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of consume() 
            log.info(f'Finished Execution of {self.consume.__name__}')



# Created Consumer() object: con
con2 = Consumer()