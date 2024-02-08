# Creazione di una finestra
from tkinter import *

window = Tk() #crea un'istanza di una finestra
window.geometry("860x560") #imposta le dimensioni della finestra in pixel
window.title("First GUI program")

icon = PhotoImage(file="logo.png")#carica un'immagine da un file
window.iconphoto(True,icon) #imposta l'icona della finestra con l'immagine
window.config(background="#5cfcff") #imposta il colore di sfondo della finestra
window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi




# Creazione di un’etichetta (label) che mostra un testo e un’immagine all’interno di una finestra
# label = un widget di area che contiene testo e/o un'immagine all'interno di una finestra
from tkinter import * #importa tutti i moduli di tkinter
window = Tk() #crea un'istanza di una finestra
photo = PhotoImage(file='mario.png') #carica un'immagine da un file

label = Label(window, #crea un'etichetta nella finestra
              text="Hi! I'm Super MARIO!!!!!", #imposta il testo dell'etichetta
              font=('Arial',40,'bold'), #imposta il tipo, la dimensione e lo stile del carattere
              fg='#00FF00', #imposta il colore del testo
              bg='black', #imposta il colore di sfondo dell'etichetta
              relief=RAISED, #imposta l'effetto 3D dell'etichetta
              bd=10, #imposta la larghezza del bordo dell'etichetta
              padx=20, #imposta lo spazio orizzontale tra il testo e il bordo
              pady=20, #imposta lo spazio verticale tra il testo e il bordo
              image=photo, #imposta l'immagine da mostrare nell'etichetta
              compound='bottom') #imposta la posizione dell'immagine rispetto al testo
label.pack() #posiziona l'etichetta nella finestra
#label.place(x=0,y=0) #posiziona l'etichetta in una posizione specifica 

window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi




#Creazione di un pulsante (button) che incrementa e stampa un contatore ogni volta che viene cliccato
from tkinter import * #importa tutti i moduli di tkinter

# button = cliccandolo, fa qualcosa

count = 0 #inizializza una variabile globale count a zero

def click(): #definisce una funzione chiamata click
    global count #dichiara count come variabile globale
    count+=1 #incrementa count di uno
    print(count) #stampa il valore di count

window = Tk() #crea un'istanza di una finestra

photo = PhotoImage(file='mario.png') #carica un'immagine da un file
window.geometry("460x360")
button = Button(window, #crea un pulsante nella finestra
                text="Click on Mario Face!!!!", #imposta il testo del pulsante
                command=click, #imposta la funzione da chiamare quando il pulsante viene cliccato
                font=("Comic Sans",30), #imposta il tipo, la dimensione e lo stile del carattere
                fg="#00FF00", #imposta il colore del testo
                bg="black", #imposta il colore di sfondo del pulsante
                activeforeground="#00FF00", #imposta il colore del testo quando il pulsante è attivo
                activebackground="black", #imposta il colore di sfondo quando il pulsante è attivo
                state=ACTIVE, #imposta lo stato del pulsante a attivo
                image=photo, #imposta l'immagine da mostrare sul pulsante
                compound='bottom') #imposta la posizione dell'immagine rispetto al testo
button.pack() #posiziona il pulsante nella finestra

window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi







# Creazione una casella di controllo (checkbox) che mostra un testo e un’immagine e che stampa una frase a seconda dello stato della casella.
from tkinter import *
def display(): #definisce una funzione chiamata display
   if(x.get()): #se il valore della variabile x è True
       print("I like Python") #stampa "I like Python"
   else: #altrimenti
       print("I don't like Python") #stampa "I don't like Python"

window = Tk() #crea un'istanza di una finestra

x = IntVar() #crea una variabile di controllo di tipo intero

python_photo = PhotoImage(file="python.png") #carica un'immagine da un file

checkbox = Checkbutton(window, #crea una casella di controllo nella finestra
                      text='Python', #imposta il testo della casella
                      variable=x, #imposta la variabile di controllo associata alla casella
                      onvalue=True, #imposta il valore da assegnare alla variabile quando la casella è selezionata
                      offvalue=False, #imposta il valore da assegnare alla variabile quando la casella è deselezionata
                      command=display, #imposta la funzione da chiamare quando la casella cambia stato
                      font=('Arial',20), #imposta il tipo, la dimensione e lo stile del carattere
                      fg='#00FF00', #imposta il colore del testo
                      bg='#000000', #imposta il colore di sfondo della casella
                      activeforeground='#0000FF', #imposta il colore del testo quando la casella è attiva
                      activebackground='#000000', #imposta il colore di sfondo quando la casella è attiva
                      padx=25, #imposta lo spazio orizzontale tra il testo e il bordo
                      pady=10, #imposta lo spazio verticale tra il testo e il bordo
                      width=800, #imposta la larghezza della casella in pixel
                      height=300, #imposta l'altezza della casella in pixel
                      anchor='w', #imposta l'allineamento del testo a sinistra
                      image=python_photo, #imposta l'immagine da mostrare sulla casella
                      compound='left') #imposta la posizione dell'immagine rispetto al testo
checkbox.pack() #posiziona la casella nella finestra

window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi







# Creazione una casella di controllo (checkbutton) che mostra un testo e un’immagine e che stampa una frase a seconda dello stato della casella.
from tkinter import * #importa tutti i moduli di tkinter

def display(): #definisce una funzione chiamata display
    if(x.get()==1): #se il valore della variabile x è 1
        print("You agree!") #stampa "You agree!"
    else: #altrimenti
        print("You don't agree :(") #stampa "You don't agree :("

window = Tk() #crea un'istanza di una finestra

x = IntVar() #crea una variabile di controllo di tipo intero

python_photo = PhotoImage(file='python.png') #carica un'immagine da un file

