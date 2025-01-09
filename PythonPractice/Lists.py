# Lists in pyhton

list =[12,234,34,12,76,67]
str1 =['rutu', 'vidya','shruti']

print(type(list))
print(list)
print(str1)

mix = [list,str1]
print(mix)

# to add element at end
list.append(45)
print(list)

# to add element at position
list.insert(1,20)
print(list)

list.insert(2,29)
print(list)

# remove element from list
list.remove(234)
print(list)

# to remove using index
list.remove(list[3])
print(list)

list.pop(3)
print(list)

# to delete multiple elements from list
del list[2:]
print(list)

# to add multiple elements in list
list.extend([17,2,89,34,44])
print(list)

# to find minimum number
print(min(list))

# to find maximum number
print(max(list))

# to do sum of all number
s = sum(list)
print(s)

# to sort numbers
list.sort() 
print(list)

list.sort(reverse=True)
print(list)

# to update item
list[4] = "Hiii"
print(list)
# for multiple atom
list[4:] = "Hiii", "Hello", "GoodMorning"
print(list)


print(list.__sizeof__)


list1 = ["apple","banana","guava","Cherries","banana","cherries","Banana","banana","Apple"]
print(list1.index("cherries"))

# to count element hoe many time occurs
print(list1.count("cherries"))
print(list1.count("banana"))
print(list1.count("guava"))


# sorting
list1.sort(reverse=True)
print(list1)

list1.sort(key=str.lower)
print(list1)

list1.sort(key=str.upper)
print(list1)

l = [["a","b","c"],["d","e","f"],["g","h","i"]]
print(l[1:][1])


# to print matrix
list1 = [] 
for i in range(3):
    list1.append([])
    for j in range(3):
        list1[i].append(j)
    for i in list1:
        print(i)
# easy way this is with list comprehension
matrix = [[y for y in range(4)] for x in range(4)]
print(matrix)


Mat1 = [[11, 12, 13],
[14, 15, 16],
[17, 18, 19]]
Mat2 = [[21, 22, 23],
[24, 25, 26],
[27, 28, 29]]
sum12 = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for i in range (len (Mat1)):
    for j in range (len (Mat1 [0])):
        sum12 [i][j] = Mat1 [i][j] + Mat2 [i][j]
for i in sum12:
    print (i)
    
    
    
# list comprehension

# traditonal way
name = ["rutuja","moni","vidya","shruti","aditya"]
name_with_a = []
for all_items in name:
    if "a" in all_items:
        name_with_a.append(all_items)
        
print(name_with_a)

# [list(expression) for item in collectio]
# [list(expression) for item in collectio if condition == TRUE]
name = ["rutuja","moni","vidya","shruti","aditya"]

name_all = [all_item for all_item in name ]

name_with_A = [all_item for all_item in name if "a" in all_item]
print(name_all)
print(name_with_A)

# for numbers
num = [number for number in range(11)]
print(num)

num = [number*2 for number in range(11)]
print(num)

# with condition
num = [number*2 for number in range(11) if (number%2 == 0)]
print(num)


a =[ord(i) for i in 'def']
print(a)