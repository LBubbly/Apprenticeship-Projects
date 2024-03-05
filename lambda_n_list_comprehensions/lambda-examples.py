
'''
LAMBDAS - an anonymous function used for short, simple, and singular functionality 

General Syntax: lambda_name = lambda parameter_s : expression 

Standalone Syntax: (lambda parameter_s : expression)(argument_s)

Variable Mode Syntax: lambda_var = lambda parameter_s : expression
                      lambda_var(argument_s)
                      
Argument Mode Syntax: map(lambda parameter_s : expression, collection)
  ^^Use /w list()^^   filter(lambda parameter_s : expression, collection)
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print((lambda n1, n2 : n1 - n2)(10, 5))

sub = lambda n1, n2 : n1 - n2
print("sub:", sub(10,5))

mapped_nums = map(lambda n : n + 1, nums)
print("mapped:", list(mapped_nums))

filtered_nums = filter(lambda n : n % 2 == 1, nums)
print("filtered:", list(filtered_nums))

print(sub.__name__)

