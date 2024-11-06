#to write a progrrame to check if  number is prime,generate all prime numbers and generate first n prime numbers
#to check if n is prime
def is_prime(n):
  if n <=1:
   return False
  for i in range(2,int(n**0.5)+1):
    if n%i ==0:
      return False  
 return True      
n=int(input("enter a number"))
if is_prime(n):
 print(f"{n} is prime")
else:
  print(f"{n} is not prime")
#now a programme to generate all prime numbers upto n
def generate_prime_numbers_upto(n):
 prime_no=[]
 for i in range(2,n+1):
     if is_prime(i):
         prime_no.append(i)
 return prime_no

n=int(input("enter a number to generate prime numbers upto it"))
print(f"prime numbers upto {n}:{generate_prime_numbers_upto(n)}")