check_button = Checkbutton(window, #crea una casella di controllo nella finestra
                           text="I agree to learn Python!!!", #imposta il testo della casella
                           variable=x, #imposta la variabile di controllo associata alla casella
                           onvalue=1, #imposta il valore da assegnare alla variabile quando la casella è selezionata
                           offvalue=0, #imposta il valore da assegnare alla variabile quando la casella è deselezionata
                           command=display, #imposta la funzione da chiamare quando la casella cambia stato
                           font=('Arial',20), #imposta il tipo, la dimensione e lo stile del carattere
                           fg='#00FF00', #imposta il colore del testo
                           bg='black', #imposta il colore di sfondo della casella
                           activeforeground='#00FF00', #imposta il colore del testo quando la casella è attiva
                           activebackground='black', #imposta il colore di sfondo quando la casella è attiva
                           padx=25, #imposta lo spazio orizzontale tra il testo e il bordo
                           pady=10, #imposta lo spazio verticale tra il testo e il bordo
                           image=python_photo, #imposta l'immagine da mostrare sulla casella
                           compound='left') #imposta la posizione dell'immagine rispetto al testo
check_button.pack() #posiziona la casella nella finestra

window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi






# Creazione dei pulsanti radio (radiobutton) che mostrano un testo e un’immagine e che stampano una frase a seconda del pulsante selezionato.
# radio button = simile alla casella di controllo, ma si può selezionare solo uno tra un gruppo
from tkinter import *

food = ["pizza","hamburger","hotdog"] #crea una lista di cibi

def order(): #definisce una funzione chiamata order
    if(x.get()==0): #se il valore della variabile x è 0
        print("You ordered pizza!") #stampa "You ordered pizza!"
    elif(x.get()==1): #se il valore della variabile x è 1
        print("You ordered a hamburger!") #stampa "You ordered a hamburger!"
    elif(x.get()==2): #se il valore della variabile x è 2
        print("You ordered a hotdog!") #stampa "You ordered a hotdog!"
    else: #altrimenti
        print("huh?") #stampa "huh?"

window = Tk() #crea un'istanza di una finestra
window.geometry("1160x760")
pizzaImage = PhotoImage(file='pizza.png') #carica un'immagine da un file
hamburgerImage = PhotoImage(file='hamburger.png') #carica un'immagine da un file
hotdogImage = PhotoImage(file='hotdog.png') #carica un'immagine da un file
foodImages = [pizzaImage,hamburgerImage,hotdogImage] #crea una lista di immagini

x = IntVar() #crea una variabile di controllo di tipo intero

for index in range(len(food)): #per ogni indice nella lunghezza della lista food
    radiobutton = Radiobutton(window, #crea un pulsante radio nella finestra
                              text=food[index], #imposta il testo del pulsante con l'elemento corrispondente della lista food
                              variable=x, #imposta la variabile di controllo associata al pulsante
                              value=index, #imposta il valore da assegnare alla variabile quando il pulsante è selezionato
                              padx = 25, #imposta lo spazio orizzontale tra il testo e il bordo
                              font=("Impact",50), #imposta il tipo, la dimensione e lo stile del carattere
                              image = foodImages[index], #imposta l'immagine da mostrare sul pulsante con l'elemento corrispondente della lista foodImages
                              compound = 'left', #imposta la posizione dell'immagine rispetto al testo
                              #indicatoron=0, #elimina gli indicatori circolari 
                              #width = 375, #imposta la larghezza dei pulsanti in pixel 
                              command=order #imposta la funzione da chiamare quando il pulsante cambia stato
                              )
    radiobutton.pack(anchor=W) #posiziona il pulsante nella finestra con l'allineamento a sinistra

window.mainloop() #posiziona la finestra sullo schermo del computer, ascolta gli eventi






# Creazione una semplice interfaccia grafica con un’immagine, una scala e un pulsante. Scala di temperatura
from tkinter import * #importa tutti i moduli di tkinter

def submit(): #definisce una funzione che stampa la temperatura selezionata dalla scala
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk() #crea una finestra principale

hotImage = PhotoImage(file='hot.png') #carica un'immagine di una fiamma
hotLabel = Label(image=hotImage) #crea un'etichetta che mostra l'immagine
hotLabel.pack() #posiziona l'etichetta nella finestra

scale = Scale(window, #crea una scala verticale
              from_=100, #imposta il valore massimo a 100
              to=0, #imposta il valore minimo a 0
              length=300, #imposta la lunghezza della scala a 600 pixel
              orient=VERTICAL, #orienta la scala verticalmente
              font = ('Consolas',20), #imposta il tipo e la dimensione del carattere
              tickinterval = 10, #aggiunge indicatori numerici per il valore
              #showvalue = 0, #nasconde il valore corrente
              resolution = 5, #imposta l'incremento dello slider a 5
              troughcolor = '#69EAFF', #imposta il colore dello sfondo della scala
              fg = '#FF1C00', #imposta il colore del testo e dello slider
              bg = '#111111' #imposta il colore dello sfondo dell'etichetta

              )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #imposta il valore corrente dello slider alla metà del range
scale.pack() #posiziona la scala nella finestra

coldImage = PhotoImage(file='cold.png') #carica un'immagine di un fiocco di neve
coldLabel = Label(image=coldImage) #crea un'etichetta che mostra l'immagine
coldLabel.pack() #posiziona l'etichetta nella finestra

button = Button(window,text='submit',command=submit) #crea un pulsante che chiama la funzione submit
button.pack() #posiziona il pulsante nella finestra

window.mainloop() #avvia il ciclo principale della finestra





# listbox = Una lista di elementi di testo selezionabili all'interno del suo contenitore
def submit(): #definisce una funzione che stampa il cibo ordinato dalla listbox

    food = [] #crea una lista vuota per il cibo

    for index in listbox.curselection(): #per ogni indice selezionato nella listbox
        food.insert(index,listbox.get(index)) #inserisce il corrispondente elemento di testo nella lista del cibo

    print("You have ordered: ") #stampa un messaggio
    for index in food: #per ogni elemento nella lista del cibo
        print(index) #stampa l'elemento

def add(): #definisce una funzione che aggiunge un nuovo elemento alla listbox
    listbox.insert(listbox.size(),entryBox.get()) #inserisce il testo inserito nella entryBox alla fine della listbox
    listbox.config(height=listbox.size()) #aggiorna l'altezza della listbox in base al numero di elementi

