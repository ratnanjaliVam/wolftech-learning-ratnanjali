# A simple function to test whether a given list has odd numbers or not

def isOdd(a):
    if a % 2 != 0:
        return True
    else:
        return False


my_list = [11,12,13,14,18]

for i in my_list:
    print(isOdd(i))