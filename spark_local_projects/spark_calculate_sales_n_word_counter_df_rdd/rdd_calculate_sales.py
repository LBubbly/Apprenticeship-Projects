import json
from log.logger import log
from pyspark.sql import SparkSession
from conf.access_config import property
#----------------------------------------------------------------------------------------------------------------------------

class Sales:
    
    def calculate(self, row):
        try:
            # Modify header row
            if row[0] == 'Property_ID':
                row = row[:-2]
                row.append('Final Price')
            # Calculate Final Price (Size * Price_SQ_FT)
            else:
                row[2] = str(round(float(row[2]) * float(row[3]),2))
                del row[3]
            return row
    
        except Exception as e:
            log.error(f'[CALCULATION ERROR] - {e}')
        finally:
            log.info('Finished Calculating')
        
    
    
    def stringify(self, row):
        try:
            # Create and return a string delimited by '|'
            string = '|'.join(row)
            log.info(f'String: {string}')
            return string
        
        except Exception as e:
            log.error(f'[STRINGIFY ERROR] - {e}')
        finally:
            log.info('Finished Stringifying')
    
    
    
    def jsonify(self, row):
        try:
            if row[0] == 'Property_ID':
                del row
            else:
                return json.dumps({'Property_ID': row[0], 'Location': row[1], 'Final Price': row[2]}) 
            
        except Exception as e:
            log.error(f'[JSONIFY ERROR] - {e}')
        finally:
            log.info('Finished Stringifying')
    
    
    
    def sales(self):
        try:
            log.info('Starting sales')
            spark = SparkSession.builder  \
                    .appName('Sales') \
                    .master('local') \
                    .getOrCreate()
                    
            
            # Make text file an RDD
            text_rdd = spark.sparkContext.textFile(property.access_config('input_path'))            
            
            # Transform each row into a list and split each row by '|' 
            split_rdd = text_rdd.map(lambda x: list(x.split('|')))      
            
            # Keep columns & associated values:   Property_ID | Location | Size | Price_SQ_FT
            kept_rdd = split_rdd.map(lambda x: [x[0], x[1], x[5], x[6]])
            
            # Used self.calculate to modify & calculate Final Price column
            calculated_rdd = kept_rdd.map(self.calculate)
            
            
            
            # Stringify & Save calculated_rdd as text file
            string_rdd = calculated_rdd.map(self.stringify) 
            string_rdd.saveAsTextFile(property.access_config('rdd_output'))
            
            # Transform into JSON & Save json_rdd
            json_rdd = calculated_rdd.map(self.jsonify)
            json_rdd.saveAsTextFile(property.access_config('rdd_output_json'))
            
                
        except Exception as e:
            log.error(f'[EXECUTION ERROR] - {e}')
        finally:
            spark.stop()
            log.info('Spark Stopped, Finishing sales')
   

        
if __name__ == '__main__':
    s = Sales()
    s.sales()