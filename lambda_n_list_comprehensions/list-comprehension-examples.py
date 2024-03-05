'''
LIST COMPREHENSIONS - A way of creating a new list with a list that already exists. 

General Syntax: nl_name = [ expression for item in e_collection ] 

Front "if": nl_name = [ if-else statement for item in e_collection ]
Back "if": nl_name = [ expression for item in e_collection if condition ]

Nested Comprehension: nl_name = [ [ expression for item in e_collection ] for item in e_collection ]

...flattened_m = [ element for row in matrix for element in row ]
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_nums = [1, 2, 3]
matrix = [ [10, 20, 30], 
           [40, 50, 60], 
           [70, 80, 90] ]


new_nums = [ num * 2 for num in nums ]
print(new_nums)

f_nums = [ num if num % 2 == 1 else "even steven" for num in nums]
print(f_nums)

b_nums = [ num for num in nums if num % 2 == 1]
print(b_nums)

nc_s = [ [ s for s in s_nums ]  for s in s_nums ]
print(nc_s)