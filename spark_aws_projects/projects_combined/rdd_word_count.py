from log.logger import log
from pyspark.sql import SparkSession
from conf.access_config import property



class CountText:
    def count_text(self):
        try:
            log.info('Starting count_text')
            
            spark = SparkSession.builder \
                .appName('CountText') \
                .master('local') \
                .getOrCreate()
                
                
            # Create RDD from text file 
            text_file_rdd = spark.sparkContext.textFile(property.access_config('file_path'))     
            
            # Use map to make all text lowercase
            lowercase = text_file_rdd.map(lambda x: x.lower())
            
            # Use flatMap to split text into words 
            words = lowercase.flatMap(lambda x: x.split(' '))
            
            # Use countByValue to return a dictionary of each each unique {'word': count}
            occurences = words.countByValue()
            
            # Show Word: Count
            for word, count in occurences.items():
                print(f'{word}: {count}')
            
                
            spark.stop()
            
        except Exception as e:
            log.error(f'CHECK count_text ERROR: {e}')
            
        finally:
            log.info('Finishing count_text')
            
        
if __name__ == '__main__':
    ct = CountText()
    ct.count_text()
    
'''

log.info(f'Text File RDD: {text_file_rdd}\nType Text File RDD: {type(text_file_rdd)}\nCollected Text File RDD: {text_file_rdd.collect()}')

 
log.info(f'Lowercase: {lowercase}\nType Lowercase: {type(lowercase)}\nCollected Lowercase: {lowercase.collect()}')


log.info(f'Words: {words}\nType Words: {type(words)}\nCollected Words: {words.collect()}')


log.info(f'Occurences: {occurences}\nType Occurences: {type(occurences)}')   
            
'''