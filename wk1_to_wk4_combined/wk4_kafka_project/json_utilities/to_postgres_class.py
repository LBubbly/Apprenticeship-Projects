import csv
import json
import psycopg2
from logging_details.logger_class import log
from config.access_properties import property


class ToPostgres:
    
    def csv_to_postgres(self, type_of_data):
        try:
            log.info(f'Started Execution: {self.csv_to_postgres.__name__} (Class: {ToPostgres.__name__})')

            # print(f'in csv_to_postgres -> {type_of_data}')
            connection = psycopg2.connect(
                host = property.access_pg_sql_file('pg_host_name'),
                port = property.access_pg_sql_file('pg_port'),
                database = property.access_pg_sql_file('pg_database'),
                user = property.access_pg_sql_file('pg_username'), 
                password = property.access_pg_sql_file('pg_password')
            )
            cursor = connection.cursor()


            match type_of_data:
                case 'employee':
                    file_path = f"{property.access_pg_sql_file('employee_csv_file_path')}"
                    table_name = f"{property.access_pg_sql_file('emp_table_name')}"
                    table_query = f"{property.access_pg_sql_file('create_emp_table_query')}"
                case 'department':
                    file_path = f"{property.access_pg_sql_file('department_csv_file_path')}"
                    table_name = f"{property.access_pg_sql_file('dept_table_name')}"
                    table_query = f"{property.access_pg_sql_file('create_dept_table_query')}"
            # print(f'PATH: .\{file_path}\nT_NAME: {table_name}\nT_QUERY: {table_query}')                    


            with open(f'.\{file_path}', 'r') as file:
                
                reader = csv.reader(file)
                header = next(reader)
                
                cursor.execute(table_query)
                connection.commit()
                                
                insert_query = f"INSERT INTO {table_name}({','.join(header)}) VALUES ({','.join(['%s']*len(header))})"
                
                for row in reader:
                    cursor.execute(insert_query, row)
                
                connection.commit()
            
            cursor.close()
            connection.close()
            print('Successfully Loaded the CSV!')
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.csv_to_postgres.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.csv_to_postgres.__name__}')
        
    
    
    def json_to_postgres(self, type_of_data):
        try:
            log.info(f'Started Execution: {self.json_to_postgres.__name__} (Class: {ToPostgres.__name__})')
            connection = psycopg2.connect(
                host = f"{property.access_pg_sql_file('pg_host_name')}",
                port = f"{property.access_pg_sql_file('pg_port')}",
                database = f"{property.access_pg_sql_file('pg_database')}",
                user = f"{property.access_pg_sql_file('pg_username')}", 
                password = f"{property.access_pg_sql_file('pg_password')}"
            )
            cursor = connection.cursor()
            
            
            match type_of_data:
                case 'employee':
                    file_path = f"{property.access_pg_sql_file('employee_json_file_path')}"
                    table_name = f"{property.access_pg_sql_file('emp_table_name')}"
                    table_query = f"{property.access_pg_sql_file('create_emp_table_query')}"
                case 'department':
                    file_path = f"{property.access_pg_sql_file('department_json_file_path')}"
                    table_name = f"{property.access_pg_sql_file('dept_table_name')}"
                    table_query = f"{property.access_pg_sql_file('create_dept_table_query')}"
            # print(f'PATH: {file_path}\nT_NAME: {table_name}\nT_QUERY: {table_query}')
            
            
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                keys = list(json_data[0].keys())
                cursor.execute(table_query)
                connection.commit()
                
                for obj in json_data:
                    values = [obj[key] for key in keys]
                    insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(values))})"
                    cursor.execute(insert_query, values)

                connection.commit()            


            cursor.close()            
            connection.close()
            print('Successfully Loaded the JSON!')
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.json_to_postgres.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.json_to_postgres.__name__}')
    
