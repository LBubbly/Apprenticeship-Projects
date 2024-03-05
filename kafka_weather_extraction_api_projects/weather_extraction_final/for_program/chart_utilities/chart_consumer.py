import json
import matplotlib.pyplot as plt
from kafka import KafkaConsumer
from conf.access_config import property
from logging_utilities.logger import log
from multiprocessing import Process
#-----------------------------------------------------------------


class ChartConsumer:    
    
    
    #-------------------------------------------------------------------------------------------------------------------
    def pie_chart(self, data_list):
   
        try:
            # Logging starting execution of pie_chart() 
            log.timestamp(f'Started Execution of {self.pie_chart.__name__}')
            print(f'PIE CHART DATA LIST LEN: {len(data_list)}')
            
            ## Counts for each cities within temperature range
            count_n10_n20 = 0
            count_n10_10 = 0 #
            count_10_15 = 0
            count_15_25 = 0
            count_25_30 = 0
            count_gt_30 = 0 #
            
            ## Iterate through collected data and increment count according to city's temperature
            for ct in data_list:
                if float(ct['temp_c']) < -10.0 and float(ct['temp_c']) >= -20.0:
                    count_n10_n20 += 1
                elif float(ct['temp_c']) >= -10.0 and float(ct['temp_c']) < 10.0:
                    count_n10_10 += 1
                elif float(ct['temp_c']) >= 10.0 and float(ct['temp_c']) < 15.0:
                    count_10_15 += 1
                elif float(ct['temp_c']) >= 15.0 and float(ct['temp_c']) < 25.0:
                    count_15_25 += 1
                elif float(ct['temp_c']) >= 25.0 and float(ct['temp_c']) < 30.0:
                    count_25_30 += 1
                elif float(ct['temp_c']) >= 30.0:
                    count_gt_30 += 1

            ## Lists: How big each slice is & Label each slice
            counts = [count_n10_n20, count_n10_10, count_10_15, count_15_25, count_25_30, count_gt_30]
            labels = [f'Temp_C (-10)-(-20): {count_n10_n20} Cities',
                      f'Temp_C (-10)-10: {count_n10_10} Cities',
                      f'Temp_C 10-15: {count_10_15} Cities',
                      f'Temp_C 15-25: {count_15_25} Cities', 
                      f'Temp_C 25-30: {count_25_30} Cities', 
                      f'Temp_C > 30: {count_gt_30} Cities']
            log.info(f'LABELS: {labels}')

            ##
            fig, ax = plt.subplots()
            ax.pie(counts, labels=labels, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
            plt.title('Temp_C Pie Chart')
            plt.show()
            
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.pie_chart.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of pie_chart() 
            log.info(f'Finished Execution of {self.pie_chart.__name__}')
    
    
    #-------------------------------------------------------------------------------------------------------------------
    def bar_chart(self, data_list):
        try:
            # Logging starting execution of bar_chart() 
            log.timestamp(f'Started Execution of {self.bar_chart.__name__}')
            print(f'BAR CHART DATA LIST LEN: {len(data_list)}')
            
            ## Create X & Y axis out of the city and temp keys
            cities = [ct['city_name'] for ct in data_list]
            temps = [ct['temp_c'] for ct in data_list]

            ##
            fig, ax = plt.subplots()
            ax.bar(cities, temps, width=0.7)

            ##
            ax.set_xlabel('Cities')
            ax.set_ylabel('Temperature_C -20 to 30')
            plt.title('City Temp_C Bar Plot')

            ##
            plt.xticks(rotation=90, fontsize=6.5)
            plt.show()
    
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.bar_chart.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of bar_chart() 
            log.info(f'Finished Execution of {self.bar_chart.__name__}')    

    
    #-------------------------------------------------------------------------------------------------------------------
    def data_collection(self, number):
        try:
            # Logging starting execution of data_collection() 
            log.timestamp(f'Started Execution of {self.data_collection.__name__}')
            print(f'Started Chart Consumer {number}...')
            
            ## Create KafkaConsumer
            consumer = KafkaConsumer(
                property.access_config('topic_name'),
                bootstrap_servers = property.access_config('server'),
                group_id = property.access_config('chart_consumer_group')
            )  
            
            ## 2 Lists: Collection of data, Comparison list to ensure uniqueness
            collected_data = []
            city_list = []
        
            while True:
                message_batch = consumer.poll(timeout_ms=1000)
                log.info(f'[MSG BATCH]: {message_batch}, {type(message_batch)}')    
                
                
                for partition, messages in message_batch.items():
                    log.info(f'[TOPIC PARTITION] - {partition}, {type(partition)}')
                    log.info(f'[MESSAGE INFO "messages"] - {messages}, {type(messages)}')
            
            
                    for message in messages:
                        
                        ## Retrieve Message Value
                        message_value = json.loads(message.value.decode('ascii'))
                        
                        
                        ## if, bad message, continue
                        if message_value == {}:
                            log.info(f'[BAD MESSAGE] - {message}')
                            print('Next Please...')
                            continue
                        else:
                            log.info(f'\n[MESSAGE] - {message}') 
                                    
                        
                        ## if, msg_value['city'] in list, continue     
                        city = message_value['location']['name']
                        if city in city_list:
                            log.info(f'{city.title()} already exists in city_list: {city_list}')
                            continue
                        else:
                            print(f'Chart Consumer {number} Appended City: {city.title()}')
                            city_list.append(city)
                        
                        
                        ## Create dict /w City, Temp
                        location_temp_dict = {
                            'city_name' : message_value['location']['name'],
                            'temp_c' : message_value['current']['temp_c']
                        }
                        
                        
                        ##
                        collected_data.append(location_temp_dict)
                        log.info(f'Chart Consumer {number} Appended to collected_data: {location_temp_dict}')
                        
                        
                        ##
                        count_str = f'[CHART CONSUMER {number} DATA COLLECTION COUNT] - {len(collected_data)}'


                        ## if, display charts
                        if len(collected_data) % 100 == 0 and len(collected_data) > 0: 
                            
                            #
                            log.info(f'[CHART CONSUMER {number} DATA COLLECTION LIST] -> LEN: {len(collected_data)}, VALUES: {collected_data}')
                            print(f'**********CONSUMER {number} CHARTING NOW*********\n{count_str}') 
                            
                            #
                            consumer.pause()
                            pause_msg = f'Chart Consumer {number} Pause...'
                            print(pause_msg)
                            log.info(pause_msg)
                            
                            # Display Charts
                            self.bar_chart(collected_data)
                            self.pie_chart(collected_data)
                            
                            # Empty Lists
                            collected_data = []
                            city_list = []
                            
                            #
                            consumer.resume()
                            resume_msg = f'Chart Consumer {number} Resumed...'
                            print(resume_msg)
                            log.info(resume_msg)
                        
                        ##
                        log.info(count_str)            
                        log.info(f'Chart Consumer {number} ready to continue...')
            
        
        
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.data_collection.__name__} ERROR: {e}')
            self.data_collection()
        finally:
            # Logging finished execution of data_collection() 
            log.info(f'Finished Execution of {self.data_collection.__name__}')
        
        
    
    #-------------------------------------------------------------------------------------------
    def multiprocess_consuming(self):
        
        try:
            # Logging starting execution of multiprocess_consuming() 
            log.timestamp(f'Started Execution of {self.multiprocess_consuming.__name__}')
            
                        
            processes = []
            for i in range(3):
                log.timestamp(f'Processing Consumer {i}')
                process = Process(target=self.data_collection, args=(i,))
                process.start()
                processes.append(process)
                log.timestamp(f'Consumer Process {i} Running...')

            count = 0
            for process in processes:
                process.join()
                log.timestamp(f'Consumer Process {count} Joined.')
                count += 1
                
                
        except Exception as e:
            # Logging error if found 
            log.error(f'[!!!] CHECK: {self.multiprocess_consuming.__name__} ERROR: {e}')
        finally:
            # Logging finished execution of multiprocess_consuming() 
            log.info(f'Finished Execution of {self.multiprocess_consuming.__name__}')
        
        
#-----------------------------------------
charter = ChartConsumer()