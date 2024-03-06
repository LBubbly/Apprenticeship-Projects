import sys
from log.logger import log
from conf.access_config import property
from pyspark.sql import SparkSession, functions as func
#----------------------------------------------------------------------------------------------------------------------------


class NetworkData:
    def network_data_transformation(self, input_path):
        try:
            log.info('Starting network_data_transformation()')
            spark = SparkSession.builder \
                                .appName('NetworkDataTransformation') \
                                .getOrCreate()
            
            
            # Create a df by looking through all json files within the specified input directory
            raw_df = spark.read.option("recursiveFileLookup", "true").json(input_path)
            
            
            # Collectively group the column values by 'companyId', 'type', and 'routerMac'
            grouped_df = raw_df.groupBy('companyId', 'type', 'routerMac')
            
            
            # Aggregate the count of the 'routerMac' column and name the column 'count'.
            # Then, collect the values from the 'deviceMac' column into a list.
            aggre_df = grouped_df.agg(func.count('routerMac').alias('count'),
                                      func.collect_list('stationMac').alias('stationMac'))
            
            
            # Write seperate JSON files for each distinct combination of the 'companyId' and 'type' columns
            aggre_df.write.partitionBy('companyId', 'type').json(property.access_config("sd_output_path"))
            
            
        except Exception as e:
            log.error(f'CHECK network_data_transformation() ERROR: {e}')
        finally:
            log.info('Finishing network_data_transformation()')
            spark.stop()



#----------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    input_path = sys.argv[1]    
    
    ndt = NetworkData()
    ndt.network_data_transformation(input_path) 