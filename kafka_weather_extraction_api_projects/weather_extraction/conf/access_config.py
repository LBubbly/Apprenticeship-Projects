from jproperties import Properties
from logging_utilities.logger import log


class AccessConfig:
    def access_config(self, property_to_access):
        try:
            log.info(f'Started Execution: {self.access_config.__name__} (Class: {AccessConfig.__name__}, Property Accessed: {property_to_access})')
            
            
            config = Properties()
            with open('conf\config.properties', 'rb') as config_file:  
                config.load(config_file)
                
            prop = config[f'{property_to_access}'].data
            return prop
        
        
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.access_config.__name__}, Error: {e}')
        
        
        finally:
            log.info(f'Finished Execution: {self.access_config.__name__}')
            
            
# Created AccessConfig object: property
property = AccessConfig()