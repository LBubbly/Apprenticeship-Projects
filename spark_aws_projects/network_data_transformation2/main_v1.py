import sys
import logging
from pyspark.sql import SparkSession, functions as func
#----------------------------------------------------------------------------------------------------------------------------

                                                                                 
class NetworkData:

    def network_data_transformation(self, input_path, output_path):
        try:
            logging.info('Starting network_data_transformation()')


            spark = SparkSession.builder \
                                .appName('NetworkDataTransformation') \
                                .master('local') \
                                .getOrCreate()


            # Create a df by looking through all json files within the specified input directory
            raw_df = spark.read.option("recursiveFileLookup", "true").json(input_path)


            # Collectively group the column values by 'companyid', 'type', and 'routerMac'
            grouped_df = raw_df.groupBy('companyid', 'type', 'routerMac')


            # Aggregate the count of the 'routerMac' column and name the column 'count'.
            # Then, collect the values from the 'stationMac' column into a list.
            aggre_df = grouped_df.agg(func.count('routerMac').alias('count'),
                                      func.collect_list('stationMac').alias('stationMac'))


            # Write seperate JSON files for each distinct combination of the 'companyId' and 'type' columns
            aggre_df.show()
            aggre_df.write.partitionBy('companyId', 'type').json(output_path)


        except Exception as e:
            logging.error(f'CHECK network_data_transformation() ERROR: {e}')

        finally:
            spark.stop()
            logging.info('Finishing network_data_transformation()')



if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    ndt = NetworkData()
    ndt.network_data_transformation(input_path, output_path)