"""
print function is use for somthing disply on terminal
len function is use for calculate eliment in string,list or somthing's have
"""


#how to print somethig
print("hello world")
print(1234)

#variable and variable assignment
text="hello"
number=1234
desi=123.4

print(text)
print(number)
print(desi)

x=y=z=10 
X,Y,Z=10,15,20
print(x,y,z,X,Y,Z)


#Python is a case-sensitive language and len function
city="kandy"
City="matale"
citY="nuwaraeli"

print(city,"for letters",(len(city)))
print(City,"for letters :",(len(City)))
print(citY,"for letters :",(len(citY))) 

#normal
print("hello world")

#\n new line
print("hello \n world")

#Carriage return 
print("hello\rworld")

#tab space 
print("hello\tworld")

#back space
print("hello\bworld")

#how to print ' using \
print("hello i\'m sripathi udayakantha.")

#somthing print with combined data types
name='sripathi'
age=24
print(f"meth 1 : may name is {name} and i\'m {age} years old.")
print("meth 2 : my name is {} and i\'m {} years old.".format(name,age))
print("meth 3 :my name is %s and i\'m  %d years old"%(name,age))
