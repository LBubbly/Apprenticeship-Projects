import psycopg2
import pandas as pd
from logging_details.logger_class import log
from config.access_properties import property


class PandasProgram:

    def pd_assignment(self):
        try:
            log.info(f'Started Execution: {self.pd_assignment.__name__} (Class: {PandasProgram.__name__})')

            connection = psycopg2.connect(
                host = property.access_pg_sql_file('pg_host_name'), 
                port = property.access_pg_sql_file('pg_port'),
                database = property.access_pg_sql_file('pg_database'),
                user = property.access_pg_sql_file('pg_username'),
                password = property.access_pg_sql_file('pg_password')
            )
            cursor = connection.cursor()
            cursor.execute("SELECT emp_id, first_name || ' ' || last_name AS emp_name, salary, department FROM employee")
            data = cursor.fetchall()
            
            
            emp_df = pd.DataFrame(data)
            emp_df[3].str.replace(' ', '')
            new_column_names = {0 : 'emp_id', 
                                1 : 'emp_name',
                                2 : 'salary',
                                3 : 'dept_name'}
            emp_df = emp_df.rename(columns=new_column_names)
            
            
            csv_df = pd.read_csv(property.access_pg_sql_file('department_csv_file_path'))
            dept_df = pd.DataFrame(csv_df)
            

            two_largest_salaries = emp_df.groupby('dept_name')['salary'].nlargest(2)
            #print(two_largest_salaries)
            second_highest_salaries = two_largest_salaries.groupby('dept_name').min()

            merged_df = pd.merge(emp_df, second_highest_salaries, on='salary')
            print(merged_df)
            
            compare_df = pd.merge(emp_df, two_largest_salaries, on='salary')
            print('\n\n', compare_df.sort_values(by='dept_name'))


            connection.close()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.pd_assignment.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.pd_assignment.__name__}')