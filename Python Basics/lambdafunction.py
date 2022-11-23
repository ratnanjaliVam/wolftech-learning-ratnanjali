# Implementing the same problem using lambda function
# lambda functions are the functions that are not pre-defined and can be created at the time when we need them

my_list = [11, 12, 13, 14, 18]

for i in my_list:
    isOdd = lambda x : x%2 != 0
    print(isOdd(i))