#using dictionary
import random

a={1:"r",2:"p",3:"s"}
c=a[random.randint(1,3)]
u=input("enter rock paper or scissor")
print("computer puts",c)

#condition
if((u=='p' and c=='r') or (u=='s' and c=='p') or (u=='r' and c=='s')):
	print("user win")

else:
	print("computer lose")









