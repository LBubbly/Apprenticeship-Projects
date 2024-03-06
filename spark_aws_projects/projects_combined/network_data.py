from log.logger import log
from conf.access_config import property
from pyspark.sql import SparkSession, functions as func
#----------------------------------------------------------------------------------------------------------------------------


class NetworkData:
    def network_data_transformation(self):
        try:
            log.info('Starting network_data_transformation()')
            
            spark = SparkSession.builder \
                                .appName('NetworkDataTransformation') \
                                .master('local') \
                                .getOrCreate()
                 
                 
            # Read Raw Data JSON File               
            raw_df = spark.read.json(property.access_config('network_data_path'))
            
            
            # Count Connected routerMac, deviceMac, and type of devices
            count_df = raw_df.groupBy('routerMac', 'deviceMac', 'type').count()
            count_df.show()
            
            
            # Reorganize Columns 
            rearranged_df = count_df.select('routerMac', 'count', 'deviceMac')
            rearranged_df.show()
            
            
            # Write Transformed DF to JSON File
            rearranged_df.write.json(property.access_config('network_data_output'))
            
            

        except Exception as e:
            log.error(f'CHECK network_data_transformation() ERROR: {e}')
            
        finally:
            spark.stop()
            log.info('Finishing network_data_transformation()')
            
            

if __name__ == '__main__':
    ndt = NetworkData()
    ndt.network_data_transformation()