def delete(): #definisce una funzione che elimina gli elementi selezionati dalla listbox
    for index in reversed(listbox.curselection()): #per ogni indice selezionato nella listbox, partendo dall'ultimo
        listbox.delete(index) #elimina l'elemento corrispondente dalla listbox

    listbox.config(height=listbox.size()) #aggiorna l'altezza della listbox in base al numero di elementi

from tkinter import * #importa tutti i moduli di tkinter

window = Tk() #crea una finestra principale

listbox = Listbox(window, #crea una listbox nella finestra
                  bg="#f7ffde", #imposta il colore di sfondo della listbox
                  font=("Constantia",35), #imposta il tipo e la dimensione del carattere della listbox
                  width=12, #imposta la larghezza della listbox a 12 caratteri
                  selectmode=MULTIPLE) #permette di selezionare più elementi dalla listbox
listbox.pack() #posiziona la listbox nella finestra

listbox.insert(1,"pizza") #inserisce "pizza" come primo elemento della listbox
listbox.insert(2,"pasta") #inserisce "pasta" come secondo elemento della listbox
listbox.insert(3,"garlic bread") #inserisce "garlic bread" come terzo elemento della listbox
listbox.insert(4,"soup") #inserisce "soup" come quarto elemento della listbox
listbox.insert(5,"salad") #inserisce "salad" come quinto elemento della listbox

listbox.config(height=listbox.size()) #imposta l'altezza della listbox in base al numero di elementi

entryBox = Entry(window) #crea una entryBox nella finestra
entryBox.pack() #posiziona la entryBox nella finestra

frame = Frame(window) #crea un frame nella finestra
frame.pack() #posiziona il frame nella finestra

submitButton = Button(frame,text="submit",command=submit) #crea un pulsante che chiama la funzione submit nel frame
submitButton.pack(side=LEFT) #posiziona il pulsante a sinistra nel frame

addButton = Button(frame,text="add",command=add) #crea un pulsante che chiama la funzione add nel frame
addButton.pack(side=LEFT) #posiziona il pulsante a sinistra nel frame

deleteButton = Button(frame,text="delete",command=delete) #crea un pulsante che chiama la funzione delete nel frame
deleteButton.pack(side=LEFT) #posiziona il pulsante a sinistra nel frame

window.mainloop() #avvia il ciclo principale della finestra









#Creazione di tanti Message box, potenziale codice malevolo
from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    messagebox.showinfo(title='This is an info message box',message='You are a person')
    messagebox.showwarning(title='WARNING!',message='You have A VIRUS!!!!')
    messagebox.showerror(title='ERROR!',message='something went wrong :(')

    if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
        print('You did a thing!')
    else:
        print('You canceled a thing! :(')

    if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):
        print('You retried a thing!')
    else:
        print('You canceled a thing! :(')

    if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
        print('I like cake too :)')
    else:
        print('Why do you not like cake? :(')

    answer = messagebox.askquestion(title='ask question',message='Do you like pie?')
    if(answer == 'yes'):
        print('I like pie too :)')
    else:
        print('Why do you not like pie? :(')

    answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?',icon='question')
    if(answer==True):
        print("You like to code :)")
    elif(answer==False):
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question ")

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()






# programma che usa la libreria tkinter per creare una finestra grafica con un pulsante. Quando si clicca il pulsante, 
# si apre una finestra di dialogo per scegliere un colore. Il colore scelto viene poi usato per cambiare lo sfondo della finestra ù
# principale
from tkinter import * #importa tutti i moduli della libreria tkinter
from tkinter import colorchooser #importa il modulo colorchooser per la scelta dei colori

def click(): #definisce una funzione che viene eseguita quando si clicca il pulsante
    color = colorchooser.askcolor() #chiede all'utente di scegliere un colore e lo assegna a una variabile
    colorHex = color[1] #estrae l'elemento all'indice 1 della variabile color, che corrisponde al codice esadecimale del colore
    window.config(bg=colorHex) #configura la finestra principale per usare il colore scelto come sfondo

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale
window.geometry("420x420") #imposta le dimensioni della finestra a 420x420 pixel
button = Button(text='click me',command=click) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo 'click me' e la funzione click come comando
button.pack() #posiziona il pulsante nella finestra usando il metodo pack
window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica






# programma che usa la libreria tkinter per creare una finestra grafica con un widget di tipo Text. Il widget Text permette di inserire più linee di testo, come una casella di testo. 
# Quando si clicca il pulsante submit, il testo inserito viene stampato nella console


# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import * #importa tutti i moduli della libreria tkinter

def submit(): #definisce una funzione che viene eseguita quando si clicca il pulsante submit
    input = text.get("1.0",END) #ottiene il testo inserito nel widget Text, dal primo carattere fino alla fine
    print(input) #stampa il testo nella console

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale
text = Text(window, #crea un oggetto di tipo Text, che rappresenta il widget per inserire il testo
            bg="light yellow", #imposta il colore di sfondo a giallo chiaro
            font=("Ink Free",25), #imposta il tipo e la dimensione del font a Ink Free e 25
            height=8, #imposta l'altezza del widget a 8 righe
            width=20, #imposta la larghezza del widget a 20 colonne
            padx=20, #imposta il padding orizzontale a 20 pixel
            pady=20, #imposta il padding verticale a 20 pixel
            fg="purple") #imposta il colore del testo a viola
text.pack() #posiziona il widget Text nella finestra usando il metodo pack
button = Button(window,text="submit",command=submit) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo 'submit' e la funzione submit come comando
button.pack() #posiziona il pulsante nella finestra usando il metodo pack
window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica







# programma che usa la libreria tkinter per creare una finestra grafica con un pulsante Open. Quando si clicca il pulsante, si apre una finestra di dialogo per scegliere un file da aprire. 
# Il file viene poi letto e stampato nella console. 

from tkinter import * #importa tutti i moduli della libreria tkinter
from tkinter import filedialog #importa il modulo filedialog per la scelta dei file

