from pyspark.sql import SparkSession
from logger import log

class WordCount:
    def word_count(self):
        try:
            log.info('Starting word_count')
            
            spark = SparkSession.builder \
                .appName('WordCount') \
                .master('local') \
                .getOrCreate()
                
            # Create RDD from text file 
            file_path = 'C:\\...\\spark_word_counter_rdd\\text.txt' 
            text_file_rdd = spark.sparkContext.textFile(file_path)     
            log.info(f'Text File RDD: {text_file_rdd}\nType Text File RDD: {type(text_file_rdd)}\nCollected Text File RDD: {text_file_rdd.collect()}')
            
            # Use map to make all text lowercase
            lowercase = text_file_rdd.map(lambda x: x.lower()) 
            log.info(f'Lowercase: {lowercase}\nType Lowercase: {type(lowercase)}\nCollected Lowercase: {lowercase.collect()}')
            
            # Use flatMap to split text into words 
            words = lowercase.flatMap(lambda x: x.split(' '))
            log.info(f'Words: {words}\nType Words: {type(words)}\nCollected Words: {words.collect()}')
            
            # Use countByValue to return a dictionary of each each unique {'word': count}
            occurences = words.countByValue()
            log.info(f'Occurences: {occurences}\nType Occurences: {type(occurences)}')   
            
            
            for word, count in occurences.items():
                print(f'{word}: {count}')
            
                
            spark.stop()
            
        except Exception as e:
            log.error(f'CHECK word_count ERROR: {e}')
            
        finally:
            log.info('Finishing word_count')
            
        
if __name__ == '__main__':
    ct = WordCount()
    ct.word_count()