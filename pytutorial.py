#!/usr/bin/env python
print ("Calculation software")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
symbol= raw_input("Enter a symbol (+,-,*,/): ")

if symbol in '+':
	print ("a+b=c")	
	c=a+b
elif symbol in '-':
	print ("a-b=c")	
	c=a-b
elif symbol in '*':
	print ("a*b=c")
	c=a*b
elif symbol in '/':
	print ("a/b=c")
	c=a/b
else: 
	print("Operation unknown!")
	c="unknown"
print (str("c is ")+str(c)+".")




