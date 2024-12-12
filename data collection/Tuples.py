#tuple is immutable data type


#example for tuples    
#index of sub tuple  =                                          (( 0  1  2  3  4  5 ))
tuple1               = (27,34.43,"sanduu",True,34.333332,43,"hi",(89,43,67,43,98,11))
#index               = (0  1       2       3     4        5   6        7            )
#nagetive index      =(-8 -7      -6      -5    -4       -3  -2       -1            )    


#check data type
print (type(tuple1)) #check data type


#value access with index
print (tuple1[3])
print (tuple1[-5])
print (tuple1[2:-2])
print (tuple1[3:])
print (tuple1[:3])
print (tuple1[7][3])
print (tuple1[7][-2])


#Tuple Method
#.count
print(tuple1.count("hi"))
print(tuple1.count(5))
print(tuple1.count(43))

#.index
print(tuple1.index("sanduu"))
print(tuple1.index(43))
print(tuple1.index(True))

#Tuple convert 