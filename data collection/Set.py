#set data type is unordered 

#example for set
set1={'sanduu',24,'kandy',True,2727}
set2={'tharuu',30,'kandy',False,3232}

print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print(f"type ia{(type(set1))}")
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()


#set with methord
#data adding
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
set1.add(30)
set2.add('hello')
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()

#data update 
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
set1.update(('one','hi'))
set2.update(('two','five'))
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()

#remove data
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
set1.remove(24)
set2.remove('tharuu')
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()

#discard data
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
set1.discard(True)
set2.discard('tharuu')
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()

#pop data 
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
set1.pop()
set2.pop()
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print()




#union
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print(set1.union(set1))
print(set2.union(set1))
print()


#intersection
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print(set1.intersection(set2))
print(set2.intersection(set1))
print()

#difference
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")
print(set1.difference(set2))
print(set2.difference(set1))
print()

#delete set
set1.clear()
print(f"this is set 1 :{set1}")
print(f"this is set 2 :{set2}")

