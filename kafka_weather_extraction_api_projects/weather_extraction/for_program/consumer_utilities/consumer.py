import json
from kafka import KafkaConsumer
from .to_postgres import to_pg
from .dict_extraction import dict_maker
from conf.access_config import property
from logging_utilities.logger import log
# ------------------------------------


class Consumer:

    
    def __init__(self):
        self.topic = property.access_config('topic_name')
        self.bootstrap_server = property.access_config('server')
        self.consumer_group = property.access_config('consumer_group')

    
    def consume(self):
        try:
            # Logging starting execution of consume() 
            log.info(f'Started Execution of {self.consume.__name__}')
            
            # Create KafkaConsumer object as 'c'
            c = KafkaConsumer(
                f'{self.topic}',
                bootstrap_servers = f'{self.bootstrap_server}',
                group_id = f'{self.consumer_group}'
            )

            print('Started Consumer')

            # Prints each consumed message
            for message in c:
                print('[MESSAGE] -', message)
                print('[TYPE] -', type(message)) # Is this a KafkaConsumer object!?
                
                print('TOPIC -', message.topic, 
                      '\nPARTITION -', message.partition, 
                      '\nOFFSET -', message.offset, 
                      '\nTIMESTAMP -', message.timestamp)

                message_val = json.loads(message.value.decode('ascii'))
                print('\nVAL_VALUE -', message_val, '\nVAL_TYPE -', type(message_val)) 


                dict_offset, dict_weather, dict_all = dict_maker.complete_extraction(message, message_val)
                print('\n\nDICT_OFFSET -', dict_offset, 
                      '\nDICT_WEATHER -', dict_weather,
                      '\nDICT_ALL -', dict_all)
                
                to_pg.to_postres(dict_offset, dict_weather, dict_all)
                print('Good?')

        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.consume.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of consume() 
            log.info(f'Finished Execution of {self.consume.__name__}')



# Created Consumer() object: con
con = Consumer()

'''
print('\nVALUE -', message.value, '\nTYPE -', type(message.value)) 
message_str = message.value.decode('ascii')
print('\nSTR_VALUE -', message_str, '\nSTR_TYPE -', type(message_str)) 
message_val = json.loads(message.value.decode('ascii'))
print('\nVAL_VALUE -', message_val, '\nVAL_TYPE -', type(message_val)) 
'''