def openFile(): #definisce una funzione che viene eseguita quando si clicca il pulsante Open
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main", #chiede all'utente di scegliere un file da aprire e lo assegna a una variabile, impostando la cartella iniziale a quella specificata
                                          title="Open file okay?", #imposta il titolo della finestra di dialogo a 'Open file okay?'
                                          filetypes= (("text files","*.txt"), #imposta i tipi di file accettati a file di testo con estensione .txt
                                          ("all files","*.*"))) #o a tutti i file con qualsiasi estensione
    file = open(filepath,'r') #apre il file in modalità lettura e lo assegna a una variabile
    print(file.read()) #legge il contenuto del file e lo stampa nella console
    file.close() #chiude il file

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale
button = Button(text="Open",command=openFile) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo 'Open' e la funzione openFile come comando
button.pack() #posiziona il pulsante nella finestra usando il metodo pack
window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica





# programma che usa la libreria tkinter per creare una finestra grafica con un pulsante save e un widget Text. 
# Quando si clicca il pulsante, si apre una finestra di dialogo per salvare il file con il testo inserito nel widget Text. 
# Il file viene poi scritto e chiuso
from tkinter import * #importa tutti i moduli della libreria tkinter
from tkinter import filedialog #importa il modulo filedialog per la scelta dei file

def saveFile(): #definisce una funzione che viene eseguita quando si clicca il pulsante save
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main", #chiede all'utente di scegliere un nome e una posizione per salvare il file, impostando la cartella iniziale a quella specificata
                                    defaultextension='.txt', #imposta l'estensione di default a .txt
                                    filetypes=[ #imposta i tipi di file accettati a file di testo, file html o tutti i file
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None: #se l'utente non sceglie nessun file, esce dalla funzione
        return
    filetext = str(text.get(1.0,END)) #ottiene il testo inserito nel widget Text, dal primo carattere fino alla fine, e lo converte in una stringa
    #filetext = input("Enter some text I guess: ") //use this if you want to use console window
    file.write(filetext) #scrive il testo nel file
    file.close() #chiude il file

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale
button = Button(text='save',command=saveFile) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo 'save' e la funzione saveFile come comando
button.pack() #posiziona il pulsante nella finestra usando il metodo pack
text = Text(window) #crea un oggetto di tipo Text, che rappresenta il widget per inserire il testo
text.pack() #posiziona il widget Text nella finestra usando il metodo pack
window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica






# Creazione di una finestra grafica con una barra dei menu. La barra dei menu contiene due menu a cascata: File e Edit. 
# Il menu File ha quattro opzioni: Open, Save, Exit, che sono associate alle funzioni openFile, saveFile e quit, 
# e una linea di separazione. Il menu Edit ha tre opzioni: Cut, Copy, Paste, che sono associate alle funzioni cut, copy e paste. 
# Ogni opzione del menu File ha anche un’immagine a sinistra del testo, che viene caricata da un file locale. 
# Quando si sceglie una delle opzioni del menu, la funzione corrispondente stampa un messaggio nella console.

from tkinter import * #importa tutti i moduli della libreria tkinter

def openFile(): #definisce una funzione che viene eseguita quando si sceglie l'opzione Open del menu File
    print("File has been opened!") #stampa il messaggio 'File has been opened!' nella console
def saveFile(): #definisce una funzione che viene eseguita quando si sceglie l'opzione Save del menu File
    print("File has been saved!") #stampa il messaggio 'File has been saved!' nella console
def cut(): #definisce una funzione che viene eseguita quando si sceglie l'opzione Cut del menu Edit
    print("You cut some text!") #stampa il messaggio 'You cut some text!' nella console
def copy(): #definisce una funzione che viene eseguita quando si sceglie l'opzione Copy del menu Edit
    print("You copied some text!") #stampa il messaggio 'You copied some text!' nella console
def paste(): #definisce una funzione che viene eseguita quando si sceglie l'opzione Paste del menu Edit
    print("You pasted some text!") #stampa il messaggio 'You pasted some text!' nella console

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale

openImage = PhotoImage(file="file.png") #carica un'immagine da un file locale e la assegna a una variabile
saveImage = PhotoImage(file="save.png") #carica un'immagine da un file locale e la assegna a una variabile
exitImage = PhotoImage(file="exit.png") #carica un'immagine da un file locale e la assegna a una variabile

menubar = Menu(window) #crea un oggetto di tipo Menu, che rappresenta la barra dei menu
window.config(menu=menubar) #configura la finestra principale per usare la barra dei menu

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15)) #crea un oggetto di tipo Menu, che rappresenta il menu a cascata File
menubar.add_cascade(label="File",menu=fileMenu) #aggiunge il menu File alla barra dei menu, con il testo 'File'
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left') #aggiunge l'opzione Open al menu File, con il testo 'Open', la funzione openFile come comando, l'immagine openImage a sinistra del testo e il parametro compound='left' per allineare il testo e l'immagine
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left') #aggiunge l'opzione Save al menu File, con il testo 'Save', la funzione saveFile come comando, l'immagine saveImage a sinistra del testo e il parametro compound='left' per allineare il testo e l'immagine
fileMenu.add_separator() #aggiunge una linea di separazione al menu File
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left') #aggiunge l'opzione Exit al menu File, con il testo 'Exit', la funzione quit come comando, l'immagine exitImage a sinistra del testo e il parametro compound='left' per allineare il testo e l'immagine

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15)) #crea un oggetto di tipo Menu, che rappresenta il menu a cascata Edit
menubar.add_cascade(label="Edit",menu=editMenu) #aggiunge il menu Edit alla barra dei menu, con il testo 'Edit'
editMenu.add_command(label="Cut",command=cut) #aggiunge l'opzione Cut al menu Edit, con il testo 'Cut' e la funzione cut come comando
editMenu.add_command(label="Copy",command=copy) #aggiunge l'opzione Copy al menu Edit, con il testo 'Copy' e la funzione copy come comando
editMenu.add_command(label="Paste",command=paste) #aggiunge l'opzione Paste al menu Edit, con il testo 'Paste' e la funzione paste come comando

window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica





