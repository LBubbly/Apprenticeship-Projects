import psycopg2
from conf.access_config import property
from logging_utilities.logger import log

class ToPostgres:

    def connection(self):
        try: 
            # Logging starting execution of connection() 
            log.info(f'Started Execution of {self.connection.__name__}')

            return psycopg2.connect(
                host = property.access_config('pg_host_name'),
                port = property.access_config('pg_port'),
                database = property.access_config('pg_database'),
                user = property.access_config('pg_username'),
                password = property.access_config('pg_password') 
            )
        
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.connection.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of connection() 
            log.info(f'Finished Execution of {self.connection.__name__}')



    def to_postres(self, dict_offset, dict_weather):
        try: 
            # Logging starting execution of connection() 
            log.info(f'Started Execution of {self.connection.__name__}')

            conn = self.connection()
            cur = conn.cursor()


            offset_table = property.access_config('offset_table_name')
            weather_table = property.access_config('weather_table_name')
            table_name = [offset_table, weather_table]
            dict_list = [dict_offset, dict_weather]
        

            for d in dict_list:
                columns = ', '.join(d.keys())
                values = ', '.join(['%s'] * len(d))
                query = f"INSERT INTO {table_name[0]} ({columns}) VALUES ({values})"
                
                table_name.pop(0)
                cur.execute(query, tuple(d.values()))
                conn.commit() 


            cur.close()
            conn.close()
            print('Success To Postgres!!!')
            
            
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.connection.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of connection() 
            log.info(f'Finished Execution of {self.connection.__name__}')


to_pg = ToPostgres()