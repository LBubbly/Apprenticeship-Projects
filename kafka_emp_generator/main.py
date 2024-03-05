from os import system
from producer import pro
from consumer import con
from kafka_logging.kafka_logger import kafka_log

class KafkaProgram:
    
    def kafka_program(self):
        try:
            # Logging starting execution of kafka_program() 
            kafka_log.info(f'Started Execution of {self.kafka_program.__name__}')
        
            # Captures user inputs for total number of objects and producer threads 
            print('***************************',
                '*      KAFKA PROJECT      *',
                '***************************\n',
                sep='\n')
            total_num_objects = int(input('Enter number of objects: '))
            total_producer_threads = int(input('Enter number of producer threads: '))
            
            # Determines total whole number of objects per thread
            objects_divided_by_thread = total_num_objects // total_producer_threads 
            
            # Producing & Consuming Objects
            pro.producing_threads(total_producer_threads, objects_divided_by_thread)
            con.consume()
            
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.kafka_program.__name__} ERROR: {e}')
            
            # Restart program
            system('cls')
            print('Please try again...')
            self.kafka_program()
            
        finally:
            # Logging finished execution of kafka_program() 
            kafka_log.info(f'Finished Execution of {self.kafka_program.__name__}')


# Calling Program
if __name__ == '__main__':
    program = KafkaProgram()
    program.kafka_program()