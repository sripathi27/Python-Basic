'''
The if-else statement is used to execute both the true part and the false part of
a given condition. If the condition is true, the if block code is executed and
if the condition is false, the else block code is executed.

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

x,y,z=10,10,20

#if
print("if")
if x==y:
    print("x is equals to y ")

if x!=z:
    print("x is not equals to z ")

if z>x:
    print("z Greater than to x ")

if x<z:
    print("x Less than to z ")


if x>=y:
    print("x is Greater than or equal to y ")


if x<=y:
    print("x is Less than or equal to y ")

print()
print()


#if else 
print("if else")
if x==y:
    print("x is equals to y ")
else:
     print("x is not equals to y ")

print()
print()

if x==z:
    print("x is equals to y ")
else:
     print("x is not equals to y ")

print()
print()


#if else and elif
print("if else and elif")
if x==z:
    print("x is equals to z ")
elif z<x:
    print("z Less than to x ")
elif x>z:
    print("x Greater than to z ")
elif z>x:
    print("z Greater than to x ")
else:
     print(" ERROR ")

print()
print()

#with AND
print("with AND")
if x==y and y>z :
    print("1st conditions is true")
elif x!=z and y<z :
    print("2nd conditions is true")
else: 
    print("both are false")
print()
print()

#with OR 
print("with OR")
if x==y or y>z :
    print("1st conditions is true")
elif x==z or y<z :
    print("2nd conditions is true")
else: 
    print("both are false")
print()
print()

#with NOT 
print("with NOT")
if not y>z :
    print("1st conditions is true")
elif not z>y :
    print("2nd conditions is true")
else: 
    print("both are false")
print()
print()


#Nested If
print("Nested If")
if x<y:
    print("go to 1st nested is")
    if x==y:
        print("1st nested true")
    else :
        print("1st nested false")
elif x!=z:
    print("go to 2st nested is")
    if x==y:
        print("2nd nested true")
    else :
        print("2nd nested false")
else:
    print("ERROR")
print()
print()


#pass
"""if statements cannot be empty, but if you for some 
reason have an if statement with no content, 
put in the pass statement to avoid getting an error."""
print("pass")

if z > y:
    pass
