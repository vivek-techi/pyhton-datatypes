My_List = [' vivek ', " Prakash ", 5, 5.386]

# length
print(len(My_List))
# indexing
print(My_List[2])
# slicing
print(My_List[:3])

print(My_List)

New_List = My_List + [' dom ', 10, 2.236]
print(f"the new list is : {New_List} ")


# methods in lists
List1 = [5, 2, 8]
List1.append(4)
print(List1)

List1.pop()
print(List1)

List1.sort()
print(List1)

# nested list

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

matrix = [list_1, list_2, list_3]

print("the output is  :{} ".format(matrix))
