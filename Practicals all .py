# first practical 
#python programme to find roots of a quadratic eauation
#d=b^2-4ac
#x=(-b+-d^1/2)/2a
import cmath
a= float(input("enter the cofficient a"))
b= float(input("enter the cofficient b"))
c= float(input("enter THE COFFICIENT c"))
d=b**2-4*a*c
root1=(-b+cmath.sqrt(d))/2*a
root2=(-b-cmath.sqrt(d))/2*a
print("roots of the quadratic equation are",root1,"and",root2)


## practical 2 - WAP to accept a number 'n' to compute the following:

### a. Check if 'n' is prime or not.
#to write a progrrame to check if  number is prime lets make a function 
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

### b. Generate all prime numbers till 'n
#now a programme to generate all prime numbers upto n
def generate_prime_numbers_upto(n):
 prime_no=[]
 for i in range(2,n+1):
     if is_prime(i):
         prime_no.append(i)
 return prime_no

n=int(input("enter a number to generate prime numbers upto it"))
print(f"prime numbers upto {n}:{generate_prime_numbers_upto(n)}")

#programme to generate the first n prime numbers
def first_n_primes(n):
  primes = []
  num=2
  while len(primes)<n:
    if is_prime(num):
      primes.append(num)
    num+=1
  return primes
n=int(input("generate the first n prime numebrs"))
print(f'the first{n} prime numbers are:{first_n_primes(n)}')

### c. generate first 'n' prime numbers

n =eval(input("enter value ")) 

count = 0
number = 2
while count < n:
   for i in range(2,number):
      if number % i == 0:
       number += 1
       break
   else:
      print(number, end=',')
      count+= 1
      number+= 1

### d. calculate the summ of first 'n' natural numberws.

n =int(input("enter value ")) 
sum =0
for i in range(1,n+1):
    sum += i
print(sum)


## practical 3 - WAP to create a pyramid of the character '*' and a reverse pyramid.

def Pyramid_maker(n):
  # Pyramid
 for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("* " * i)

