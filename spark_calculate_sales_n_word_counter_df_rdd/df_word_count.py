from log.logger import log
from conf.access_config import property
from pyspark.sql import SparkSession, functions as func



class CountText:
    def count_text(self):
        try:
            log.info('Starting count_text')
            
            spark = SparkSession.builder \
                .appName('CountText') \
                .master('local') \
                .getOrCreate()
            
                
            # Create DF from text file 
            text_df = spark.read.text(property.access_config('file_path'))
            
            # Lowercase and split text into words + Separate all singular words into seperate rows. 
            split_lower_df = text_df.select(func.explode(func.split(func.lower(text_df.value), '\\s')).alias('words'))
            
            # Use groupby to count each occurrence of the word
            counted_df = split_lower_df.groupBy('words').count()
            
            # Show DF & Stop SparkSession
            counted_df.show()    
            spark.stop()
            
            
        except Exception as e:
            log.error(f'CHECK count_text ERROR: {e}')
            
        finally:
            log.info('Finishing count_text')
            
        
if __name__ == '__main__':
    ct = CountText()
    ct.count_text()