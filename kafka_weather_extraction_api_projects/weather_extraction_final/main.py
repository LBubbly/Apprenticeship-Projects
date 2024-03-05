# --------------------------------------------------------------------------------
from os import system
from logging_utilities.logger import log
from for_program.producer_utilities.producer import pro
from for_program.chart_utilities.chart_consumer import charter
from for_program.kafka_utilities.offset_operations import offset_operator
# --------------------------------------------------------------------------------

class Program:
    
    def back(self):
        user_input = input('Ready to go back?\n[Y]: ')
        
        if user_input.upper() != 'Y':
            print(F'INVALID INPUT: {user_input}')
            self.back()
            
            
    ###
    def read_messages(self):
        try:
            log.info(f'Started Execution of {self.read_messages.__name__}')
        
        
            print('*********************************',
                '*      SELECT AN OPERATION      *',
                '*********************************',
                '1) NUMBER OF PARTITIONS', 
                '2) READ RANGE OF OFFSETS', 
                '3) READ MAX OFFSET MESSAGE', 
                '4) BACK TO MAIN',
                '',
                sep='\n')
            selected_action = input('SELECT [1|2|3|4]: ')
            
            match selected_action:
                case '1':
                    system('cls')
                    offset_operator.number_of_partitions()
                    self.back()
                    system('cls')
                    self.read_messages()
                case '2':
                    offset_operator.define_range()
                    self.back()
                    system('cls')
                    self.read_messages()
                case '3':
                    offset_operator.retrieve_max_offset()
                    self.back()
                    system('cls')
                    self.read_messages()
                case '4':
                    pass # KEEP AS PASS, TO RETURN TO MAIN...
                case default:
                    system('cls')
                    print(f'INVALID INPUT: {selected_action}')
                    self.read_messages()
            
            
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.read_messages.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.read_messages.__name__}')
    
    
    ###
    def view_charts(self):
        try:
            log.info(f'Started Execution of {self.view_charts.__name__}')
        
        
            print('*****************************',
                '*      SELECT A CHART:      *',
                '*****************************',
                '1) PIE CHART', 
                '2) BAR CHART', 
                '3) BACK TO MAIN',
                '',
                sep='\n')
            selected_action = input('SELECT [1|2|3]: ')
            
            match selected_action:
                case '1':
                    charter.pie_chart()
                    self.back()
                    
                    system('cls')
                    self.view_charts()
                case '2':
                    charter.bar_chart()
                    self.back()
                    
                    system('cls')
                    self.view_charts()
                case '3':
                    pass # KEEP AS PASS, TO RETURN TO MAIN...
                case default:
                    system('cls')
                    print(f'INVALID INPUT: {selected_action}')
                    self.view_charts()
            
            
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.view_charts.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.view_charts.__name__}')
    
    ###
    def start(self):
        try:
            log.info(f'Started Execution of {self.start.__name__}')
            
            
            print('*******************************',
                '*      SELECT AN ACTION:      *',
                '*******************************',
                '1) PRODUCE', 
                '2) READ MESSAGES', 
                '3) VIEW CHARTS',
                '4) EXIT PROGRAM',
                sep='\n')
            selected_action = input('SELECT [1|2|3|4]: ')
            
            match selected_action:
                case '1':
                    system('cls')
                    pro.multithreaded_producing()
                    self.back()
                    
                    system('cls')
                    print('WELCOME BACK!!!')
                    self.start()
                case '2':
                    system('cls')
                    self.read_messages()
                    
                    system('cls')
                    print('WELCOME BACK!!!')
                    self.start()
                case '3':
                    system('cls')
                    self.view_charts()
                    
                    system('cls')
                    print('WELCOME BACK!!!')
                    self.start()
                case '4':
                    system('cls')
                    print('All Done!')
                    exit(0)
                case default:
                    system('cls')
                    print(f'INVALID INPUT: {selected_action}')
                    self.start()
        
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.start.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.start.__name__}')



# --------------------------------------------------------------------------
if __name__ == '__main__':       
    try:
        log.info('Started Execution of main.py')   
        
        # Starting Program Here...
        program = Program()
        program.start()
        
    except Exception as e:
        log.error(f'[!!!] CHECK: main.py ERROR: {e}')
    finally:
        log.info('Finished Execution of main.py')