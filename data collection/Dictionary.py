dict1={'name':'sanduu','age':24,'city':'kandy','school':'WKCC'}

print(dict1)
print(f"type is {(type(dict1))}")
print()

#value assces 
print(dict1['name'])
print(dict1['age'])
print(dict1)
print()


#change value
dict1['city']='matale'
dict1['age']=25
print(dict1)
print()


#single data adding
print(dict1)
dict1['gender']='male'
print()


#multy data adding
print(dict1)
dict1.update({'married':False,'id':2727,'job':'student'})
print(dict1)
print()
