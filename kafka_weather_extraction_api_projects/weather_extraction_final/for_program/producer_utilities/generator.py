import requests
from conf.access_config import property
from logging_utilities.logger import log


class WeatherAPIGenerator:               
    def get_data(self, 
                 criteria, # For city | country
                 api_key = property.access_config('api_key')):
        
        try:
            log.info(f'Started Execution of {self.get_data.__name__}')
            
            api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={criteria}&aqi=no'
            response = requests.get(api_url)
            
            if response.status_code == 200:
                data = response.json()
                log.info(f'\nTYPE {type(data)}\nDATA {data}')
                return data # Returns dict
            
            else:
                print('Nothing returned...')
                return {} # Return empty dictionary as the message value 
                          # Something predictable to handle on the other side (Consumer)

 
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.get_data.__name__} ERROR: {e}')
        finally:
            log.info(f'Ended Execution of {self.get_data.__name__}')


weather_generator = WeatherAPIGenerator()