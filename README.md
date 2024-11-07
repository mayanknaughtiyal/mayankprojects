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



### b. Generate all prime numbers till 'n'

Code =

n= int(input("enter value")) 

for num in range(1,n): 
  
 if num > 1: 
   
  for i in range (2, num): 
       
   if num % i == 0: 
      
    break

 
  else: print(num, end=',')


Output enter value 100 2,3,5,7,11,13,17,19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,79,83,89,97,

![IMG-20241106-WA0007](https://github.com/user-attachments/assets/fa5f115c-003a-4b6a-a5e6-e5da76402c89)

![IMG-20241106-WA0006](https://github.com/user-attachments/assets/34b98eb9-3093-485d-b684-01582cbdeccd)

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

![Screenshot 2024-11-07 131319](https://github.com/user-attachments/assets/019f4a6a-8baf-4254-ae80-0cc8b9ba443f)


### d. calculate the summ of first 'n' natural numberws.

n =eval(input("enter value ")) 
sum =0
for i in range(1,n+1):
    sum += i
print(sum)


![Screenshot 2024-11-07 132054](https://github.com/user-attachments/assets/262fb515-ef5b-405d-bd72-167353996637)




## practical 3 - WAP to create a pyramid of the character '*' and a reverse pyramid.



def print_pyramid(n):
   
   for i in range(n):
     
     print(' ' * (n - i - 1), end='')
     
     print('*' * (2 * i + 1))

#Number of rows for the pyramid
rows = 5

print("Pyramid:")

print_pyramid(rows)


def print_reverse_pyramid(n):
   
   for i in range(n, 0, -1):
    
     print(' ' * (n - i), end='')
    
     print('*' * (2 * i - 1))

#Number of rows for the reverse pyramid
rows = 5

print("\nReverse Pyramid:")

print_reverse_pyramid(rows)

![IMG-20241106-WA0009](https://github.com/user-attachments/assets/00f62032-1d63-4650-902e-1fa292b5f22f)

![IMG-20241106-WA0008](https://github.com/user-attachments/assets/88de3a7a-4f38-4621-a542-bd7bed445a53)





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

   
![IMG-20241106-WA0011](https://github.com/user-attachments/assets/532abd9e-cfa7-4fd0-aa49-4ac96f3a142f)


![IMG-20241106-WA0010](https://github.com/user-attachments/assets/af3bf10a-22b0-41d2-bb60-c8e6d3c881b9)
    
   


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


![image](https://github.com/user-attachments/assets/48b4bf0b-3c93-458d-8906-9df8854dfe5d)





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



![IMG_20241106_115748_028](https://github.com/user-attachments/assets/bac06745-7b54-4056-84ee-a461fb68ec19)



## practical 7 - WAP to perform the following operations on a string. 

### a. find the frequency of a character in a string . 

string = "hello world to python"

character = input("enter a character ")

f=0

for i in string:

   if i ==character:
     f+=1
print("frequency of" , character ,'is', f)     

![Screenshot 2024-11-07 112630](https://github.com/user-attachments/assets/965af336-aee9-43b1-885f-93e89f10e10f)



### b. replace a character by another character in a string .

string = "hello world to python"

print(string.replace ("e","i"))


![Screenshot 2024-11-07 113427](https://github.com/user-attachments/assets/5480e2ce-5bf2-48cf-98c9-c3da63472fec)



### c. remove the first occurance os a character from a satring .

string = "hello world to python program"

print(string[3:len(string)])

![Screenshot 2024-11-07 114106](https://github.com/user-attachments/assets/64a834c4-7768-4cf8-93a3-5ab1705db93e)



### d. remove all the occurances of a character from a string

string = "hello world to python tutorial"

print(string[ :0])

![Screenshot 2024-11-07 114402](https://github.com/user-attachments/assets/636c507d-7afc-4e33-ae1c-4fe52059df51)


print(string[ :2])


![Screenshot 2024-11-07 114538](https://github.com/user-attachments/assets/9df7d84a-bd5e-4c58-a7f0-028ada7db6bb)


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

![Screenshot 2024-11-07 132054](https://github.com/user-attachments/assets/262fb515-ef5b-405d-bd72-167353996637)

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


![Screenshot 2024-11-07 150130](https://github.com/user-attachments/assets/b0a92e87-cc70-4513-859f-82c72f08e04f)


## practical 10 - Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are the cubes of the keys .

def cubes():
 
 dict={}

 for i in range (1,9):
 
   dict[i] = i**3

 print(dict)

cubes()

![Screenshot 2024-11-07 151910](https://github.com/user-attachments/assets/0aee5bdc-285f-4723-b396-0b4ca85f8824)


## practical 11 - consider a tuple t1 =(1,4,6,3,2,8,5,10,9,7,6). WAP to perform the following.

### (a.)  print half the values of the tuple in one line and other half in the other next line.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

half_value=len(t1)//2

first_half = t1[ :half_value]

print("first_half" ,first_half )

second_half = t1[half_value: ]

print("second_half" ,second_half )   

![Screenshot 2024-11-07 153337](https://github.com/user-attachments/assets/ec1f42c5-a0cd-45bf-8ddc-6f698f086fc3)

### (b.) Print another tuple whose values are even numbers in a given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

even_number = tuple(filter(lambda x: x%2==0, t1))

print("tuple with even number ", even_number )

![Screenshot 2024-11-07 154105](https://github.com/user-attachments/assets/9047ffe3-d839-4ad8-a6d2-101b85dd11f8)


### (c.) Concatenate a tuple t2 =(12,15,11) with t1.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

t2 =(12,15,11)

concatenation= (t1 ,t2)

print("tuple with concatenation  ", concatenation )

![Screenshot 2024-11-07 154606](https://github.com/user-attachments/assets/96394980-9de9-4dc6-8954-ecdb623c90f3)

 

### (d.) return Maximum and minimum value from this given tuple.

t1 =(1,4,6,3,2,8,5,10,9,7,6)

print("maximum value in t1 is ", max(t1))

print("minimum value in t1 is ", min(t1))

![Screenshot 2024-11-07 154955](https://github.com/user-attachments/assets/5c9ba36f-bad3-4374-a3bc-d32ac27fe950)



## practical 12- WAP to accept a name from a user. Raisen and handle appropriate exception(s) if the text entered by the user contains digits and /or special characters . 

name =input("enter a name ")

try:
   
    if name.isalpha():
       
       print(" This is correct name ")

    else:
      
       raise Exception(" There is name error ")

except Exception as e:
   
    print(e)


![Screenshot 2024-11-07 160028](https://github.com/user-attachments/assets/885f035d-3ac5-4d56-8518-6d2193b98f8a)

![Screenshot 2024-11-07 160243](https://github.com/user-attachments/assets/a9864f28-1803-46bc-9098-31097e2e6b2f)


## practical 13.- WAP to read a file and

### a. Print the total numbers of characters words and lines in the file.

### b. Calculate the frequency of each character in the file. Use of variable of dictionary type to maintain the count.

### c. Print the words in reverse order.

### d. Copy even lines of the file to the file named "file 1" and odd lines to another file "file 2".

def filehandling():
   
   f=open( https://github.com/khushveerk/Python-code-/blob/main/khushveer%20file2.txt,'r')
   
   data =f.read()
   
   f.close()

   words =data.split()
   
   lines =len(data.splitlines())
   
   print(" lines in the text file is:" ,lines)
   
   print(" Number of words in text file",len(words))
   
   print(" Number of characters in text file",len(data))

filehandling()

def freq():

  f =open( https://github.com/khushveerk/Python-code-/blob/main/khushveer%20file2.txt ,'r')

  data =f.read()

  f.close()

  d ={}

  for i in data:
   
    b =data.count(i)
   
    d[i]=b

  print(d)

freq()


def reverse_words():
 
  f =open("https://github.com/khushveerk/Python-code-/blob/main/khushveer%20file2.txt")

  data1 =f.read()
  
  data2 =data1.split()

  reverse =data2[ ::-1]

  print(" reverse words:","".jion(reverse))

reverse_words()

def file1_and_file2():

  f =open(r"https://github.com/khushveerk/Python-code-/blob/main/khushveer%20file2.txt")

  f3 =open(w"https://github.com/khushveerk/Python-code-/blob/main/khushveer%20file%203.txt")

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












  












  
