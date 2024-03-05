import json
from kafka_logging.kafka_logger import kafka_log


class JSONOperations:    
    def generate_emps_to_json(self, employees_list):
        try:
            kafka_log.info(f'Started Execution: {self.generate_emps_to_json.__name__} (Class: {JSONOperations.__name__})')
            
            for_json = []
            for employee in employees_list:
                for_json.append(employee)

            with open(f"{property.access_pg_sql_file('employee_json_file_path')}", 'w') as file:
                json.dump(for_json, file, indent=4)
        except Exception as e:
            kafka_log.error(f'[!!!] CHECK: {self.generate_emps_to_json.__name__}, ERROR: {e}')
        else:
            kafka_log.info('Successful Generation to Employee JSON File!')
        finally:
            kafka_log.info(f'Finished Execution: {self.generate_emps_to_json.__name__}')
        
