print("Bree is tall")
#

# adding multiple numbers
def add_items(*nums):
    sum=0
    for num in nums:
        sum+=num

        print(sum)

add_items(10,12,30,12) 


# write a python function that takes two arguments
# (a and b)and returns their sum

def sum(a , b):
   sum= a + b
   return sum


print(sum (10,20) ) 

# write a python function that takes in a string as input and returns the string reversed.
def reverse(word):
    word=word[::-1]
    return word
print(reverse("motor"))

# using list comprehesion
def reverse(name):
    name=[name[i]
    for i in range (len(name)-1,-1,-1)]
    return "".join (name)
x="python"
print(reverse(x))

# converting string to list
# string=list(string)

# sorting a dictionary
my_dict={'c':3,'a':5,'d':8,'b':1}
sorted_dict=my_dict.keys()
sorted_dict=sorted(sorted_dict)
for key in sorted_dict:
    print(key, ":",my_dict[key])

#  write a function that takes a list of integers
# as inputs and returns the sum of all the integers
# in the list 
def sum_of_integers(*nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum


print(sum_of_integers(2,4,7,8,9))

# flattening a list in python
def flatten_list(a_list):
    return[item for sublist in a_list for item in sublist]
matrix=[ [1,2,3],
        [4,5,6],
        [7,8,9],
        ]
print(flatten_list(matrix))


def flatten_list(a_list):
    flat = []
    for sublist in a_list:
         for item in sublist:
             flat.append(item)
    return flat


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
 ]

flatten_list(matrix)

# write a function that take  list of integers as inputs and returns
# a new list with all even numbers removed.

def remove_even_numbers(*numbers):
    new_list=[]
    for i in numbers:
         if i % 2!=0:
             new_list.append(i)
    return i

def remove(*nums):
    new_list=[]
    for i in nums:
        if i%2!=0:
            new_list.append(i)
            return i
        
print(remove_even_numbers(3,5,6,7,8,9)) 
# finding the largest number
heights = [100, 2, 300, 10, 11, 1000]
largest_number = heights[0]
for number in heights:
    if number > largest_number:
        largest_number = number
print(largest_number) 

heights = [100, 2, 300, 10, 11, 1000]
def my_max(x, y):
    if x < y:
        return y
    else:
        return x
max_height = reduce (my_max, heights)
print(max_height)
 