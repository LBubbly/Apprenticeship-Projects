from logging_utilities.logger import log
# ---------------------------------------------------------------------------------

class DictExtraction:
    
    def complete_extraction(self, message, message_value):
        try: 
            log.info(f'Started Execution of {self.complete_extraction.__name__}')
            
            
            dict_offset = {
                'topic_name': message.topic,
                'partition_number': message.partition,
                'offset_value': message.offset,
                'timestamp_number': message.timestamp
            }
            
            
            dict_weather = {
                'city_name' : message_value['location']['name'],
                'country_name' : message_value['location']['country'],
                'lat' : message_value['location']['lat'],
                'lon' : message_value['location']['lon'],
                'localtime_epoch' : message_value['location']['localtime_epoch'],
                'temp_c' : message_value['current']['temp_c'],
                'temp_f' : message_value['current']['temp_f'],
                'wind_mph' : message_value['current']['wind_mph'],
                'wind_kph' : message_value['current']['wind_kph'],
                'vis_km' : message_value['current']['vis_km'],
                'vis_miles' : message_value['current']['vis_miles'],
                'w_condition' : message_value['current']['condition']['text'],
                'timestamp_number': message.timestamp
            }
            
            # Retrieve each in 1 go... 
            return dict_offset, dict_weather 
        

        except Exception as e:
            log.error(f'[!!!] CHECK: {self.complete_extraction.__name__} ERROR: {e}')
        finally:
            log.info(f'Finished Execution of {self.complete_extraction.__name__}')
    
    
# Object to use everywhere
dict_maker = DictExtraction()