# Creazione di una finestra grafica con un frame e quattro pulsanti. 
# Il frame è un contenitore rettangolare che serve a raggruppare e posizionare i widget. I pulsanti hanno il testo W, A, S, D e 
# sono disposti in modo da formare una croce. Quando si clicca su uno dei pulsanti, non succede nulla, perché non sono associati a 
# nessun comando
# frame = a rectangular container to group and hold widgets
from tkinter import * #importa tutti i moduli della libreria tkinter

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN) #crea un oggetto di tipo Frame, che rappresenta il contenitore, con il colore di sfondo rosa, il bordo di 5 pixel e il rilievo affossato
frame.pack() #posiziona il frame nella finestra usando il metodo pack

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo W, il font Consolas di dimensione 25 e la larghezza di 3 caratteri, e lo posiziona nel frame usando il metodo pack, con il parametro side=TOP per indicare la posizione in alto
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo A, il font Consolas di dimensione 25 e la larghezza di 3 caratteri, e lo posiziona nel frame usando il metodo pack, con il parametro side=LEFT per indicare la posizione a sinistra
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo S, il font Consolas di dimensione 25 e la larghezza di 3 caratteri, e lo posiziona nel frame usando il metodo pack, con il parametro side=LEFT per indicare la posizione a sinistra
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT) #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo D, il font Consolas di dimensione 25 e la larghezza di 3 caratteri, e lo posiziona nel frame usando il metodo pack, con il parametro side=LEFT per indicare la posizione a sinistra

window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica







# Creazione di una finestra grafica con un pulsante che crea una nuova finestra. La funzione create_window crea un oggetto di tipo Tk,
# che rappresenta una nuova finestra indipendente. La riga commentata con il simbolo # potrebbe essere usata per chiudere la vecchia 
# finestra. Il pulsante nella vecchia finestra ha il testo ‘create new window’ e la funzione create_window come comando.

from tkinter import * #importa tutti i moduli della libreria tkinter

def create_window(): #definisce una funzione che viene eseguita quando si clicca il pulsante
    new_window = Tk() #crea un oggetto di tipo Tk, che rappresenta una nuova finestra indipendente
    #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    #Tk() = new independent window
    #old_window.destroy() #chiude la vecchia finestra

old_window = Tk() #crea un oggetto di tipo Tk, che rappresenta la vecchia finestra

Button(old_window,text="create new window",command=create_window).pack() #crea un oggetto di tipo Button, che rappresenta il pulsante con il testo 'create new window' e la funzione create_window come comando, e lo posiziona nella vecchia finestra usando il metodo pack

old_window.mainloop() #avvia il ciclo principale della vecchia finestra, che gestisce gli eventi dell'interfaccia grafica







# Creazione di una finestra grafica con un widget di tipo Notebook. Il widget Notebook gestisce una collezione di finestre o display, 
# che possono essere selezionati tramite delle schede. Il codice crea due schede, Tab 1 e Tab 2, che contengono ciascuna un frame con 
# una label. Il frame di Tab 1 ha una label con il testo ‘Hello, this is tab#1’, mentre il frame di Tab 2 ha una label con il testo 
# ‘Goodbye, this is tab#2’. Quando si clicca su una delle schede, si visualizza il frame corrispondente.
from tkinter import * #importa tutti i moduli della libreria tkinter
from tkinter import ttk #importa il modulo ttk, che contiene alcuni widget aggiuntivi

window = Tk() #crea un oggetto di tipo Tk, che rappresenta la finestra principale

notebook = ttk.Notebook(window) #crea un oggetto di tipo Notebook, che rappresenta il widget che gestisce le schede
#widget that manages a collection of windows/displays

tab1 = Frame(notebook) #crea un oggetto di tipo Frame, che rappresenta il frame per la scheda 1
#new frame for tab 1
tab2 = Frame(notebook) #crea un oggetto di tipo Frame, che rappresenta il frame per la scheda 2
#new frame for tab 2

notebook.add(tab1,text="Tab 1") #aggiunge il frame di Tab 1 al widget Notebook, con il testo 'Tab 1' per la scheda
notebook.add(tab2,text="Tab 2") #aggiunge il frame di Tab 2 al widget Notebook, con il testo 'Tab 2' per la scheda
notebook.pack(expand=True,fill="both") #posiziona il widget Notebook nella finestra usando il metodo pack, con i parametri expand=True e fill="both" per espandere e riempire lo spazio disponibile
#expand = expand to fill any space not otherwise used
#fill = fill space on x and y axis
Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack() #crea un oggetto di tipo Label, che rappresenta la label con il testo 'Hello, this is tab#1', con la larghezza di 50 caratteri e l'altezza di 25 righe, e la posiziona nel frame di Tab 1 usando il metodo pack
Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack() #crea un oggetto di tipo Label, che rappresenta la label con il testo 'Goodbye, this is tab#2', con la larghezza di 50 caratteri e l'altezza di 25 righe, e la posiziona nel frame di Tab 2 usando il metodo pack

window.mainloop() #avvia il ciclo principale della finestra, che gestisce gli eventi dell'interfaccia grafica








# Creazione di una semplice interfaccia grafica (GUI) che chiede all’utente di inserire il proprio nome, cognome ed email
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# grid() = geometry manager che organizza i widget in una struttura a griglia in un widget padre

# Crea una finestra principale per la GUI
window = Tk()

# Crea un'etichetta con il titolo della GUI, impostando il testo, il font e la posizione nella griglia
titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

# Crea un'etichetta con il testo "First name: ", impostando la larghezza, il colore di sfondo e la posizione nella griglia
firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
# Crea una casella di testo per inserire il nome, impostando la posizione nella griglia
firstNameEntry = Entry(window).grid(row=1,column=1)

# Crea un'etichetta con il testo "Last name: ", impostando il colore di sfondo e la posizione nella griglia
lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
# Crea una casella di testo per inserire il cognome, impostando la posizione nella griglia
lastNameEntry = Entry(window).grid(row=2,column=1)

# Crea un'etichetta con il testo "email: ", impostando il colore di sfondo e la posizione nella griglia
emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
# Crea una casella di testo per inserire l'email, impostando la posizione nella griglia
emailEntry = Entry(window).grid(row=3,column=1)

# Crea un bottone con il testo "Submit", impostando la posizione nella griglia e la dimensione in base al numero di colonne
submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

# Avvia il ciclo principale della GUI, che gestisce gli eventi e le interazioni dell'utente
window.mainloop()







