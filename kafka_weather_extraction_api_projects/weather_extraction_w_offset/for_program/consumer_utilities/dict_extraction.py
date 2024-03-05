from logging_utilities.logger import log
# ---------------------------------------------------------------------------------

class DictExtraction:
    
    def complete_extraction(self, message, message_value):
        try: 
            # Logging starting execution of complete_extraction() 
            log.info(f'Started Execution of {self.complete_extraction.__name__}')
            
            
            dict_offset = {
                'topic_name': message.topic,
                'partition_number': message.partition,
                'offset_value': message.offset,
                'timestamp_number': message.timestamp
            }
            
            print('timestamp_number -', message.timestamp, '\nTYPE -', type(message.timestamp))
            
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
                'w_condition' : message_value['current']['condition']['text']
            }

            # Concat dict_offset + dict_offset
            dict_all = {**dict_offset, **dict_weather}
            
            # Retrieve each in 1 go... set up 3 variables to collect
            return dict_offset, dict_weather, dict_all 
        

        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.complete_extraction.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of complete_extraction() 
            log.info(f'Finished Execution of {self.complete_extraction.__name__}')
    
    
# Object to use everywhere
dict_maker = DictExtraction()