#list is mutable data type


#example for list    
#index of sub list   =                                          [[  0  1  2  3  4  5 ]]
list1               = [ 27,34.43,"sanduu",True,34.333332,43,"hi",[ 89,43,67,43,98,11 ]]
#index               =[ 0  1       2       3     4        5   6        7            ]
#nagetive index      =[-8 -7      -6      -5    -4       -3  -2       -1            ]    


#check data type
print (type(f"type is : {list1} ")) #check data type


#value access with index
print("###value access with index###")
print (list1[3])
print (list1[-5])
print (list1[2:-2])
print (list1[3:])
print (list1[1:5])
print (list1[1:6:2])
print (list1[::3])
print (list1[7][3])
print (list1[7][-2])
print ()



#change data
print(list1)
list1[2]="matale"
list1[-4]=37
print(list1)
print ()



#.count
print(list1)

print(list1.count("hi"))
print(list1.count(5))
print(list1.count(43))

print(list1)
print ()



#.index
print(list1)

print(list1.index("hi"))
print(list1.index(43))
print(list1.index(True))

print(list1)
print ()


#len()
print(f"len is :{(len(list1))}")
print ()

#data add
print(list1)

list1.append("hello")
list1.extend([20,34,44.44])
list1.insert(0,"start")
list1.insert(5,"mid")
list1.insert(-1,67.00)

print(list1)

#data remove 
print(list1)

list1.pop()
list1.pop(-5)
list1.remove("hello")
list1.remove(34)

print(list1)

list1.clear()
list1[:]=[]

print(list1)




