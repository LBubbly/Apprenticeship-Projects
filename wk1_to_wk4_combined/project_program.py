from os import system
from logging_details.logger_class import log
from config.access_properties import property
from wk1_generator.generator_program import GeneratorProgram
from wk2_etl_functionality.etl_program import ETLProgram
from wk3_pandas_assignment.panda_program import PandasProgram
from wk4_kafka_project.kafka_program import KafkaProgram

class ProjectProgram:
    
    def wk1_data_generator(self):
        try:
            log.info(f'Started Execution: {self.wk1_data_generator.__name__} (Class: {ProjectProgram.__name__})')

            gen = GeneratorProgram()
            employee_or_department = gen.emp_or_dept_display()
            system('cls')
            csv_or_json = gen.csv_or_json_display()
            system('cls')
            gen.generator_selector(csv_or_json, employee_or_department)
            
            
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.wk1_data_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.wk1_data_generator.__name__}')
        
        
    
    def wk2_load_to_postgres(self):
        try:
            log.info(f'Started Execution: {self.wk2_load_to_postgres.__name__} (Class: {ProjectProgram.__name__})')
            etl = ETLProgram()
            file = etl.etl_csv_or_json_display()
            system('cls')
            data = etl.etl_emp_or_dept_display()
            system('cls')
            etl.etl_selector(file, data)
            
            
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.wk2_load_to_postgres.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.wk2_load_to_postgres.__name__}')
        
        
    def wk3_pandas_assignment(self):
        try:
            log.info(f'Started Execution: {self.wk3_pandas_assignment.__name__} (Class: {ProjectProgram.__name__})')
            p = PandasProgram()
            p.pd_assignment()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.wk3_pandas_assignment.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.wk3_pandas_assignment.__name__}')
    
    
    ''' DON'T FORGET TO CONNECT TO PROJECT SELECTION '''
    def wk4_kafka_project(self):
        try:
            log.info(f'Started Execution: {self.wk4_kafka_project.__name__} (Class: {ProjectProgram.__name__})')
            kp = KafkaProgram()
            # kp.program_method
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.wk4_kafka_project.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.wk4_kafka_project.__name__}')
    
    
    
    def project_selection(self):
        try:
            log.info(f'Started Execution: {self.project_selection.__name__} (Class: {ProjectProgram.__name__})')
            
            selected_project = input(f"{property.access_displays('weekly_projects_display')} ")
            match selected_project:
                case '1':
                    system('cls')
                    self.wk1_data_generator()
                    self.project_selection()
                case '2':
                    system('cls')
                    self.wk2_load_to_postgres()
                    self.project_selection()
                case '3':
                    system('cls')
                    self.wk3_pandas_assignment()
                    self.project_selection()
                case '4':
                    #system('cls')
                    print('Exited Program.')
                    exit(0)
                case default:
                    system('cls')
                    print(f'INVALID INPUT! {selected_project}')
                    log.info(f'INVALID INPUT! {selected_project}')
                    self.project_selection()
                
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.project_selection.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.project_selection.__name__}')



if __name__ =='__main__':
    program = ProjectProgram()
    program.project_selection()