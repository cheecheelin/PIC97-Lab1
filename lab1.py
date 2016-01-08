#write a function to determine whether a number is prime \
import math
def isprime(x):
	if x<=1:
		return "false"
	elif x==2:
		return "true"
	elif x%2==0:
		return "false"
	else:
		divisor=3
		upperlimit=math.sqrt(x)+1
		while (divisor<=upperlimit):
			if x%divisor==0:
				return "false"
			divisor+=2
		return "true"
			
		
#write a function to find all the prime numbers between 0 and x 
	#modify it to work for between x and y 
	#modify it to store all the values in a list 

			
def isprimelist(x):
	primelist=[]
	for i in range(0,x):
		if isprime(i)=="true":
			primelist.append(i)
	return primelist


print isprime(257)
print isprime(10)
print isprime(144)
print isprimelist(100)
