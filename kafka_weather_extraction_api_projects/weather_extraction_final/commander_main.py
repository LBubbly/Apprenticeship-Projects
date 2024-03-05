# --------------------------------------------------------------------------------
from logging_utilities.logger import log
from for_program.kafka_utilities.kafka_commands_multithread import commander
# --------------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        log.info('Finished Execution of commander_main.py')   
        
        # Start Commander Here...
        print('Hey Commander...')
        commander.start_kafka()
    
    except Exception as e:
        log.error(f'[!!!] CHECK: commander_main.py ERROR: {e}')
    finally:
        log.info('Finished Execution of commander_main.py')