import json
from kafka import KafkaProducer
from conf.access_config import property
from logging_utilities.logger import log
from .generator import weather_generator   
# ------------------------------------


class WeatherProducer:
    
    
    def __init__(self):
        self.topic = property.access_config('topic_name')
        self.bootstrap_server = property.access_config('server')    


    def produce(self):
        try:
            # Logging starting execution of produce() 
            log.info(f'Started Execution of {self.produce.__name__}')
            
            # Create KafkaProducer object as 'p'
            p = KafkaProducer(
                bootstrap_servers = self.bootstrap_server,
                value_serializer = lambda m: json.dumps(m).encode('ascii') 
            )


            while True:
                # 1) User input first
                criteria = input('ENTER CITY | COUNTRY | DONE: ')
                print('CRITERIA -', criteria)


                if criteria.upper() == 'DONE':
                    break


                weather_dict = weather_generator.get_data(criteria)
                print('WEATHER DICT -', weather_dict,
                      '\nTYPE -', type(weather_dict))


                p.send(f'{self.topic}', weather_dict) 
            
            
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.produce.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of produce() 
            log.info(f'Finished Execution of {self.produce.__name__}')


# Created WeatherProducer() object: pro
pro = WeatherProducer()