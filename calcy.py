#calcy program
x=int(input("enter value of x is"))
y=int(input("enter value of y is"))
o=input("what do you want to do?+,-,*,/:")

#defining addition
def add():
	return x+y

#defining substitution	
def sub():
	return x-y	 

#defining multiplication
def mult():
	return(x*y)

#defining division
def divide():
	return x/y	

if(o=='+'):
	res=add()
elif(o=='-'):
	res=sub()
elif(o=='*'):
	res=mult()
elif(o=='/'):
	res=mult()

print(res)					


