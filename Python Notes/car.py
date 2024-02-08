#Object Oriented Programming OOP
class Car:
    #Metodi riutilizzabili da tutti gli oggetti creati dalla classe
    def __init__(self,make,model,year,color): #construttore
        self.make = make #instance variable
        self.model= model
        self.year = year
        self.color = color

    def drive(self): 
        print("This " + self.model + " is driving") 

    def stop(self):
        print("This " + self.model + " is stopped")