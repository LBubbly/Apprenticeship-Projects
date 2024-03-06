from log.logger import log
from conf.access_config import property
from pyspark.sql import SparkSession, functions as func
#----------------------------------------------------------------------------------------------------------------------------

class CalculateSales:
    
    def sales(self):
        try:
            log.info('Starting sales')
            spark = SparkSession.builder  \
                    .appName('Sales') \
                    .master('local') \
                    .getOrCreate()
                    
            
            # Make text file an DF
            text_df = spark.read.text(property.access_config('input_path'))
            
            
            # Transform each row into a list and split each row by '|'  
            split_df = text_df.select(func.split(text_df.value, '\\|').alias('split'))
            
            
            # Keep columns & associated values:   Property_ID | Location | Size | Price_SQ_FT
            four_col_df = split_df.select(split_df[0][0], split_df[0][1], split_df[0][5], split_df[0][6])
            
            
            # Rename df columns and remove the first row / header row
            renamed_df = four_col_df.withColumnRenamed('split[0]', 'Property_ID') \
                                    .withColumnRenamed('split[1]', 'Location') \
                                    .withColumnRenamed('split[5]', 'Size') \
                                    .withColumnRenamed('split[6]', 'Price_SQ_FT') 
            renamed_df = renamed_df.where(renamed_df.Property_ID != 'Property_ID')
            
            
            
            # Calculate Final_Price column, Drop Size + Price_SQ_FT columns, & Save as JSON
            calculated_df = renamed_df.withColumn('Final_Price', func.round(func.col('Size') * func.col('Price_SQ_FT'), 2)) \
                                      .drop('Size', 'Price_SQ_FT')
            calculated_df.write.json(property.access_config('df_output_json'))
            
            
            # Join columns with '|' as separator & Save as text file
            string_df = calculated_df.withColumn('Joined_By_Pipe', func.concat_ws('|', 'Property_ID', 'Location', 'Final_Price')) \
                                     .drop('Property_ID', 'Location', 'Final_Price')
            string_df.write.text(property.access_config('df_output'))
            
            
                
        except Exception as e:
            log.error(f'[EXECUTION ERROR] - {e}')
        finally:
            spark.stop()
            log.info('Spark Stopped, Finishing sales')
   

        
if __name__ == '__main__':
    s = CalculateSales()
    s.sales()