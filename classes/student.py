class Student:
   first_name="Bridgit"
   last_name="Amakove"
   age=23
   school="AkiraChix"
country="Kenya" 


   

    # Instance variables

class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country) :
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        # Methods are used to add behaviours to a class.
        # Adding methods to a class
    def _init_(self,name,age,country):
       self.name=name
       self.age=age
       self.country=country     

    def greet_student(self): 
        # methods
        return f"Hello {self.first_name},from {self.country}.Welcome to {self.school} " 
      

    def greet(self):
       return f"Hello {self.name}"
    def show_full_name(self):
      return f"{self.first_name}{self.last_name}"
      

    def year_of_birth(self):
      self.current_year=2023
      return self.current_year-self.age
      return self.current_year-self.age
    
    
 

    
    def show_initials(self):
        return f"{self.first_name[0]}{self.last_name[0]}"
        return f"{self.first_name[0]}{self.last_name[0]}"
       

 
    
      
     


        