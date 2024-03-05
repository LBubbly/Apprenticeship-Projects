import random
import datetime
from .employee_class import Employee
from .department_class import Department


class Generators:
    def __init__(self):
        self.current_date = datetime.datetime.now()
        self.current_year = self.current_date.year
        self.departments_list = ['Finance', 'Marketing', 'Human Resources', 'Sales', 'IT', 'Customer Service',
                                 'Legal', 'Operations', 'Research and Development', 'Product Management']



    def id_generator(self, number_of_rows):
        try:
            letter = chr(random.randint(ord('a'), ord('z')))
            id_string = f'{letter.upper()}{number_of_rows + 1}'

            return id_string
        except:
            print('I don\'t!?!')



    def name_generator(self):
        try:
            name = ''
            for i in range(random.randrange(3,7)):
                name += chr(random.randint(ord('a'), ord('z')))

            return name.title()
        except:
            print('I don\'t!?!')



    def salary_generator(self):
        try:
            min_salary = 10000
            max_salary = 100000
            salary = random.randint(min_salary, max_salary)

            return salary
        except:
            print('I don\'t!?!')



    def department_generator(self):
        try:
            department = random.choice(self.departments_list)

            return department.title()
        except:
            print('I don\'t!?!')



    def age_generator(self):
        try:
            age = random.randint(21, 60)

            return age
        except:
            print('I don\'t!?!')



    def date_generator(self, year):
        try:
            month = random.randint(1, 12)
            if month == 2:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 31)
            date = datetime.date(year, month, day)

            return date
        except:
            print('Date out of bounds')
            return self.date_generator(year)



    def birth_date_generator(self, age):
        try:
            birth_year = self.current_year - age
            birth_date = self.date_generator(birth_year)

            return birth_date
        except:
            print('I don\'t!?!')



    def join_date_generator(self, birth_date):
        try:
            birth_year = birth_date.year
            join_year = random.randint(birth_year + 21, self.current_year)
            join_date = self.date_generator(join_year)

            return join_date
        except:
            print('I don\'t!?!')



    def employee_object_generator(self, number_of_objects, employees_list=[], specified_class=Employee):
        try:
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
        except:
            pass


    def department_object_generator(self, dept_list=[], specified_class=Department):
        try:
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
        except:
            pass

