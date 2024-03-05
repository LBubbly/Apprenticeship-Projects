import json
import random
from faker import Faker
from threading import Thread
from kafka import KafkaProducer
from conf.access_config import property
from logging_utilities.logger import log
from .generator import weather_generator   
from for_program.kafka_utilities.offset_operations import offset_operator
# ------------------------------------
 

class WeatherProducer:
    
    
    def __init__(self):
        self.topic = property.access_config('topic_name')
        self.bootstrap_server = property.access_config('server')    


    def produce(self, number, partition_number):
        try:
            # Logging starting execution of produce() 
            log.info(f'Started Execution of {self.produce.__name__}')
            
            
            # Create KafkaProducer object as 'p'
            p = KafkaProducer(
                bootstrap_servers = self.bootstrap_server,
                value_serializer = lambda m: json.dumps(m).encode('ascii') 
            )


            for _ in range(number):
                # 1) User input first
                fake = Faker()
                fake_country = fake.country()
                fake_city = fake.city()
                fake_locations = [fake_city, fake_country]
                log.info(f'FAKES: {fake_locations}')
                
                criteria = random.choice(fake_locations)
                print('CRITERIA -', criteria)
                

                weather_dict = weather_generator.get_data(criteria)
                log.info(f'\nWEATHER DICT - {weather_dict}\
                      \nTYPE - {type(weather_dict)}')

                p.send(f'{self.topic}', value=weather_dict, partition=partition_number) 
                p.flush()
            
            
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.produce.__name__} ERROR: {e}')
            self.produce()
        finally:
            # Logging finished execution of produce() 
            log.info(f'Finished Execution of {self.produce.__name__}')
            
        
    def multithreaded_producing(self):
        
        #partitions_list = [0, 1, 2, 3, 4]
        partitions_list = list(offset_operator.number_of_partitions())
        
        
        number_to_generate = int(input('Enter number of cities and countries to produce: '))
        divided_number = number_to_generate // len(partitions_list)
        modulus = number_to_generate % len(partitions_list)
        print(f'Divided: {divided_number}({type(divided_number)}) & Modulus: {modulus}({type(modulus)})')
        
        
        threads = []
        for partition in partitions_list:
            print('Inside For Loop')
            if partition == partitions_list[-1]:
                additional = divided_number + modulus
                thread = Thread(target=self.produce, args=(additional, partition)) 
            else:
                thread = Thread(target=self.produce, args=(divided_number, partition))
                
            thread.start()
            threads.append(thread)
            log.info('Starting Thread, Partition', partition)
            
        
        for thread in threads:
            thread.join()
        
        print('Producer Threads Joined')


# Created WeatherProducer() object: pro
pro = WeatherProducer()
