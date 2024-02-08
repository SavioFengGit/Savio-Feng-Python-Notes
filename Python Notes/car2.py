#Object Oriented Programming OOP
class Car:

    wheels = 4 #class variable

    #Metodi riutilizzabili da tutti gli oggetti creati dalla classe
    def __init__(self,make,model,year,color): #construttore
        self.make = make #instance variable, unique value
        self.model= model
        self.year = year
        self.color = color

