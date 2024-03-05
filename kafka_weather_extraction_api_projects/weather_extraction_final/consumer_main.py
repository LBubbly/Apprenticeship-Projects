# --------------------------------------------------------------------------------
from logging_utilities.logger import log
from for_program.consumer_utilities.consumer import con
# --------------------------------------------------------------------------------


if __name__ == '__main__':
    try:
        log.info(f'Started Execution of consumer_main.py')   
        
        # Starting Consumer Here...
        print('Hi Consumer...')
        con.multiprocess_consuming()
    
    except Exception as e:
        log.error(f'[!!!] CHECK: consumer_main.py ERROR: {e}')
    finally:
        log.info('Finished Execution of consumer_main.py')