# Creazione di una GUI che simula un download di un file di 100 GB
# Importa il modulo tkinter e il suo sottomodulo ttk che fornisce dei widget più moderni
from tkinter import *
from tkinter.ttk import *
# Importa il modulo time che fornisce delle funzioni per gestire il tempo
import time

# Definisce una funzione chiamata start che viene eseguita quando si clicca il bottone
def start():
    # Imposta il valore del file da scaricare in GB
    GB = 100
    # Imposta il valore iniziale del download in GB
    download = 0
    # Imposta la velocità del download in GB al secondo
    speed = 1
    # Crea un ciclo while che si ripete finché il download non raggiunge il valore del file
    while(download<GB):
        # Fa una pausa di 0.05 secondi per simulare il tempo di download
        time.sleep(0.05)
        # Aggiorna il valore della barra di progresso in base alla percentuale del download
        bar['value']+=(speed/GB)*100
        # Aggiorna il valore del download in base alla velocità
        download+=speed
        # Imposta il valore della variabile percent con la percentuale del download arrotondata
        percent.set(str(int((download/GB)*100))+"%")
        # Imposta il valore della variabile text con il download e il file in GB
        text.set(str(download)+"/"+str(GB)+" GB completed")
        # Aggiorna la GUI per mostrare i cambiamenti
        window.update_idletasks()

# Crea una finestra principale per la GUI
window = Tk()

# Crea due variabili di tipo stringa per memorizzare la percentuale e il testo del download
percent = StringVar()
text = StringVar()

# Crea una barra di progresso orizzontale con una lunghezza di 300 pixel e la posiziona nella finestra
bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

# Crea un'etichetta con il valore della variabile percent e la posiziona nella finestra
percentLabel = Label(window,textvariable=percent).pack()
# Crea un'etichetta con il valore della variabile text e la posiziona nella finestra
taskLabel = Label(window,textvariable=text).pack()

# Crea un bottone con il testo "download" e la funzione start come comando e lo posiziona nella finestra
button = Button(window,text="download",command=start).pack()

# Avvia il ciclo principale della GUI
window.mainloop()






# Creazione di una GUI che disegna una bandiera giapponese con un cerchio bianco al centro, sembra una pokeball
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# Crea una finestra principale per la GUI
window = Tk()

# Crea un widget canvas che è usato per disegnare grafici, immagini e altre forme in una finestra
# Imposta l'altezza e la larghezza del canvas a 500 pixel
canvas = Canvas(window,height=500,width=500)
# Queste righe di codice sono commentate e non vengono eseguite
#canvas.create_line(0,0,500,500,fill="blue",width=5)
#canvas.create_line(0,500,500,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
# Crea un arco rosso che riempie la metà superiore del canvas, impostando l'angolo di estensione a 180 gradi e lo spessore a 10 pixel
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# Crea un arco bianco che riempie la metà inferiore del canvas, impostando l'angolo di inizio a 180 gradi e lo spessore a 10 pixel
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# Crea un ovale bianco che rappresenta il sole, impostando le coordinate del rettangolo che lo circonda e lo spessore a 10 pixel
canvas.create_oval(190,190,310,310,fill="white",width=10)
# Posiziona il canvas nella finestra
canvas.pack()

# Avvia il ciclo principale della GUI
window.mainloop()







# Creazione di una GUI che mostra il tasto premuto dall’utente.
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# Definisce una funzione chiamata doSomething che viene eseguita quando si preme un tasto
def doSomething(event):
    # Questa riga di codice è commentata e non viene eseguita
    #print("You pressed: " + event.keysym)
    # Aggiorna il testo dell'etichetta con il nome del tasto premuto, usando l'attributo keysym dell'evento
    label.config(text=event.keysym)

# Crea una finestra principale per la GUI
window = Tk()

# Associa la funzione doSomething all'evento di pressione di un tasto nella finestra
window.bind("<Key>",doSomething)

# Crea un'etichetta con un font grande e la posiziona nella finestra
label = Label(window,font=("Helvetica",100))
label.pack()

# Avvia il ciclo principale della GUI
window.mainloop()




#  Creazione di una GUI che stampa le coordinate del mouse quando si clicca il pulsante sinistro
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# Definisce una funzione chiamata doSomething che viene eseguita quando si verifica un evento del mouse
def doSomething(event):
    # Stampa le coordinate del mouse, usando gli attributi x e y dell'evento
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

# Crea una finestra principale per la GUI
window = Tk()

# Associa la funzione doSomething all'evento di clic del pulsante sinistro del mouse nella finestra
window.bind("<Button-1>",doSomething) #left mouse click
# Queste righe di codice sono commentate e non vengono eseguite
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved
# Avvia il ciclo principale della GUI
window.mainloop()






# Creazione di una GUI che permette di trascinare due etichette colorate con il mouse
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# Definisce una funzione chiamata drag_start che viene eseguita quando si clicca il pulsante sinistro del mouse su un widget
def drag_start(event):
    # Assegna il widget che ha generato l'evento alla variabile widget
    widget = event.widget
    # Memorizza le coordinate x e y del mouse rispetto al widget nelle variabili startX e startY del widget
    widget.startX = event.x
    widget.startY = event.y

# Definisce una funzione chiamata drag_motion che viene eseguita quando si muove il mouse tenendo premuto il pulsante sinistro su un widget
def drag_motion(event):
    # Assegna il widget che ha generato l'evento alla variabile widget
    widget = event.widget
    # Calcola le nuove coordinate x e y del widget in base alla differenza tra le coordinate attuali e iniziali del mouse
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    # Posiziona il widget nelle nuove coordinate usando il metodo place
    widget.place(x=x,y=y)

# Crea una finestra principale per la GUI
window = Tk()

# Crea un'etichetta con il colore di sfondo rosso, la larghezza di 10 caratteri e l'altezza di 5 righe e la posiziona nella finestra alle coordinate (0,0)
label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

# Crea un'etichetta con il colore di sfondo blu, la larghezza di 10 caratteri e l'altezza di 5 righe e la posiziona nella finestra alle coordinate (100,100)
label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

