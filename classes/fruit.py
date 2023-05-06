class Fruit:
      def __init__(self,name,size,shape) :
        self.name=name
        self.size=size
        self.shape=shape

      def eat_fruit(self):
          return f"I love eating {self.name}"
      

      def blend_fruit(self):
          return f"I like blending {self.size} fruits"
      
      def description(self):
          return f"{self.name} is my favourite fruit"
