#Object Oriented Programming OOP

from car import Car
car_1 = Car("Chevy", "Corvette", 2021,"blue") #creazione dell'oggetto car_1
car_2 = Car("Ford", "Mustang", 2022,"red")
car_1.drive()
car_1.stop()

#utilizzo di una variabile sulla classe
from car2 import Car
car_1 = Car("Chevy", "Corvette", 2021,"blue") #creazione dell'oggetto car_1
car_2 = Car("Ford", "Mustang", 2022,"red")
car_1.whells = 2 #sovrascrive la variabile sull'1, il 2 avrà sempre 4 della classe principale
print(car_1.wheels)
print(car_2.wheels)

#cambio di valore della variabile della classe
from car2 import Car
car_1 = Car("Chevy", "Corvette", 2021,"blue") #creazione dell'oggetto car_1
car_2 = Car("Ford", "Mustang", 2022,"red")
Car.wheels = 2 #sovrascrive il valore su tutti gli oggetti, avranno tutte e 2 il valore 2
print(car_1.wheels)
print(car_2.wheels)


#Inheritance
class Animal:

    alive = True
    
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")   

class Rabbit(Animal): #eredita tutto da animal
    def run(self): #metodo che ha solo rabbit
        print("The rabbit is running")

class Fish(Animal): #eredita tutto da animal
    pass

class Hawk(Animal): #eredita tutto da animal
    pass

#costruiamo gli oggetti
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat() #use Animal class method-> This is Inheritange, ti basta cambiare il metodo della classe animal per cambiare a tutti
hawk.sleep()
rabbit.run()#metodo definito dentro l'oggetto rabbit


# Multi Inheritance
class Organism:

    alive = True

class Animal(Organism): #eredita da Organism

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #eredita da animal
    
    def bark(self):
        print("This dog is barking")


dog = Dog() #crea l'oggetto dog
print(dog.alive)#ereditato da animal
dog.eat()#ereditato da animal
dog.bark()#metodo suo



# Multi Inheritance from more class
class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey): #eredita da prey
    pass

class Hawk(Predator): #eredita da predator
    pass

class Fish(Prey, Predator): #Eredita da due classi
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
hawk.hunt()
fish.hunt() #usa il metodo della prima classe
fish.flee() #usa il metodo della seconda classe


# Method overriding
class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self): #overriding the class method
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()


# Method chaining, calling multiple methods sequentially
class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self
    
    def brake(self):
        print("You stop on the brakes")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self
    
car = Car()
car.turn_on().drive()
car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()




# Function super(), used to give access to the methods of a parent class, returns a temporary object of a parent class when used
class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)  #riusiamo il metodo della classe madre

    def area(self):
        return self.length*self.width #metodo custom suo

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width) #riusiamo il metodo della classe madre
        self.height = height

    def volume(self):
        return self.length*self.width*self.height #metodo custom suo

square = Square(3,3) #creo gli oggetti
cube = Cube (3,3,3)
print(square.area())
print(cube.volume())



# Prevents a user from creating an object of that class and compels a user to override abstract methods in a child class
# abstract class-> class which contains one or more abstract methods
# abstract method-> method that has a declaration but doesn't have an implementation
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod #chi eredita da vehicle, dovrà poi implemnetare la funzione go e stop
    def go(self):
        pass

    @abstractmethod 
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("The car is stopping")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("The motorcycle is stopping")


#vehicle = Vehicle() can't create an object
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
motorcycle.stop()



#Pass Object as arguments
class Car:

    color = None
    
class Motorcycle:

    color = None

def change_color(car,color):

    car.color = color #metodo che cambia il colore

car_1=Car() #creazione oggetti
car_2=Car()
car_3=Car()
bike_1=Motorcycle()
change_color(car_1,"red") #passo l'oggetto come argomento del metodo
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)



# Duck typing, the class of an object is less important than the methods /attributes, class type is not checked if minimum methods/attributes are present 
# if it walks like a duck, and it quacks like a duck, then it must be a duck!
class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person():

    def catch(self,duck):
        duck.walk() #metodi di duck
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck) #runnato la funzione passandogli l'oggeto duck, gli puoi passare chicken e avvierà il metodo di chicken




# walrus operator !=, assigment espression aka walrus operator, assigns values to variables as part of a larger espression
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food) #trasformiamo queste righe con il walrus

foods = list() #lista
while food := input("What food do you like?: ") != "quit": #asegna il valore a food, e finche inserisci qualcosa che non è quit continuo il loop
    foods.append(food)

    

# Functions to variables, assign functions to variables
def hello():
    print("hello")

hi = hello
hi() #puoi assegnarlo normalmente, basta che metti la parentesi tonda in quanto funzione

#vediamo un altro caso
say = print
say("I can't believe this works!") #assegna la funzione print, poi inserisci l'argomento che richeiderebbe print




# High order function, a function that either: 1 accept a function as an argument or 2 returns a function (in python, functions are also treated as objects)
def loud(text): #accetta una stringa come argomento
    return text.upper()#ritorna un text

def quiet(text):
    return text.lower()

def hello(func): #questo ha come argomento una funzione, quindi è high order
    text = func("hello")
    print(text)#ritorna una funzione


hello(loud) #hello è high order quindi gli posso passare la funzione loud

#vediamo un altro esempio
def divisor(x):
    def dividend(y):
        return y/x
    return dividend #ritorna una funzione

divide = divisor(2) #assegnazione alla variabile di una funzione
print(divide(10)) #printa la funzione



#lambda function, function writte in 1 line using lambda keuword, accepts any number of arguments, but only has one espression. "shortcut"
def double(x):
    return x * 2

print(double(5))

#trasformiamo con lambda
double = lambda x:x *2 #la prima x è la variabile, dopo : è l'espressione
print(double(5))


#Author Xiao Li Savio Feng


