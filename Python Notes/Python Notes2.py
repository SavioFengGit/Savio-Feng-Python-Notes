#Savio Feng's Python Notes2

# File detection
import os
path = "C:\\Users\\..."

if os.path.exists(path): 
    print("That locationExists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("That location doesn't exists!")


# Read the content of a file, use name if same folder or path
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found! ")
# print(file.close) #check if closed, they probably automatically closed for u


# open the file and write on it, overwrite all
text= "Write it! \n"
with open('test.txt','w') as file: #open with write mode
    file.write(text)


# open the file and write on it, append the text
text= "Write it! \n"
with open('test.txt','a') as file: #open with write mode
    file.write(text)

# copying files: copyfile() "copies contents of a file", copy() "copyfile() + permission mode + destination can be a directory", copy2() "copy() + copies metadata"
import shutil
shutil.copyfile('test.txt','copytest.txt') #src and dst


# move files or folder
import os

source = "Path"
destination = "Path"

try:
    if os.patth.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + "was not found")


# delete files or folder
import os
path='test.txt'

try:
    os.remove(path) # os.rmdir(path) delete the folder
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You don't have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + "was deleted")


# some modules
import messages as msg
msg.hello()
msg.bye()

from messages import hello,bye
hello()
bye()

help("modules") #trova tutti i moduli che hai

# sort() method   = used with lists
# sort() function = used with iterables
students = [("Squidward", "F", 60), #nome, voto e età
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

grade = lambda grades:grades[1] #assegna a grade la posizione 1 cioè il voto
# students.sort(key=grade) questo va a ordinare per grade, ma andiamo a usare la funzione sorted
sorted_students = sorted(students,key=grade) # sorts and creates a new list, attraverso la funzione sorted

for i in sorted_students: #printa gli studenti ordinati per voto
    print(i)




# map() =   applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82) #conversione in euro 
to_dollars = lambda data: (data[0],data[1]/0.82) #conversione in dollari
store_euros = list(map(to_euros, store)) #applica la conversione in euro a tutto lo store

for i in store_euros:
    print(i)



# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18 #applica la condizione di maggiore età dopo i : e seleziona solo quelli consoni
drinking_buddies = list(filter(age, friends)) #filtra tutti i minorenni, lo applica ad ogni elemento di friends

for i in drinking_buddies:
    print(i)


# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"] #riduciamo questo in un solo elemento unito
word = functools.reduce(lambda x, y,:x + y,letters) #come primo argomento applico l'uonione e come secondo l'iterable
print(word)

factorial = [5,4,3,2,1] #esempio col fattoriale
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)


# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)



# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# def check_temp(value):
    # if value >= 70:
        # return "HOT"
    # elif 69 >= value >= 40:
        # return "WARM"
    # else:
        # return "COLD"

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)





# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]
# --------------------------------------
users = list(zip(usernames,passwords))

for i in users:
    print(i)
# --------------------------------------
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+" : "+value)
# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)




#Time module
import time
#*************************************************************************
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                       epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time

#*************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

#*************************************************************************
# time.strptime(time_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

#*************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

#*************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)




# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading
#facciamo partire 3 thread in parallelo 
import threading
import time
#creazione di tre funzioni
def eat_breakfast():
    time.sleep(3) #pausa di 3 secondi
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")
#creazione di 3 oggetti di tipo thread, assegnando una funzione da eseguire come target e una tupla vuota come args
x = threading.Thread(target=eat_breakfast, args=())
x.start() #avvia il thread

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()
#Aspetto che i tre thread terminino usando il metodo join, che blocca il thread principale finché il thread a cui è applicato non finisce.
x.join()
y.join()
z.join()

print(threading.active_count()) #stampa il numero di thread attivi
print(threading.enumerate()) #stampa la lista dei thread attivi
print(time.perf_counter()) #stampa il tempo di esecuzione



# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

#funzione timer che stampa il tempo trascorso da quando è stato avviato il thread
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True) #daemon identifica che il thread finirà automaticamente quando il thread principale terminerà
x.start()

# x.setDaemon(True)
# print(x.isDaemon())
answer = input("Do you wish to exit?") #premendo un tasto si fermerà






#Author Xiao Li Savio Feng