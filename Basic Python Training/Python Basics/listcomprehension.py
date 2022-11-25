list1 = [5, 8, 16, 1, 5]
list2 = [2, 4, 4, 10, 10]

new_list = [(i+j)/2 for i, j in zip(list1, list2)]
print(new_list)

