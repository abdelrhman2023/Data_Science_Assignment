def is_prime(num):
	if abs(num)==0 or abs(num)==1:
		print(f"{num} is n't prime number")
	else:
		for x in range(2,num):
			if num%x==0:
				print(f"{num} is n't prime number")
				break
		else:
			print(f"{num} is prime number")
                

def is_even(num):
	if num%2==0:
		print(True)
		print(f'{num} is even number')
	else:
		print(False)
		print(f'{num} is odd number')


def number_of_prime(number):
	counter=0
	lst=[]
	for x in range(2,1000000):
		for i in range(2,x):
			if x%i==0:
				break
		else:
			lst.append(x)
			counter+=1
		if counter == number:
			print(lst)
			break