# Reverse Pyramid
def reverse_Pyramid(n1):
 for i in range(n, 0, -1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("* " * i)
#Number of rows for the pyramid
n=int(input("enter no of rows you want in pyramid")
n1=int(input("enter no of rows for reverse Pyramid ")
print("Pyramid:", Pyramid_maker(n))
print('reverse pyramid ',reverse_Pyramid(n1))


## practical 4 - WAP that accepts a character and performances the following.

### a. print whether the character is a letter or numeric digit or a special character.    

### b. if the character is a letter, print whether the letter is uppercase or lowercase. 

### c. if the character is numeric digit, print its name in the text.

  
charac = input("Enter the data: ")

if charac >= 'A' and charac <= 'Z':
    
   print(charac, "is an Uppercase Letter")

elif charac >= 'a' and charac <= 'z':
    
   print(charac, "is a Lowercase Letter")

elif charac >= '0' and charac <= '9':
    
   print(charac, "is a Numeric Digit")
   n = int(charac)
   
   dict= {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
    
   print(dict[n])

else:

   print(charac, "is a Special Character")   

   

   


## practical 5 - WAP to swap the first n characters of two strings .

str1 =input("enter first string ")

str2 =input("enter second string ")

n1 =int(input("enter no of characters which is to be swap: "))

n=str1[ :n1]

m=str2[ :n1]

if n1 <= min(len(str1),le(str)):
  
  print(str1.replace(n,m))

else:
  
  print(str2.replace(n,m))







## practical 6 - WAP to 

print("Enter the first string:", end="")

string1 =input()

print("Enter the second string:", end="")

string2 =input()

print("\nstring before swap: ")

print(" string1 =", string1)

print(" string2 =", string2)

temp = string1 

string1 = string2

string2 = temp

print("\nstring before swap: ")

print(" string1 =", string1)

print(" string2 =", string2)






## practical 7 - WAP to perform the following operations on a string. 

### a. find the frequency of a character in a string . 

string = "hello world to python"

character = input("enter a character ")

f=0

for i in string:

   if i ==character:
     f+=1
print("frequency of" , character ,'is', f)     




### b. replace a character by another character in a string .

string = "hello world to python"

print(string.replace ("e","i"))





### c. remove the first occurance os a character from a satring .

string = "hello world to python program"

print(string[3:len(string)])





### d. remove all the occurances of a character from a string

string = "hello world to python tutorial"

print(string[ :0])


print(string[ :2])



## practical 8 - WAP  to create a list of only the even integers appearing in the list (may have elements of other types ) using for loop and list comprehension.

def cubes():
  
  newlist =[]
  
  number = [1,3,5,2,7,4,"five"]

  for i in number:
  
   if type(i)==int:
   
     if i%2 ==0:
      
       newlist.append(i**3)
  
  print(newlist)

cubes()

## practical 9 - Write a function that accepts two streings and returns the indices of all mthe occurancesa of the second string in the first string as a list . If the second string is not present in the first string then it should return -1 .


def occurances(a,b):
  
  newlist = []

  
  if b not in a:
   
    print(-1)
 
  else:
    
    i=0
   
    while i<=len(a):
     
      c=a.find(b,i)
     
      if c== -1:
      
       break
      
      i = c+len(b)
      
      newlist.append(c)
    
    print(newlist)

a=input("enter first string; ")

b=input("enter second string; ")

occurances(a,b)



## practical 10 - Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are the cubes of the keys .

def cubes():
 
 dict={}

 for i in range (1,9):
 
   dict[i] = i**3

 print(dict)

cubes()

![Screenshot 2024-11-07 151910](https://github.com/user-attachments/as

## practical 11 - consider a tuple t1 =(1,4,6,3,2,8,5,10,9,7,6). WAP to perform the following.

### (a.)  print half the values of the tuple in one line and other half in the other next line.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

half_value=len(t1)//2

first_half = t1[ :half_value]

print("first_half" ,first_half )

second_half = t1[half_value: ]

print("second_half" ,second_half )   


### (b.) Print another tuple whose values are even numbers in a given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

even_number = tuple(filter(lambda x: x%2==0, t1))

print("tuple with even number ", even_number )



### (c.) Concatenate a tuple t2 =(12,15,11) with t1.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

t2 =(12,15,11)

concatenation= (t1 ,t2)

print("tuple with concatenation  ", concatenation )


 

### (d.) return Maximum and minimum value from this given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

print("maximum value in t1 is ", max(t1))

print("minimum value in t1 is ", min(t1))




## practical 12- WAP to accept a name from a user. Raisen and handle appropriate exception(s) if the text entered by the user contains digits and /or special characters . 

name =input("enter a name ")

try:
   
    if name.isalpha()!=%'e':
       
       print(" This is correct name ")

    else:
      
       print(" There is name error ")





## practical 13.- WAP to read a file and

### a. Print the total numbers of characters words and lines in the file.

### b. Calculate the frequency of each character in the file. Use of variable of dictionary type to maintain the count.

### c. Print the words in reverse order.

### d. Copy even lines of the file to the file named "file 1" and odd lines to another file "file 2".

def filehandling():
   
   f=open( file link,'r')
   
   data =f.read()
   
   f.close()

   words =data.split()
   
   lines =len(data.splitlines())
   
   print(" lines in the text file is:" ,lines)
   
   print(" Number of words in text file",len(words))
   
   print(" Number of characters in text file",len(data))

filehandling()

def freq():

  f =open( filelink ,'r')

  data =f.read()

  f.close()

  d ={}

  for i in data:
   
    b =data.count(i)
   
    d[i]=b

  print(d)

freq()


def reverse_words():
 
  f =open(r"file link")

  data1 =f.read()
  
  data2 =data1.split()

  reverse =data2[ ::-1]

  print(" reverse words:","".jion(reverse))

reverse_words()

def file1_and_file2():

  f =open(r"file link")

  f3 =open(r"file link")

  f4 =open(w"")

  lines =f.readlines()

  for i in range(len(lines)):

     if i%2==0:
       f3.wreite(lines[i])
  else:
    f4.write(lines[i])

  f.close()

  f3.close()

  f4.close()

  file5 =open()

  file6 =open()

  print("even lines:",file5.read())

  print("odd lines:",file6.read())

  f5.close()

  f6.close()

file1_and_file2()












  












  
