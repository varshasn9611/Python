import random
a=['r','p','s']
v1=0
v2=0
while(True):
	p=input("your choice r/p/s: ")
	c=random.choice(a)

	print("your choice" ,p,"computer choice",c)

	if((p=='r'or p=='p'or p=='s'):
		if(p==c):
			print(tie)
		elif((p=='r' and c=='p') or (p=='p' and c=='s') or (p=='s' and c=='r')):
			v1=v1+1
			print("computer won",v1,"times")
		else:
			v2=v2+1
			print("u won", v2,"times")
	else:
		print("give proper input")
		break
		if(v1==4 or v2==3):
			if(v1==4):
				print("I'M sorry,computer won the game")
			else:
				print("congrats u won against computer, have a great day")
			break	

	
		