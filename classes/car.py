
   
class Car:
    
    def __init__(self,model,make,registration) :
        self.model=model
        self.make=make
        self.registration=registration

        # carry people
        # autonomous packing
        # turn on lights

    def accelerate(self):
       self.accelerate=30
       return self.accelerate +self.speed
    
    
    

    def decelerate(self):
        
        self.decelerate=self.speed-self.decelerate
        return self.decelerate
    


    def car_description(self):
        return f"{self.make} cars are very expensive"
            