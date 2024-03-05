# --------------------------------------------------------------------------
import psycopg2
import pandas as pd
from os import system
from conf.access_config import property
from logging_utilities.logger import log
from kafka import KafkaConsumer, TopicPartition 
# --------------------------------------------------------------------------



class OffsetOperations:
    def __init__(self):
        self.topic = property.access_config('topic_name')
        self.consumer = KafkaConsumer( # This consumer is from a separate consumer group...
            self.topic,
            bootstrap_servers = property.access_config('server'), 
            group_id = property.access_config('message_consumer_group')
        )


    #--------------------------------------------------------------------------------------------------
    # Determined the number of partitions in Weather_API topic directly from Kafka 
    def number_of_partitions(self):
        try:
            log.info(f'Started Execution of {self.number_of_partitions.__name__}')   
        
            # Retrieving Partitions Set Here...
            partitions = self.consumer.partitions_for_topic(self.topic)
            print(f"Partitions for {property.access_config('topic_name')}: {partitions}")
            return partitions
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.number_of_partitions.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.number_of_partitions.__name__}')
    
    
    
    #--------------------------------------------------------------------------------------------------
    # Connection to our pg db
    def connection(self):
        try: 
            log.info(f'Started Execution of {self.connection.__name__}')

            # Returning connection here...
            return psycopg2.connect(
                host = property.access_config('pg_host_name'),
                port = property.access_config('pg_port'),
                database = property.access_config('pg_database'),
                user = property.access_config('pg_username'),
                password = property.access_config('pg_password') 
            )
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.connection.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.connection.__name__}')
            
            
            
    ###--------------------------------------------------------------------------------------------------
    # Display total offsets of each partition
    def get_total_offsets(self):
        try: 
            log.info(f'Started Execution of {self.get_total_offsets.__name__}')
            
            ###
            with self.connection() as conn:
                system('cls')
                partitions = self.number_of_partitions()
                
                for partition in partitions:
                    result = pd.read_sql(f'SELECT\n    MIN(offset_value) AS min_offset,\n    MAX(offset_value) AS max_offset\nFROM offset_table\nWHERE partition_number = {partition};', conn)
    
                    min_offset = result['min_offset'][0]
                    max_offset = result['max_offset'][0]
                    print(f'Partition {partition}: {min_offset}-{max_offset} Offsets')
        
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.get_total_offsets.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.get_total_offsets.__name__}')
            
    
    
    #--------------------------------------------------------------------------------------------------
    # Retrieve specified offset from pg db
    def get_offset(self, partition_number, offset_number):
        try: 
            log.info(f'Started Execution of {self.get_offset.__name__}')
            
            ###
            with self.connection() as conn:        
                cur = conn.cursor()
                cur.execute(f'SELECT * FROM weather_table wt\nJOIN offset_table ot\nON wt.timestamp_number = ot.timestamp_number\nWHERE partition_number = {partition_number}\nAND offset_value = {offset_number};', conn)
                data = cur.fetchall()
                conn.commit()
                df = pd.DataFrame(data)
                print(df)
                return(df)
            
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.get_offset.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.get_offset.__name__}')
    
        
    
    #--------------------------------------------------------------------------------------------------
    # To return messages from a user-determined range from pg db
    def define_range(self):
        try: 
            log.info(f'Started Execution of {self.define_range.__name__}')
            
            ###
            self.get_total_offsets() # Prints Partitions & Min-Max Range of Offsets
            partition_number = int(input('Select Partition #: '))
            offset_min = int(input('Enter Minimum Offset #: ')) 
            offset_max = int(input('Enter Maximum Offset #: ')) 

            print('SELECTED:',
                f'Partition: {partition_number}',
                f'Range: {offset_min}-{offset_max}',
                sep='\n')

            dfs = []
            for offset in range(offset_min, offset_max):
                df = self.get_offset(partition_number, offset)
                dfs.append(df)
            
            combined_df = pd.concat(dfs)
            combined_df.to_csv('for_program\kafka_utilities\data\df.csv')
            
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.define_range.__name__} ERROR: {e}')
            self.define_range()
        finally:
            log.info(f'Finished Execution of {self.define_range.__name__}')
            
        
    '''    
    #--------------------------------------------------------------------------------------------------
    # Returns the latest/max offset from Kafka 
    def retrieve_max_offset(self):
        try:
            log.info(f'Started Execution of {self.retrieve_max_offset.__name__}')   
            system('cls')
        
        
            # Displays partitions we are available to... 
            partitions = self.consumer.partitions_for_topic(self.topic)
            partitions_list = list(partitions)
            selected_partition = int(input(f'SELECT A PARTITION [{partitions_list[0]}-{partitions_list[-1]}]: '))
            
            if selected_partition not in partitions_list:
                print('INVALID INPUT:', selected_partition)
                self.retrieve_max_offset()
                
                
            # Connecting /w pg
            with self.connection() as conn:
                # Run query to retrieve max offset in pg
                result = pd.read_sql(f'SELECT MAX(offset_value) AS max_offset\nFROM offset_table\nWHERE partition_number = {selected_partition};', conn)
                max_offset = result['max_offset'][0] # TYPE: numpy.int64
                log.info(f'PG MAX OFFSET: {max_offset}\nTYPE: {type(max_offset)}')
                
                
                # Use max offset & increment by 1
                incre_offset = int(max_offset)+1    
                log.info(f'Incre_OFFSET: {incre_offset}\nTYPE: {type(incre_offset)}')    
            
                
                # Use .end_offsets()
                topic_partition = TopicPartition(self.topic, selected_partition)
                end_offsets = self.consumer.end_offsets([topic_partition]) # The offset of the last available message + 1
                end_offset = end_offsets[topic_partition]
                log.info(f'MAX OFFSET: {end_offset}')
                print(f'MAX OFFSET: {end_offset}')
        
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.retrieve_max_offset.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.retrieve_max_offset.__name__}')
    '''
    
     
offset_operator = OffsetOperations()

'''
            # column_names = ['City', 'Country', 'Lat', 'Lon', 'Localtime_Epoch', 'Temp_C', 'Temp_F', 'Wind_MPH', 'Wind_KPH', 'Vis_km', 'Vis_Miles', 'W_Condition', 'Timestamp_Number', 'Topic', 'Partition', 'Offset', 'Timestamp_Number']
'''