# Associa la funzione drag_start all'evento di clic del pulsante sinistro del mouse sull'etichetta rossa
label.bind("<Button-1>",drag_start)
# Associa la funzione drag_motion all'evento di movimento del mouse con il pulsante sinistro premuto sull'etichetta rossa
label.bind("<B1-Motion>",drag_motion)

# Associa la funzione drag_start all'evento di clic del pulsante sinistro del mouse sull'etichetta blu
label2.bind("<Button-1>",drag_start)
# Associa la funzione drag_motion all'evento di movimento del mouse con il pulsante sinistro premuto sull'etichetta blu
label2.bind("<B1-Motion>",drag_motion)

# Avvia il ciclo principale della GUI
window.mainloop()






# Creazione di due GUI diverse che permettono di muovere un’immagine di una macchina da corsa con i tasti w, s, a, d o 
# le frecce direzionali.
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *

# Definisce una funzione chiamata move_up che viene eseguita quando si preme il tasto w o la freccia su
def move_up(event):
   # Sposta l'etichetta o l'immagine sul canvas verso l'alto di 10 pixel, usando il metodo place o move
   label.place(x=label.winfo_x(), y=label.winfo_y()-10)
   #canvas.move(myimage,0,-10)
# Definisce una funzione chiamata move_down che viene eseguita quando si preme il tasto s o la freccia giù
def move_down(event):
   # Sposta l'etichetta o l'immagine sul canvas verso il basso di 10 pixel, usando il metodo place o move
   label.place(x=label.winfo_x(), y=label.winfo_y()+10)
   #canvas.move(myimage,0,10)
# Definisce una funzione chiamata move_left che viene eseguita quando si preme il tasto a o la freccia sinistra
def move_left(event):
   # Sposta l'etichetta o l'immagine sul canvas verso sinistra di 10 pixel, usando il metodo place o move
   label.place(x=label.winfo_x()-10, y=label.winfo_y())
   #canvas.move(myimage,-10,0)
# Definisce una funzione chiamata move_right che viene eseguita quando si preme il tasto d o la freccia destra
def move_right(event):
   # Sposta l'etichetta o l'immagine sul canvas verso destra di 10 pixel, usando il metodo place o move
   label.place(x=label.winfo_x()+10, y=label.winfo_y())
   #canvas.move(myimage,10,0)

# Crea una finestra principale per la prima GUI
window = Tk()
# Imposta la geometria della finestra a 500x500 pixel
window.geometry("500x500")

# Associa le funzioni di movimento agli eventi di pressione dei tasti w, s, a, d o delle frecce direzionali nella finestra
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

# Crea un oggetto PhotoImage che carica l'immagine della macchina da corsa dal file racecar.png
myimage = PhotoImage(file='racecar.png')
# Crea un'etichetta che mostra l'immagine e la posiziona nella finestra alle coordinate (0,0)
label = Label(window,image=myimage)
label.place(x=0,y=0)

# Avvia il ciclo principale della prima GUI
window.mainloop()

#-------------move images on canvas-------------

# Crea una finestra principale per la seconda GUI
window = Tk()

# Associa le funzioni di movimento agli eventi di pressione dei tasti w, s, a, d o delle frecce direzionali nella finestra
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

# Crea un widget canvas che è usato per disegnare grafici, immagini e altre forme in una finestra
# Imposta la larghezza e l'altezza del canvas a 500 pixel e lo posiziona nella finestra
canvas = Canvas(window,width=500,height=500)
canvas.pack()

# Crea un oggetto PhotoImage che carica l'immagine della macchina da corsa dal file racecar.png
photoimage = PhotoImage(file='racecar.png')
# Crea un'immagine sul canvas che mostra l'oggetto PhotoImage e la posiziona sul canvas alle coordinate (0,0) con l'ancora a nord-ovest
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

# Avvia il ciclo principale della seconda GUI
window.mainloop()







# Creazione di una GUI che mostra un’immagine di un UFO che si muove in modo casuale sullo sfondo di uno spazio.ù
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *
# Importa il modulo time che fornisce delle funzioni per gestire il tempo
import time

# Imposta le costanti WIDTH e HEIGHT a 500 pixel, che rappresentano la larghezza e l'altezza della finestra
WIDTH = 500
HEIGHT = 500
# Imposta le variabili xVelocity e yVelocity a 1, che rappresentano la velocità di spostamento dell'UFO in pixel al secondo
xVelocity = 1
yVelocity = 1
# Crea una finestra principale per la GUI
window = Tk()

# Crea un widget canvas che è usato per disegnare grafici, immagini e altre forme in una finestra
# Imposta la larghezza e l'altezza del canvas a WIDTH e HEIGHT e lo posiziona nella finestra
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

# Crea un oggetto PhotoImage che carica l'immagine dello spazio dal file space.png
background_photo = PhotoImage(file='space.png')
# Crea un'immagine sul canvas che mostra l'oggetto PhotoImage e la posiziona sul canvas alle coordinate (0,0) con l'ancora a nord-ovest
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

# Crea un oggetto PhotoImage che carica l'immagine dell'UFO dal file ufo.png
photo_image = PhotoImage(file='ufo.png')
# Crea un'immagine sul canvas che mostra l'oggetto PhotoImage e la posiziona sul canvas alle coordinate (0,0) con l'ancora a nord-ovest
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

# Ottiene la larghezza e l'altezza dell'immagine dell'UFO usando i metodi width e height dell'oggetto PhotoImage
image_width = photo_image.width()
image_height = photo_image.height()

