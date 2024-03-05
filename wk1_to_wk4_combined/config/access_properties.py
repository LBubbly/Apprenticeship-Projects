from jproperties import Properties
from logging_details.logger_class import log


class AccessProperties():
    
    
    def access_displays(self, property_to_access):
        try:
            log.info(f'Started Execution: {self.access_displays.__name__} (Class: {AccessProperties.__name__}, Property Accessed: {property_to_access})')
            
            config = Properties()
            with open('config\displays.properties', 'rb') as config_file:  
                config.load(config_file)
                
            display = config[f'{property_to_access}'].data
            return display
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.access_displays.__name__} \nError: {e}')
        finally:
            log.info(f'Finished Execution: {self.access_displays.__name__}')
    
    
    def access_pg_sql_file(self, property_to_access):
        try:
            log.info(f'Started Execution: {self.access_pg_sql_file.__name__} (Class: {AccessProperties.__name__}, Property Accessed: {property_to_access})')
            
            config = Properties()
            with open('config\pg_sql_file.properties', 'rb') as config_file:  
                config.load(config_file)
                
            prop = config[f'{property_to_access}'].data
            return prop
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.access_pg_sql_file.__name__}, Error: {e}')
        finally:
            log.info(f'Finished Execution: {self.access_pg_sql_file.__name__}')
    
    
    def access_kafka_config(self, property_to_access):
        try:
            log.info(f'Started Execution: {self.access_kafka_config.__name__} (Class: {AccessProperties.__name__}, Property Accessed: {property_to_access})')
            
            config = Properties()
            with open('config\kafka_config.properties', 'rb') as config_file:  
                config.load(config_file)
                
            prop = config[f'{property_to_access}'].data
            return prop
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.access_kafka_config.__name__}, Error: {e}')
        finally:
            log.info(f'Finished Execution: {self.access_kafka_config.__name__}')
    
    
property = AccessProperties()

'''
TEST ------------------------------------------------
test = AccessProperties()
t = test.access_pg_sql_file('pg_host_name')
t2 = test.access_pg_sql_file('pg_port')
t3 = test.access_pg_sql_file('pg_database')
t4 = test.access_pg_sql_file('pg_username')
t5 = test.access_pg_sql_file('pg_password')
t6 = test.access_pg_sql_file('emp_table_name')
t7 = test.access_pg_sql_file('create_emp_table_query')
t6 = test.access_pg_sql_file('dept_table_name')
t8 = test.access_pg_sql_file('create_dept_table_query')
t9 = test.access_pg_sql_file('emp_column_names')
t10 = test.access_pg_sql_file('dept_column_names')
t11 = test.access_pg_sql_file('employee_csv_file_path')
t12 = test.access_pg_sql_file('department_csv_file_path')
t13 = test.access_pg_sql_file('employee_json_file_path')
t14 = test.access_pg_sql_file('department_json_file_path')
print(t)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
print(t10)
print(t11)
print(t12)
print(t13)
print(t14)'''