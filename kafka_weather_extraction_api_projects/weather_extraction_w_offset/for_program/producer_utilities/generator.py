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
            # print('API_URL', api_url)
            response = requests.get(api_url)
            # print('RESPONSE', response)
            
            if response.status_code == 200:
                data = response.json()
                
                print('TYPE', type(data), 
                      '\nDATA', data)
                return data # Returns dict
            else:
                print('Nothing returned...')


        except Exception as e:
            log.error(f'[!!!] CHECK: {self.get_data.__name__} ERROR: {e}')
        finally:
            log.info(f'Ended Execution of {self.get_data.__name__}')


weather_generator = WeatherAPIGenerator()