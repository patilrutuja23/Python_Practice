# run function on all items of collection

collection_1 = [10,20,30,40,50,60,70,80,90]
collection_2 =[]

# this is traditional way to do mapping 
for x in collection_1:
    collection_2.append(float(x))
    
print(collection_1)
print(collection_2)


# using map 
print("using map function")
coll_1 = [12,23,34,45,56,67,78,89,90]
coll_2 =list(map(str,coll_1))

print(coll_1)
print(coll_2)


print("Double the value")
double = list(map(lambda x: x*2 , coll_1))
print(double)