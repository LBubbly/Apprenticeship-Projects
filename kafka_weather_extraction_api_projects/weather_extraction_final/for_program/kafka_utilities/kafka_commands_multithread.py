import subprocess
from os import system
from threading import Thread
from conf.access_config import property
from logging_utilities.logger import log
# -------------------------------------------------
 

class KafkaCommands:
    def command_activation(self, command):
        try:
            log.info(f'Started Execution of {self.command_activation.__name__}')
            
            # Command Activation Occurs Here...
            subprocess.run(command, shell=True, check=True)
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.command_activation.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.command_activation.__name__}')
        
        
    
    def start_kafka(self):
        try:
            log.info(f'Started Execution of {self.start_kafka.__name__}')
            
            
            start_input = input('Shall we start the Kafka Zookeeper & Broker?\nSELECT [Y|N]: ')
            match start_input.upper():
                case 'Y':
                    print('Starting Up!')
                    
                    # Kafka Commands Listed Here...
                    commands = [property.access_config('start_zookeeper_command'), 
                                property.access_config('start_broker_command')]
                    
                    
                    # Start Kafka Commands Here...
                    threads = []
                    for command in commands:
                        log.info(f'Threading Command: {command}')
                        thread = Thread(target=self.command_activation, args=(command,))
                        thread.start()
                        threads.append(thread)
                        log.info(f'Appended Thread: {thread}')
                        
                        
                    # Joining to main thread, when threads are finished...
                    for thread in threads:
                        thread.join()
                        log.info(f'Joined Thread: {thread}')
                        
                        
                case 'N':
                    system('cls')
                    print('Alright, no worries!')
                    exit(0)
                case default:
                    system('cls')
                    print(f'INVALID INPUT: {start_input}')
                    self.start_kafka()
        
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.start_kafka.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.start_kafka.__name__}')

  
commander = KafkaCommands()