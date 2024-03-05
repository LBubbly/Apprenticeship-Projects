from .to_postgres_class import ToPostgres
from logging_details.logger_class import log
from config.access_properties import property


class ETLProgram:

    def etl_csv_or_json_display(self):
        try:
            log.info(f'Started Execution: {self.etl_csv_or_json_display.__name__} (Class: {ETLProgram.__name__})')

            selected_file_format = input(f"{property.access_displays('type_of_file_load_display')} ")
            match selected_file_format.lower():
                case '1':
                    selected_file_format = 'csv'
                case '2':
                    selected_file_format = 'json'
                case default:
                    print(f'INVALID INPUT: {selected_file_format}')
                    self.etl_csv_or_json_display()

            return selected_file_format
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.etl_csv_or_json_display.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.etl_csv_or_json_display.__name__}')



    def etl_emp_or_dept_display(self):
        try:
            log.info(f'Started Execution: {self.etl_emp_or_dept_display.__name__} (Class: {ETLProgram.__name__})')
            
            selected_data_type = input(f"{property.access_displays('type_of_data_display')} ")
            match selected_data_type.lower():
                case '1':
                    selected_data_type = 'employee'
                    return selected_data_type
                case '2':
                    selected_data_type = 'department'
                    return selected_data_type
                case '3':
                    selected_data_type = 'both'
                    return selected_data_type
                case default:
                    print(f'INVALID INPUT: {selected_data_type}')
                    self.etl_emp_or_dept_display()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.etl_emp_or_dept_display.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.etl_emp_or_dept_display.__name__}')


    def etl_selector(self, selected_file_format, selected_data_type):
        try:
            log.info(f'Started Execution: {self.etl_selector.__name__} (Class: {ETLProgram.__name__})')
            
            etl_obj = ToPostgres()
            
            if selected_file_format == 'csv' and selected_data_type == 'both':
                print(f'FILE: {selected_file_format}\nDATA: {selected_data_type}')
                etl_obj.csv_to_postgres('employee')
                etl_obj.csv_to_postgres('department')
                                
            elif selected_file_format == 'csv':
                print(f'FILE: {selected_file_format}\nDATA: {selected_data_type}')
                etl_obj.csv_to_postgres(selected_data_type)
                
            # ...
                
            elif selected_file_format == 'json' and selected_data_type == 'both':
                print(f'FILE: {selected_file_format}\nDATA: {selected_data_type}')
                etl_obj.json_to_postgres('employee')
                etl_obj.json_to_postgres('department')
                
            elif selected_file_format == 'json':
                print(f'FILE: {selected_file_format}\nDATA: {selected_data_type}')
                etl_obj.json_to_postgres(selected_data_type)
                
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.etl_selector.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.etl_selector.__name__}')



'''
    def rename_columns(self):
        try:
            pass
        except:
            pass
        else:
            pass

'''