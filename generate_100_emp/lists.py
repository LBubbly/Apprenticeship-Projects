import random  
#---------------------------------------------------------------------------------  


def shuffle_list(a_list): 
    return random.shuffle(a_list) 


#---------------------------------------------------------------------------------  
 

def random_id_generator(id_list): 
    
    while len(id_list) < 100:  
        letter = chr(random.randint(ord('a'), ord('z'))) 
        letter = f'{letter}{len(id_list)+1}'  
        id_list.append(letter.upper())  

    return id_list 
 

#---------------------------------------------------------------------------------  


vowels = ['a', 'e', 'i', 'o', 'u', 'y']  
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',  
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']  
all_letters = ['m', 'n', 'b', 'v', 'c', 'x', 'z', 'l', 'k', 'j', 'h',   
               'g', 'f', 'd', 's', 'a', 'p', 'o', 'i', 'u', 'y', 't',  
               'r', 'e', 'w', 'q']  
 

def name_generator(names_list, comparison_list=[], comparison_list_2=[]): 
    
    while len(names_list) < 100: 

        for i in range(len(all_letters)): 
            for j in range(i+1, len(vowels)): 
                for k in range(j+1, len(consonants)): 
                    for l in range(k+1, len(all_letters)): 

                        name = f'{all_letters[i]}{vowels[j]}{consonants[k]}{all_letters[l]}' 
                        
                        if len(names_list) == 100: 
                            break 

                        if name in comparison_list: 
                            continue 
                        elif name in comparison_list_2: 
                            continue 
                        else: 
                            names_list.append(name.title()) 

                        shuffle_list(vowels) 
                        shuffle_list(consonants) 
                        shuffle_list(all_letters) 

    shuffle_list(names_list) 
    return names_list 


#---------------------------------------------------------------------------------  


def random_salaries(salary_list): 
    
    while len(salary_list) < 100:  
        shuffle_list(salary_list) 

        salary = random.randint(10000, 100000) 
        salary_list.append(salary) 

    return salary_list 


#---------------------------------------------------------------------------------  


def random_department(dep_list): 
    shuffle_list(dep_list) 

    while len(dep_list) < 100:  
        shuffle_list(dep_list) 

        dep = dep_list[0] 
        dep_list.append(dep) 

    return dep_list 


#---------------------------------------------------------------------------------  
 

def age_n_dates(age_list, birth_date_list, join_date_list): 

    count = 1 
    while count < 101:         
        current_year = 2023 
        age = random.randint(21, 60) 

        
        birth_year = current_year - age 
        birth_month = str(random.randint(1, 12)) 
        if len(birth_month) == 1:
            birth_month = f'0{birth_month}'
            
        if birth_month == '02': 
            birth_day = random.randint(1, 29) 
        else:  
            birth_day = random.randint(1, 31) 
        birth_date = f'{birth_year}-{birth_month}-{birth_day}' 


        join_year = random.randint(birth_year+21, 2023) 
        join_month = str(random.randint(1, 12)) 
        if len(join_month) == 1:
            join_month = f'0{join_month}'
            
        if join_month == '02': 
            join_day = random.randint(1, 29) 
        else:  
            join_day = random.randint(1, 31) 
        join_date = f'{join_year}-{join_month}-{join_day}' 


        age_list.append(age) 
        join_date_list.append(join_date) 
        birth_date_list.append(birth_date) 


        count += 1 

    return age_list, birth_date_list, join_date_list 


#---------------------------------------------------------------------------------  


''' 
print(f'*******************  IDS  *******************') 
print(ids_list) 
print(len(ids_list)) 


print(f'*******************  FIRST NAMES *******************') 
print(first_names_list) 
print(len(first_names_list), type(first_names_list)) 


print(f'*******************  LAST NAMES  *******************') 
print(last_names_list) 
print(len(last_names_list), type(last_names_list)) 


print(f'*******************  MANAGER NAMES *******************') 
print(manager_names_list) 
print(len(manager_names_list), type(manager_names_list)) 


t_names = [] 
for i in first_names_list: 
    t_names.append(i) 
for i in last_names_list: 
    t_names.append(i) 
for i in manager_names_list: 
    t_names.append(i) 
set_names = set(t_names) 
print(len(set_names), type(set_names)) 


print(f'*******************  AGES & DATES  *******************') 
count = 0 
while count < 100: 
    print(f'{ages_list[count]} | {join_dates_list[count]} | {birth_dates_list[count]}') 
    count += 1 

print(len(ages_list)) 
print(len(join_dates_list)) 
print(len(birth_dates_list)) 


print(f'*******************  SALARIES  *******************') 
print(salaries_list) 
print(len(salaries_list)) 


print(f'*******************  DEPARTMENTS *******************') 
print(departments_list) 
print(len(departments_list)) 

'''  