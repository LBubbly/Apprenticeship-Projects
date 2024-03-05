import time
import json
from threading import Thread
from kafka import KafkaProducer
from .generator import generator
from kafka_conf.access_kafka import k_property         
from kafka_logging.kafka_logger import kafka_log
# ------------------------------------

class Producer:
    
    
    def __init__(self):
        self.topic = k_property.access_kafka_config('topic_name')
        self.bootstrap_server = k_property.access_kafka_config('server')    


    def produce(self, number, index):
        try:
            # Logging starting execution of produce() 
            kafka_log.info(f'Started Execution of {self.produce.__name__}')
            
            # Create KafkaProducer object as 'p'
            p = KafkaProducer(bootstrap_servers=self.bootstrap_server)

            for_json_file = []
            for _ in range(number):
                # 1) Generate by 'number' arg 
                employee_dict = generator.generate()
                # 2) Append JSON to for_json_file list
                for_json_file.append(employee_dict)
                # 3) Transform dict into JSON 
                employee_json = json.dumps(employee_dict)
                # 4) Send JSON to Kafka Consumer
                p.send(f'{self.topic}', employee_json.encode('utf-8'))
                # 5) Print to check...
                print(employee_dict)
            
            with open(f"json_utilities\\json_files\\thread-{index}.json", "w") as file:
                json.dump(for_json_file, file, indent=4)
            
            # Waits
            time.sleep(20)
            
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.produce.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of produce() 
            kafka_log.info(f'Finished Execution of {self.produce.__name__}')



    def producing_threads(self, number_of_threads, number_of_objects):        
        try:
            # Logging starting execution of producing_threads()
            kafka_log.info(f'Started Execution of {self.producing_threads.__name__}')
            
            
            # Create specified number_of_threads and appending each to the threads list
            threads = []   
            for i in range(number_of_threads):
                thread = Thread(target=self.produce, args=(number_of_objects, i))
                thread.start()
                threads.append(thread)
                print('Starting', i, thread)
            
            
            # Join each thread in the threads list
            count = 0
            for thread in threads:
                thread.join()
                print('Joining', count, thread)
                count += 1
        
        
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.producing_threads.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of producing_threads() 
            kafka_log.info(f'Finished Execution of {self.producing_threads.__name__}')    



# Created Producer() object: pro
pro = Producer()


# total_num_objects = 10 # user input...
# total_num_threads = 3 # user input...
# total_num_divided = total_num_objects // total_num_threads
# pro.producing_threads(total_num_threads, total_num_divided)
