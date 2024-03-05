import json
import psycopg2
from kafka_logging.kafka_logger import kafka_log
from kafka_conf.access_kafka import k_property

class ToPostgres:
    
    def json_to_postgres(self, file_path):
        try:
            kafka_log.info(f'Started Execution: {self.json_to_postgres.__name__} (Class: {ToPostgres.__name__})')
            connection = psycopg2.connect(
                host = f"{k_property.access_kafka_config('pg_host_name')}",
                port = f"{k_property.access_kafka_config('pg_port')}",
                database = f"{k_property.access_kafka_config('pg_database')}",
                user = f"{k_property.access_kafka_config('pg_username')}", 
                password = f"{k_property.access_kafka_config('pg_password')}"
            )
            cursor = connection.cursor()
            
            table_name = f"{k_property.access_kafka_config('emp_table_name')}"
            table_query = f"{k_property.access_kafka_config('create_emp_table_query')}"
            
            
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
            kafka_log.error(f'[!!!] CHECK: {self.json_to_postgres.__name__}, ERROR: {e}')
        finally:
            kafka_log.info(f'Finished Execution: {self.json_to_postgres.__name__}')
    
to_pg = ToPostgres()
# to_pg.json_to_postgres('json_utilities\\json_files\\thread-0.json')