# Crea un ciclo infinito che si ripete finché la finestra non viene chiusa
while True:
    # Ottiene le coordinate attuali dell'immagine dell'UFO sul canvas usando il metodo coords del widget canvas
    coordinates = canvas.coords(my_image)
    # Stampa le coordinate sul terminale
    print(coordinates)
    # Controlla se l'immagine dell'UFO ha raggiunto il bordo destro o sinistro della finestra, confrontando le coordinate con WIDTH e image_width
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        # Inverte il segno della variabile xVelocity, facendo cambiare direzione all'UFO sull'asse x
        xVelocity = -xVelocity
    # Controlla se l'immagine dell'UFO ha raggiunto il bordo superiore o inferiore della finestra, confrontando le coordinate con HEIGHT e image_height
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        # Inverte il segno della variabile yVelocity, facendo cambiare direzione all'UFO sull'asse y
        yVelocity = -yVelocity
    # Sposta l'immagine dell'UFO sul canvas di xVelocity pixel sull'asse x e di yVelocity pixel sull'asse y, usando il metodo move del widget canvas
    canvas.move(my_image,xVelocity,yVelocity)
    # Aggiorna la GUI per mostrare i cambiamenti
    window.update()
    # Fa una pausa di 0.01 secondi per simulare il tempo di spostamento
    time.sleep(0.01)

# Avvia il ciclo principale della GUI
window.mainloop()










# Creazione di una GUI che mostra quattro palline di diversi colori e dimensioni che rimbalzano sullo schermo.
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *
# Importa il modulo Ball che contiene la definizione della classe Ball
from Ball import *
# Importa il modulo time che fornisce delle funzioni per gestire il tempo
import time

# Crea una finestra principale per la GUI
window = Tk()

# Imposta le costanti WIDTH e HEIGHT a 500 pixel, che rappresentano la larghezza e l'altezza della finestra
WIDTH = 500
HEIGHT = 500

# Crea un widget canvas che è usato per disegnare grafici, immagini e altre forme in una finestra
# Imposta la larghezza e l'altezza del canvas a WIDTH e HEIGHT e lo posiziona nella finestra
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

# Crea quattro oggetti della classe Ball, passando il canvas, le coordinate iniziali, il diametro, la velocità sull'asse x e y e il colore
# Ogni oggetto della classe Ball ha un attributo image che rappresenta l'immagine della pallina sul canvas
volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

# Crea un ciclo infinito che si ripete finché la finestra non viene chiusa
while True:
    # Chiama il metodo move di ogni oggetto della classe Ball, che sposta l'immagine della pallina sul canvas in base alla sua velocità e alle sue coordinate
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    # Aggiorna la GUI per mostrare i cambiamenti
    window.update()
    # Fa una pausa di 0.01 secondi per simulare il tempo di spostamento
    time.sleep(0.01)

# Avvia il ciclo principale della GUI
window.mainloop()

#*********************************************************
# Definisce la classe Ball, che rappresenta una pallina che si muove sul canvas
class Ball:

    # Definisce il metodo costruttore della classe, che viene chiamato quando si crea un oggetto della classe
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        # Assegna il canvas passato come parametro all'attributo canvas dell'oggetto
        self.canvas = canvas
        # Crea un'immagine di un ovale sul canvas, passando le coordinate, il diametro e il colore, e assegna il risultato all'attributo image dell'oggetto
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        # Assegna la velocità sull'asse x e y passate come parametri agli attributi xVelocity e yVelocity dell'oggetto
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    # Definisce il metodo move della classe, che sposta l'immagine della pallina sul canvas in base alla sua velocità e alle sue coordinate
    def move(self):
        # Ottiene le coordinate attuali dell'immagine della pallina sul canvas usando il metodo coords del widget canvas
        coordinates = self.canvas.coords(self.image)
        # Controlla se l'immagine della pallina ha raggiunto il bordo destro o sinistro della finestra, confrontando le coordinate con WIDTH e il diametro
        if(coordinates[2]>=(WIDTH) or coordinates[0]<0):
            # Inverte il segno della variabile xVelocity, facendo cambiare direzione alla pallina sull'asse x
            self.xVelocity = -self.xVelocity
        # Controlla se l'immagine della pallina ha raggiunto il bordo superiore o inferiore della finestra, confrontando le coordinate con HEIGHT e il diametro
        if(coordinates[3]>=(HEIGHT) or coordinates[1]<0):
            # Inverte il segno della variabile yVelocity, facendo cambiare direzione alla pallina sull'asse y
            self.yVelocity = -self.yVelocity
        # Sposta l'immagine della pallina sul canvas di xVelocity pixel sull'asse x e di yVelocity pixel sull'asse y, usando il metodo move del widget canvas
        self.canvas.move(self.image,self.xVelocity,self.yVelocity)






# Creazione di una GUI che mostra l’ora, il giorno e la data correnti
# Importa il modulo tkinter che fornisce le funzioni per creare una GUI
from tkinter import *
# Importa il modulo time che fornisce delle funzioni per gestire il tempo
from time import *

# Definisce una funzione chiamata update che viene eseguita ogni secondo
def update():
    # Ottiene la stringa dell'ora corrente nel formato 12 ore usando la funzione strftime del modulo time
    time_string = strftime("%I:%M:%S %p")
    # Aggiorna il testo dell'etichetta dell'ora con la stringa ottenuta
    time_label.config(text=time_string)

    # Ottiene la stringa del giorno corrente usando la funzione strftime del modulo time
    day_string = strftime("%A")
    # Aggiorna il testo dell'etichetta del giorno con la stringa ottenuta
    day_label.config(text=day_string)

    # Ottiene la stringa della data corrente nel formato mese, giorno e anno usando la funzione strftime del modulo time
    date_string = strftime("%B %d, %Y")
    # Aggiorna il testo dell'etichetta della data con la stringa ottenuta
    date_label.config(text=date_string)

    # Chiama la funzione update dopo 1000 millisecondi (1 secondo) usando il metodo after del widget window
    window.after(1000,update)


# Crea una finestra principale per la GUI
window = Tk()

# Crea un'etichetta che mostra l'ora corrente, impostando il font, il colore del testo e il colore di sfondo
time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# Posiziona l'etichetta nella finestra
time_label.pack()

# Crea un'etichetta che mostra il giorno corrente, impostando il font
day_label = Label(window,font=("Ink Free",25,"bold"))
# Posiziona l'etichetta nella finestra
day_label.pack()

# Crea un'etichetta che mostra la data corrente, impostando il font
date_label = Label(window,font=("Ink Free",30))
# Posiziona l'etichetta nella finestra
date_label.pack()

# Chiama la funzione update per la prima volta
update()

# Avvia il ciclo principale della GUI
window.mainloop()

