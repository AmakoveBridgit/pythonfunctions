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

    
    
