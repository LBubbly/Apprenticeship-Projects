import json
from kafka import KafkaConsumer
from .to_postgres import to_pg
from multiprocessing import Process
from .dict_extraction import dict_maker 
from conf.access_config import property
from logging_utilities.logger import log
from for_program.kafka_utilities.offset_operations import offset_operator
# ------------------------------------


class Consumer:
        
        
    def consume(self, number):
        try:
            # Logging starting execution of consume() 
            log.timestamp(f'Started Execution of {self.consume.__name__}')
            print(f'Started Consumer {number}...')

            consumption_count = 0
            
            consumer = KafkaConsumer(
                property.access_config('topic_name'),
                bootstrap_servers = property.access_config('server'),
                group_id = property.access_config('consumer_group'),
                enable_auto_commit = False
            )
            
            while True:
                message_batch = consumer.poll(timeout_ms=5000)
                log.info(f'[MSG BATCH]: {message_batch}, {type(message_batch)}')    
                
                
                for partition, messages in message_batch.items():
                    log.info(f'[TOPIC PARTITION] - {partition}, {type(partition)}')
                    log.info(f'[MESSAGE INFO "messages"] - {messages}, {type(messages)}')
                    
                    
                    for message in messages:                    
                        message_val = json.loads(message.value.decode('ascii'))
                        log.info(f'MESSAGE VALUE: {message_val}')
                    
                        
                        if message_val == {}:
                            log.info(f'[BAD MESSAGE] - {message}')
                            print('Next Please...')
                            continue
                        
                        
                        consumer.commit()
                        log.info(f'\n[MESSAGE] - {message}\
                                \n[TYPE] - {type(message)}\
                                \n[TOPIC] - {message.topic}\
                                \n[KEY] - {message.key}\
                                \n[PARTITION] - {message.partition}\
                                \n[OFFSET] - {message.offset}\
                                \n[TIMESTAMP] - {message.timestamp}\
                                \nVAL_VALUE - {message_val}\
                                \nVAL_TYPE - {type(message_val)}') 
                        
                        
                        dict_offset, dict_weather = dict_maker.complete_extraction(message, message_val)
                        to_pg.to_postres(dict_offset, dict_weather)
                        
                        
                        city_name = message_val['location']['name']
                        country_name = message_val['location']['country']
                        print(f'Consumer {number} consumed {city_name.title()}, {country_name.title()}')
                        
                        
                        consumption_count += 1
                        
        except KeyboardInterrupt:
            log.info(f'KeyboardInterrupt Exception Occurred...')
            print(f'[CONSUMER {number} CONSUMPTION COUNT] - {consumption_count}')
            pass                
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.consume.__name__} ERROR: {e}')
            self.consume(number)
        finally:
            # Logging finished execution of consume() 
            log.info(f'Finished Execution of {self.consume.__name__}')



    def multiprocess_consuming(self):
        
        try:
            # Logging starting execution of multiprocess_consuming() 
            log.timestamp(f'Started Execution of {self.multiprocess_consuming.__name__}')
            
            partitions_set = offset_operator.number_of_partitions()
                        
            processes = []
            for i in partitions_set:
                log.timestamp(f'Processing Consumer {i}')
                process = Process(target=self.consume, args=(i,))
                process.start()
                processes.append(process)
                log.timestamp(f'Consumer Process {i} Running...')

            count = 0
            for process in processes:
                process.join()
                log.timestamp(f'Consumer Process {count} Joined.')
                count += 1
                
                
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.multiprocess_consuming.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of multiprocess_consuming() 
            log.info(f'Finished Execution of {self.multiprocess_consuming.__name__}')
        
# Created Consumer() object: con
con = Consumer()