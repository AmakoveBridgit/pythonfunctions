def even_numbers():
    x=range(10)
    for i in x:
        if i%2==0:
            print(i)

def even():
    x=range(20)
    for i in x:
        if i %2==0:
            print(i)

def odd_numbers():
    x=range(20) 
    for i in x:
        if i%2 !=0:
            print(i)          
odd_numbers()            

def divisible_by_five():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
    else:
        print(f"{i} is not divisible by 5") 
divisible_by_five()  

def multiple_comparison():
    x=range(50)
    for i in x:
        if i %5==0:
            print(f"{i} is divible by 5")
        elif  i%7 ==0:
            print(f"{i} is divisible by 7")
        elif i % 9==0:
            print(f"{i} is divible by 9") 
        else:
            print(f"{i} is not divible by 5,7 or 9")        
multiple_comparison() 

def odd_or_even():
    x=range(20)
    for i in x:
        if i% 2==0 and i%3==0:
            print(f"{i} is divible by both 2 and 3")
        elif i % 2==0 or i%3==0:
            print(f"{i} is divible by either 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3") 
odd_or_even()   

def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1
        
def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break


def continue_statement():
    x=0
    while x<=10:
        x+=1
        if x % 3==0:
            continue
        print(x)

# ASSIGNMENT
# Write a function that uses while, if and continue statements 
# to print all the even numbers between 0 and 50. 

def all_even_numbers():
    x=0
    while x<50:
        x+=1
        if x% 2!=0:
            continue
        print(x)
all_even_numbers()        

# Write a function that takes an integer argument and 
# prints "Prime" if the number is prime, and "Not prime" 
# if the number is not prime.
def prime_number():
    x= 25
    if x>1:
       for i in range(2,int(x/2)+1): 
          if x%i==0:
             print(x,"is Not Prime")
         
    else:
        print(x ," is Prime")    
prime_number()             

    

# Write a function that takes a list of integers as input and prints 
# the sum of all the even numbers in the list.
def list_of_integers():
    x=range(30,50)
    sum=0
    for i in x:
        if i % 2==0:
            print(sum)
            sum=sum+i    
        else:
            print("nums")    
        
    print(sum)
    avg=sum/len(x)

list_of_integers()        



# Write a function that takes any two integers as input, and prints 
# the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_numbers(a,b):
    sum=0
    for i in x:
         if i% 3==0:
              print(sum)
            

         else:
            print("number")    
            sum=sum+i
            print(sum)
print(sum_numbers(10,20)) 





for num in range(3,9):
    if num ==5:
      continue
    else:
      print(num)
num=range(1,15)  
sum=0
for i in num:
    sum=sum+i
    print(sum)

x=["Bridgit","Anna","Janekioo","Meghan"] 
longest=max(x,key=len)  
print(longest) 


def check(a,c):
    b=a is "a"
    print (b)
    d="a" is c
    print(d)

check("a","laice")



# write  a python function named divisible-by-seven that uses range function for loop and a 
# for loop to return a list containing all the numbers between 100 and 200 that are divisible by 7

def divisible_by_seven():
    # x=range(100,200)
    empty=[]
    # for i in x:
    for i in range(100,200) : 
        if i %7==0:
            empty.append(i)
    return empty
print(divisible_by_seven())


# empty=[i for i in x if i % 7==0]
# return empty

# using for loop calculate the average of a list in a range of 55:100
def calc_avg():
    x=range(55,100)
    sum=0
    for i in x:
        sum=sum+i

    avg=sum/len(x) 
    return avg   
print(calc_avg())
def get_avg():
    sum =0
    for i in range(55,100):
        sum=sum +i
        avg=sum/ len(range(55,100))
        return avg



def reverse():
  x=range(30,1,-1)
  for i in x:
    print(i)        
reverse()

text="hello world"
print(text.split("l"))
# using a while loop print numbers  prime numbers from 1-10
def primeNum(num):
    if num <2:
        return False 
    for i in range(2,num):
        if (num % i)==0:
            return False
    return True
num=0
while (num<=10):
    if primeNum(num):
        print(num)
    num+=1

    # write a python function that takes argument as a list a=[2,4,6,8]
    # and remove the secondlast item from that list and returns the whole list without removed item.



    # write a python programe that has a list days=["Monday","tuesday","Friday"."Monday"]
    # and counts the number occurences of monday
    
# def count_ocurrences():
#     days=["Monday","tuesday","Friday","Monday"]
#     my_days=days.count("Monday")
#     print(my_days)
# count_ocurrences()   
days=["Monday","tuesday","Friday","Monday"]
print(days.count("Monday"))


    # write a python program that takes in a list of cars ,cars=["Ford","BMW","volvo"]
    # and returns a sorted list
 
    # # myList= cars.sort()
    # myList=sorted(cars)
  
    # print(myList)

def sortItems():
    cars=["Ford","BMW","Volvo"]
    myList=cars.sort()
    print(myList)
print(sortItems())



# write a python function that takes one argument which is a list,a=[1,2,3,4,5]
# and return true if 4 is present in te list and false is 4 is not in the list
def find_item():
    list =[1,2,3,4,5]
    for i in list:
        if list ==4:
            print("4 is found")
   






# check if a number is divisible by both 2 and 3
def divisible():
    for i in range(0,51):
        if i %2==0 and i %3==0:
            print("divisible by both")
        elif i%2==0 or i % 3== 0:
            print("divisible by either 2,3")  
        else:
            print("not divisible by any")    
divisible()  


# add the sum of numbers in the range
def sum_all():
    sum=0
    x=range(10)
    for i in x:
        sum=sum+ i
    print(sum)
sum_all() 

# write a python programme to check if its a year is leap year or not
months=[0,31,28,31,30,31,30,31,31,30,30,31]
def is_leap(year):
    return year %4==0 and (year %100!=0 or year %400==0)

print(is_leap(2017))
# check if a months is a leap year
def month_is_leap(year,month):
    if not 1<=month<=12:
        return "Invalid month"
    if month==2 and is_leap(year):
        return 29
    return month_is_leap[month]
print(month_is_leap(2022,2))


# checking if ids are the same
a=[2,3,4]
b=[2,3,4]
print (a is b)
