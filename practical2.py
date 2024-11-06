#to write a progrrame to check if  number is prime,generate all prime numbers and generate first n prime numbers
#to check if n is prime
def is_prime(n):
  if n <=1:
   return False
  for i in range(2,int(n**0.5)+1):
    if n%i ==0:
      return False
  else:  
     return True      
n=int(input("enter a number"))
if is_prime(n):
 print(f"{n} is prime")
else:
  print(f"{n} is not prime")
