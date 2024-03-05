import random
import datetime
from .employee_class import Employee
from .department_class import Department
from logging_details.logger_class import log



class Generators:
    def __init__(self):
        self.current_date = datetime.datetime.now()
        self.current_year = self.current_date.year
        self.departments_list = ['Finance', 'Marketing', 'Human Resources', 'Sales', 'IT', 'Customer Service',
                                 'Legal', 'Operations', 'Research and Development', 'Product Management']


    def id_generator(self, number_of_rows):
        try:
            log.info(f'Started Execution: {self.id_generator.__name__} (Class: {Generators.__name__})')
            letter = chr(random.randint(ord('a'), ord('z')))
            id_string = f'{letter.upper()}{number_of_rows + 1}'

            return id_string
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.id_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.id_generator.__name__}')
        
        
    def name_generator(self):
        try:
            log.info(f'Started Execution: {self.name_generator.__name__} (Class: {Generators.__name__})')
            name = ''
            for i in range(random.randrange(3,7)):
                name += chr(random.randint(ord('a'), ord('z')))

            return name.title()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.name_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.name_generator.__name__}')
        
        
    def salary_generator(self):
        try:
            log.info(f'Started Execution: {self.salary_generator.__name__} (Class: {Generators.__name__})')
            min_salary = 10000
            max_salary = 100000
            salary = random.randint(min_salary, max_salary)

            return salary
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.salary_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.salary_generator.__name__}')

        
    def department_generator(self):
        try:
            log.info(f'Started Execution: {self.department_generator.__name__} (Class: {Generators.__name__})')
            department = random.choice(self.departments_list)

            return department.title()
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.department_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.department_generator.__name__}')

        
    def age_generator(self):
        try:
            log.info(f'Started Execution: {self.age_generator.__name__} (Class: {Generators.__name__})')
            age = random.randint(21, 60)

            return age
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.age_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.age_generator.__name__}')

        
    def date_generator(self, year):
        try:
            log.info(f'Started Execution: {self.date_generator.__name__} (Class: {Generators.__name__})')
            month = random.randint(1, 12)
            if month == 2:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 31)
            date = datetime.date(year, month, day)

            return date
        except Exception as e:
            log.info('Date out of bounds')
            return self.date_generator(year)
        finally:
            log.info(f'Finished Execution: {self.date_generator.__name__}')


    def birth_date_generator(self, age):
        try:
            log.info(f'Started Execution: {self.birth_date_generator.__name__} (Class: {Generators.__name__})')
            birth_year = self.current_year - age
            birth_date = self.date_generator(birth_year)

            return birth_date
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.birth_date_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.birth_date_generator.__name__}')

        
    def join_date_generator(self, birth_date):
        try:
            log.info(f'Started Execution: {self.join_date_generator.__name__} (Class: {Generators.__name__})')
            birth_year = birth_date.year
            join_year = random.randint(birth_year + 21, self.current_year)
            join_date = self.date_generator(join_year)

            return join_date
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.join_date_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.join_date_generator.__name__}')


    ''' 
    INHERIT FROM THE ABOVE -> class ObjectGenerator: ?? 
    USE super() 
    '''
    def employee_object_generator(self, number_of_objects, employees_list=[], specified_class=Employee):
        try:
            log.info(f'Started Execution: {self.employee_object_generator.__name__} (Class: {Generators.__name__})')
            while len(employees_list) < number_of_objects:
                age = self.age_generator()
                birth_date = self.birth_date_generator(age)
                join_date = self.join_date_generator(birth_date)

                employees_list.append(
                    specified_class(
                        self.id_generator(len(employees_list)),
                        self.name_generator(),
                        self.name_generator(),
                        age,
                        birth_date,
                        join_date,
                        self.salary_generator(),
                        self.name_generator(),
                        self.department_generator()))

            return employees_list
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.employee_object_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.employee_object_generator.__name__}')

        
    def department_object_generator(self, dept_list=[], specified_class=Department):
        try:
            log.info(f'Started Execution: {self.department_object_generator.__name__} (Class: {Generators.__name__})')
            random.shuffle(self.departments_list)

            for department in self.departments_list:
                if len(dept_list) == 10:
                    break
                
                dept_list.append(
                    specified_class(
                        f'DEP{len(dept_list)+1}',
                        department
                    ))

            return dept_list
        except Exception as e:
            log.error(f'[!!!] CHECK: {self.department_object_generator.__name__}, ERROR: {e}')
        finally:
            log.info(f'Finished Execution: {self.department_object_generator.__name__}')
