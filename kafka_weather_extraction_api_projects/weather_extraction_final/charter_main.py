from logging_utilities.logger import log
from for_program.chart_utilities.chart_consumer import charter


if __name__ == '__main__':
    try:
        log.info(f'Started Execution of consumer_main.py')   
        
        charter.multiprocess_consuming()
    
    except Exception as e:
        log.error(f'[!!!] CHECK: consumer_main.py ERROR: {e}')
    finally:
        log.info('Finished Execution of consumer_main.py')