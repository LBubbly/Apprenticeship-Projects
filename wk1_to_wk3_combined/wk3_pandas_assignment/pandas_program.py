import psycopg2
import pandas as pd
from logging_details.logger_class import log
from config.access_properties import property
from sqlalchemy import create_engine

'''
log.info(f'Started Execution: {self.generate_depts_to_json.__name__} (Class: {JSONOperations_Gen.__name__})')
log.error(f'[!!!] CHECK: {self.generate_depts_to_json.__name__}, ERROR: {e}')
log.info('Successful Generation to Department JSON File!')
log.info(f'Finished Execution: {self.generate_depts_to_json.__name__}')
'''



class PandasProgram:
    def pd_assignment(self):
        try:
            log.info(f'Started Execution: {self.pd_assignment.__name__} (Class: {PandasProgram.__name__})')

            #engine = create_engine()

            connection = psycopg2.connect(
                host = property.access_pg_sql_file('pg_host_name'), 
                port = property.access_pg_sql_file('pg_port'),
                database = property.access_pg_sql_file('pg_database'),
                user = property.access_pg_sql_file('pg_username'),
                password = property.access_pg_sql_file('pg_password')
            )
            cursor = connection.cursor()
            
            sql = "SELECT emp_id, first_name || ' ' || last_name AS emp_name, salary, department FROM employee" 
            employees_df = pd.read_sql_query(sql, connection)
            departments_df = pd.read_csv(property.access_pg_sql_file('department_csv_file_path'))
            
            
            joined_df = pd.merge(departments_df, employees_df, on='department', how='inner')
            
            print(joined_df)
            connection.close()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.pd_assignment.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.pd_assignment.__name__}')
