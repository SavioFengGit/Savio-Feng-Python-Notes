#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


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