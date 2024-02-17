# Savio Feng's Python Notes


# Variables, single quotes or double quotes, the type assigned automatically
first_name = "Savio "
last_name = "Feng \n"
print(first_name + "He's an Engineer") #print variable contatenata con una stringa
print("The type of the data it's " + str(type(first_name))) #print del data type, fatto il casting str per poter concatenare
full_name= first_name + " " + last_name #concatenazione di due variabili
print(full_name) 

# Le operazioni possono essere fatte solo da dati della stessa tipologia
age = 20
age +=1
print("your age is : " +str(age)) 

# Boolean variables, per commentare ctrl +k +c
human = False
print("are you a human? " + str(human))


# Some functions
nome="Savio"
print(len(nome)) #lunghezza
print(nome.find("o")) #trova la posizione di o
print(nome.count("o")) #conta le lettere o
print(nome.capitalize()) #mostra il nome
print(nome.upper()) #maiuscolo
print(nome.isdigit()) #controlla se è un digit
print(nome.replace("o","a"))#sostituisce la lettera o con a



# type casting
x = 1 #int
y = 2.0 #float
z = "3" #stringa
y = int(y) #casting da float a int
print(y)
print("La y vale : " + str(y)) 



# funzione input()
name  = input("What's your name?: ") #assegnazione del nome digitato
age = int(input("How old are you?: ")) #il dato inserito deve essere integer 
print("Hello " + name + " pleasure to know that you are " + str(age) + ", you are so young!! ")


# import math module
import math
pi = 3.14
print(math.ceil(pi)) # per eccesso
print(math.floor(pi)) # per difetto
print((abs(pi)))
print(pow(pi,5))


# Slicing, crea una sottostringa estraendo gli elementi da un altra stringa
name ="Savio Feng"
first_name = name[6:10] #prende gli elementi dal 6 al 10, Feng
reverse_name = name[::-1] #reverse name
print(first_name)
print(reverse_name)
# with slice
sito = "https://adoisodiaofjohqrifjerr.zeta"
nome_dominio=slice(8,-5) #parte da 8 e dice dove deve finire la, cioè al quintultimo carattere, il punto
print(sito[nome_dominio])


# if statement, attento all'identazione
age = int(input( "How old are you?"))

if age >= 18:
    print("you are an adv") #se vera la condizione 
elif age < 0:
    print("You are joking bro!") #controllo il caso  negativo
else:
    print("you are a baby") # se non è vera nessuna delle condizioni


# operatori logici
temp = int(input("What's the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("ok not bad")
elif temp < 0:
    print("wow freeezing time!")
else:
    print("wow it's hot af")


# While loop
name = None
while not name: #finche non inserisci qualche nome, continua a chiedertelo
    name = input("what's your name?: ") 


# for loop
for i in range(100): #incrementa automaticamente ad ogni iterazione di 1, parte da zero
    print(i)

for i in range(50,100): #range
    print(i)

for i in range(50,100,2): #fa salti da due, conta quindi non +1 ma +2 alla volta
    print(i)

for i in "Savio code": #stampa 1 lettera alla volta
    print(i)

import time
for seconds in range(10,0,-1): #conterà da 10 a 1, il -1 serve per farlo fermare a 1 e non a 0
    print(seconds)
    time.sleep(1) #lo fai fermare per 1 secondo ad ogni ciclo, così conta al secondo
print("Happy new year!)")


# nested loops, i e j, per fare matrici o cose del genere
rows = int(input("How many rows):"))
columns =int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end ="")
    print()


#loop control statements: break "termina", continue "skippa la prossima esecuzione", pass "non fare nulla"

while True:
    name= input("Enter name: ")
    if name!="":
        break #ferma l'esecuzione quando inserisci qualcosa che non sia vuoto

phone = "123-456-7890"
for i in phone:
    if i=="-":
        continue #gli faccio skippare il print del trattino
    print(i, end="")#la parte di end lo fa scrivere tutto sulla stessa riga, cioè gli fa finire con un senza spazio


for i in range(1,21): #voglio skippare il print di 13, e printare il resto
    if i == 13:
        pass
    else:
        print(i)


#LISTE, ha un indice di partenza, possiamo sfruttarlo, il primo elemento è sempre lo zero
food = ["pizza","pasta","coca cola","sprite"]
print("All the foods are: " + str(food))
print(food[0]) #printo solo la pizza
food[1]="sushi" #sostituisco la pasta con il sushi
print (food[1])


for x in food:
    print(x,end=" ")

food.insert(4,"cake") #inserisco un elemento nella lista
food.sort() #ordino la lista alfabeticamente
print(food)



#Liste di liste
drinks = ["coffe","milk","orange","tea"]
food = ["pizza","pasta","hamburger","meat"]

eat = [drinks,food] #concatena le due liste
print(eat)
print(eat[0]) #visualizza la prima lista
print(eat[1]) #visualizza la seconda lista



#Tuple , collezione ordinata e immutabile, gruppa dati correlati
student = ("Savio", 21, "male") #anche diversi tipi
print(student.count("Savio")) #conta quanti Savio ci sono nella tupla
print(student.index("male")) #printa la posizione dell'elemento male

for x in student:
    print(x, end=" ") #printa tutti gli elementi della tupla student



#set, collezione non ordinate e senza indici, no duplicates values
utensils = {"fork","spoon","knife"}
utensils.add("napkin") #aggiunge un elemento al set
utensils.remove("fork") #elimina l'elemento fork
for x in utensils:
    print(x, end=" ")


utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}
utensils.update(dishes) #aggiorna il set dishes con gli elementi di utensils, non aggiunge i doppione, non sono ammessi
dinner_table = utensils.union(dishes) #li unisce
for x in utensils: 
    print(x, end=" ")

