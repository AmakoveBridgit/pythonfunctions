def is_password(*word):
    #  word="Password"
     if word=="password":
          print("correct")
     else:
          print("Not correct")     
is_password("word")  

# python programme to find the common element
a=[1,2,7,4,5] 
b=[5,5,7,9] 
def common(a,b):
     a_set=set(a)
     b_set=set(b)

     if(a_set & b_set):
          print(a_set & b_set)
     else:
          print("No common number")
common(a,b)  

# finding a number
nums=[1,2,3,4,5]
for num in nums:
    if num==3:
         print("found")
         continue
     
    print(num)


# checking if ids are the same
a=[2,3,4]
b=[2,3,4]
print (a is b)

print(id(a))
print(id(b))
print (a is b)

# empty dictionary  dictionaries are mutable
my_dictionary={}  
print(my_dictionary)
# you can also use the dict() or fromkeys()
cities=('paris','athens','madrid')
continent='europe'
my_dictionary=dict.fromkeys(cities,continent)
print(my_dictionary)

     #  acess individual item in a dictionary
my_info={'name':'abakuk','age':23,'location':'kenya'}  
print(my_info['location'])

# updating items in a dictionariy
my_info.update(name='tedy',age=30,occupation='developer')
print(my_info)

# deleting items 
del my_info['age']
print(my_info)