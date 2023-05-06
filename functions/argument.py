def birth(name,age):
    year=2023-age
    print(f"Hello {name},you were born in {year}")
def my_country(country="kenya"): 
    print(f"Hello you are from {country}")
def hello(*names):
    for name in names:
        print(f"Hello {name}")
def sum(num):
    answer=0
    for num in nums:
        answer+=num
    return answer
def multiply_many(**kwargs):
    answer=1
    for num in kwargs.values():
        answer*=num
    return answer

def multiply(**kwargs):
    answer=1
    for num in kwargs.values():
        answer*=num
        return answer


    
    # A function named concatenate_args that takes any 
    # number of string arguments in positional arguments 
    # format and concatenates them into a single string
def concatenate_args(*names):
     my_name=""
     for name in names:
        my_name+=name
     return my_name

# A function named concatenate_kwargs that takes any 
# number of string arguments in keyword arguments  format 
# and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    my_name=""
    for name in kwargs.values():
        my_name+=name
    return my_name

def concat(**names):
    for name in names.values():
        print(name)


concat(a="Bree",b="Breaye",c="Brenda")   

def demo(name,age):
    print(name,age)

demo("Bree",20)

def my_name(*args):
    for i in args:
        print(i)
my_name(20,30,50,40)  


def my_name(**kwargs):
    for n in kwargs.values():
        print(n)
my_name(a=20,b=30,c=20,d=10)        
    
# list1=[10,12,13,14,12,15,16]
# list2=[12,10,13,29,14,15]
# list=list1.intersection(list2)
# print(list)

def common_items(a,b):
    a_set=set(a)
    b_set=set(b)
    if len(a_set.intersection(b_set))>0:
        return(a_set.intersection(b_set))
    else:
        return("no common numbers")
a=[5,6,7,8,9] 
b=[6,7,3,10,12,5] 
print(common_items(a,b))  