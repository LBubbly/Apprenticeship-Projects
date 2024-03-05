from log.logger import log
from pyspark.sql import SparkSession
#----------------------------------------------------------------------------------------------------------------------------

class Sales:
    
    def sales(self):
        try:
            log.info('Starting sales')
            spark = SparkSession.builder  \
                    .appName('Sales') \
                    .master('local') \
                    .getOrCreate()
                    
            
            # Make text file an RDD
            file_path = 'C:\\...\\spark_sales_reduce_n_calculate_rdd\\files\\sales.txt'
            text_rdd = spark.sparkContext.textFile(file_path)
            log.info(f'Text File RDD: {text_rdd}\nType Text File RDD: {type(text_rdd)}\nCollected Text File RDD: {text_rdd.collect()}')
            
            
            # Transform each row into a list and split each row by '|' 
            split_rdd = text_rdd.map(lambda x: list(x.split('|')))
            log.info(f'Split RDD: {split_rdd}\nType Split RDD: {type(split_rdd)}\nCollected Split RDD: {split_rdd.collect()}')
            
            
            # Keep columns & associated values:   Property_ID | Location | Size | Price_SQ_FT
            kept_rdd = split_rdd.map(lambda x: [x[0], x[1], x[5], x[6]])
            log.info(f'Kept RDD: {split_rdd}\nType Kept RDD: {type(split_rdd)}\nCollected Kept RDD: {split_rdd.collect()}')
            
            
            # Modify list of columns and calculate Final Price (Size * Price_SQ_FT)
            calculated = []
            for i, v in enumerate(kept_rdd.collect()):
                
                # Modify list of column header
                if i == 0:
                    v = v[:-2]
                    v.append('Final Price')
                    calculated.append(v)
                    log.info(f'Column Header Names: {v}')
                    continue
                
                # Calculate Value for 3rd Column (Final Price)   ->   Calculate Final Price, Delete last column, Append List
                v[2] = str(round(float(v[2]) * float(v[3]), 2))
                del v[3] 
                calculated.append(v)
                
                log.info(f'Index:{i}, Value: {v}, Type: {type(v)}')
            log.info(f'Calculated: {calculated}\nType Calculated: {type(calculated)}')
            
            
            # Create a list of strings delimited by '|'
            strings_list = ['|'.join(a_list) for a_list in calculated]
            log.info(f'String List: {strings_list}')
            
            
            # Convert list of lists to RDD
            string_rdd = spark.sparkContext.parallelize(strings_list)
            print('String RDD:', string_rdd.collect(), type(string_rdd))
            
            
            # Save calculated_rdd as text file
            output_path = 'C:\\...\\spark_sales_reduce_n_calculate_rdd\\files\\final_sales'
            # string_rdd.saveAsTextFile(output_path)
            
            with open(output_path, 'w') as file:
                for row in string_rdd.collect():
                    file.write(row +'\n')
            
                
        except Exception as e:
            log.error(f'[ERROR] - {e}')
        finally:
            spark.stop()
            log.info('Spark Stopped, Finishing sales')
   

        
if __name__ == '__main__':
    s = Sales()
    s.sales()