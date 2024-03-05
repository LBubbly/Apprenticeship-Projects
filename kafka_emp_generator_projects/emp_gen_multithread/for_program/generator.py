from random import randint, randrange, choice
from kafka_logging.kafka_logger import kafka_log

class Generator:
    
    def letter(self):
        try:
            # Logging starting execution of letter()
            kafka_log.info(f'Started Execution of {self.letter.__name__}')
            
            # Returns a random uppercase letter from A-Z
            return chr(randint(ord('a'), ord('z'))).upper()
        
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.letter.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of letter() 
            kafka_log.info(f'Finished Execution of {self.letter.__name__}')
    
    
    
    def name(self):
        try:
            # Logging starting execution of name() 
            kafka_log.info(f'Started Execution of {self.name.__name__}')
        
            # Creating a random name with 3-7 letters 
            name = ''
            for _ in range(randrange(3,7)):
                name += chr(randint(ord('a'), ord('z')))
            return name.title()
    
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.name.__name__} ERROR: {e}')
        finally:
            # Logging finishing execution of name() 
            kafka_log.info(f'Finished Execution of {self.name.__name__}')
    
    
    
    def generate(self):
        try:
            # Logging starting execution of generate() 
            kafka_log.info(f'Finished Execution of {self.generate.__name__}')  
            
            # Variables for random data
            id = f"{self.letter()}{self.letter()}{randint(1, 999)}"
            name = f"{self.name()} {self.name()}" 
            age = randint(21, 60)
            salary = randint(10000, 100000)
            department_list = ['Finance', 'Marketing', 'Human Resources', 'Sales', 'IT', 'Customer Service',
                            'Legal', 'Operations', 'Research and Development', 'Product Management']
            department = choice(department_list)
            
            # Placing variables in dictionary
            dict_format = {
                "id" : id,
                "name" : name,
                "age" : age,
                "salary" : salary,
                "department" : department
            }
            
            # Return dictionary
            return dict_format
        
        except Exception as e:
            # Logging error if found 
            kafka_log.error(f'[!!!] CHECK: {self.generate.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of generate() 
            kafka_log.info(f'Finished Execution of {self.generate.__name__}')   
 
    
# Created Generator() object: generator
generator = Generator()