for x in dinner_table:
    print(x, end=" ")

print(utensils.difference(dishes)) #mostra gli elementi diversi


# Dictionary, changeable, una collezione non ordinata di unique key:value pairs. Fast because they use hashing, allow us to access a value quickly
capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}
print(capitals.keys()) #print keys
print(capitals.get('Germany')) #return None, non c'è nel nostro dizionario
print(capitals.values()) #print values
print(capitals.items()) #mostra tutti gli item, cioè le coppie chiave:valore
capitals.update({'Germany':'Berlin'}) #add in dict the item
capitals.pop('China') #remove China 

for key,value in capitals.items():
    print(key, value) #print the dict


# Index operator [], give access to a sequence's element (str,list,tuples)
name = "savio code"

if(name[0].islower()): #se il primo carattere è lower, lo mette in upper
    name=name.capitalize()
print(name)

first_name = name[0:5].upper() #in upper il nome
print(first_name)

last_character = name[-1] #il -1 identifica l'ultimo elemento
print(last_character)


# Function, a block of code which is executed only when it's called.
def hello(name): #definizione della funzione, la variabile name è dentro al contesto, fuori al suo scope puoi riusarlo
    print("Hello! " + name)

name="Savio"
hello(name) #inserisci il valore di "name"

def add(value1,value2):
    print(value1+value2)

value1=int(input("insert the first value: "))
value2=int(input("insert the second value: "))
add(value1,value2)


# Return statement, functions send python values/objects back to the caller, these values are known as the funciont's return value
def multiply(number1,number2):
    result = number1* number2
    return result

c=multiply(5,6)
print(c) 


# keyword arguments, arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments. Python knows the names of the arguments that our funcion receives
def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="Code", middle="Dude", first="Savio")


# Nested functions calls, function calls inside other function calls, innermost function calls are resolved first, returned value is used as argument for the next outer function
num = input( "Enter a positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num) #questo sarebbe il procedimento, vediamo come farlo col nested
print(round(abs(float(input("Enter a whole positive number:"))))) #versione nested


#scope, the region that a variable is recognized, the variable is only available from inside the region it is created, a global and locally scoped versions of a variable can be created
name ="Savio Feng" #global

def display_name():
    name="Code"
    print(name) #local

print(name)
display_name()



#args parameter, parameter that will pack all arguments into a tuple, useful so that a function can accept a varying amount of arguments
def add(*stuff):
    sum = 0
    stuff = list(stuff) #casting a list degli argomenti
    for i in stuff:
        sum += i
    return sum
    
print(add(4,2,6,54,7,1))


# kwargs parameter, parameter that will pack all arguments into a dictionary
def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items(): #per ogni pair key:values, vai a printarlo
        print(value, end=" ")

hello(title="Mr.",first="Savio",last="Feng",info="code")



# str.format() method that gives users more control when displaying output, use placeholder {}, ex {:b} "binary form", {:E} "Exa"
animal="Cow"
item ="moon"
print("The {} jumped over the  {} ".format(animal,item)) #PLACEHOLDER WITH {} vediamo altri modi per usarli
print("The {0} jumped over the  {1} ".format(animal,item)) #PLACEHOLDER WITH {}
print("The {animal} jumped over the  {item} ".format(animal="Cow",item="moon")) #PLACEHOLDER WITH {}
print("The {animal} jumped over the  {animal} ".format(animal="Cow",item="moon")) #PLACEHOLDER WITH {}

text = "The {} jumped over {}" #possiamo metterlo su una variabile 
print(text.format(animal,item))


# Some modules
import random
x=random.randint(1,100000) #genera random numbers in range
print(x)


import random
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)


import random
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)


# Exceptions, events detected during execution that interrupt the flow of a program
try: #controlla l'esecuzione e cattura i vari errori che potrebbero essere generati e li gestisce attraverso le except
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by:"))
    result = numerator / denominator
except ZeroDivisionError as e: #best practice mettere as e
    print(e) #printa il problema
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers!")
except Exception as e:
    print(e)
    print("something went wrong...") #non lo manda in errore, ma printa il messaggio
else:
    print("The result is: " + str(float(result)))
finally:
    print("Bye") #viene eseguita sempre questa parte del finally



#Author Xiao Li Savio Feng