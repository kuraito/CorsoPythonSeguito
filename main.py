#----01 SINTASSI

messaggio = input("inserisci il nome: ") #input dell utente
print(messaggio) #esce l input
#l'indentazione in python è molto importante

#-----------------------------------------------------

#----- 02 VARIABILI

x = 5 #assegno valore alla variabile
y = 6
#y solamente non si può dichiarare e basta deve per forza avere un valore
#python è case sensitive quindi x e X non sono la stessa cosa
z, w, u = 32, 60, 50 #diamo 3 valori diversi a 3 variabili
e = f = g = 32 #hanno tutte e 3 lo stesso valore

#posso fare ovviamente le operazioni con le variabili

citta = ["roma", "milano", "napoli"] #una collection
x1, y1, z1 = citta #prende ognuno un valore della lista
#----------------------------------------------------------------

#----- 03 tipi di dati

#NON E' NECESSARIO SPECIFICARE IL TIPO DI DATO
#in python abbiamo str, int, float, bool, list, range ecc...

x2 = 5.5
x2 = "ciao"
print(type(x2)) #stampiamo la FUNZIONE per stampare il tipo della variabile x

#le collezioni sono: liste, tuple, range, dizionari, set

#-------------------------------------------------------------------

#--------04 casting

#si prende un numero e si converte in una stringa e viceversa

x3 = int("5") #per fare il casting a int 
y3 = str(5) #per fare il casting a stringa s

#print(x3+y3) #da errore se non si fa il casting

#concatenare due stringe si fa con +

#------------------------------------------------------------------

#---------05 Stinghe

x4 = "ciao" #è una stringa
y4 = 'ciao' #è una stringa, l'importante è solo non mischiare

x5 = """prova
1
2
fine""" #stringa multiriga

#le stringe vengono trattate come un array, quindi è un insieme di singoli caratteri

print(x4[1]) #stampa i perche prende di ciao il carattere a posizione 1
print(len(x4)) #da la lunghezza
print(x4[:3]) #dall'inizio al carattere 3 (3 non compreso però)
print(x4[2:]) #dal secondo carattere in poi
print(x4[2:7]) #dal 2 carattere al 7 carattere
print(x4[-4]) #carattere meno -4 partendo dalla fine
print(x4[-4:1]) #da -4 a 1
print(x4.upper()) #mette in alto tutto
print(x4.lower()) #mette in basso tutto
print(x4.replace("o", "w")) #tutte le o diventano w
print(x4 + y4) #si concatena la stringa

prova = "ciao ho anni {} e peso {}" #diciamo che tra le {} va un qualcosa
print(prova.format(15, 65)) #inserisce 15 nelle {}

#posso inserire gli indici nelle {}
prova1 = "ciao ho anni {1} e peso {0}" #diciamo che tra le {} va un qualcosa
print(prova1.format(15, 65)) #inserisce 15 nelle {}

prova2 = "ciao ho anni 15 e sono \"figo\""
print(prova2)
prova3 = 'sono alla ricerca dell\'amore' #ESCAPE dei caratteri (VEDERE DOCUMENTAZIONE PYTHON)

#-----------------------------------------------------------------------------

#-------06 BOOLEAN 
x6 = True
y6 = False #valori booleani

if 5 < 10:
    print("ciao sono SIUM")
else: 
    print("ciao sono sium")

print(bool(0)) #da valore false
print(bool(1)) #da valore true
print(bool(y6)) #da false
#bool("") bool(()) bool([]) bool({}) sono tutti FALSE

lista_cose_da_commprare = [] #lista vuota
if lista_cose_da_commprare: #se è vero che è falso
    print("andare al supermercato")
else:
    print("non serve andare al supermercato")

#--------------------------------------------------------------------

#--------07 OPERAZIONI ARITMERICHE
x7 = 5
y7 = 7

#si può fare
x7 = x7 + 3 #da 8
x7 += 3 #stessa cosa ora da 11 VALE ANCHE PER TUTTI GLI OPERATORI DI ASSEGNAMENTO

#abbiamo + - * / modulo % potenza ** float division//

#alcuni metodi sono min, max, abs, pow
x8 = min(10,15,25) #x8 è il minimo di quei valori
y8 = abs(-5) #da il valore assoluto

#se vogliamo fare matematica più complessa dobbiamo importare MATH

#----------------------------------------------------------------------------

#-------08 CONDIZIONI
if x8 < 10:
    print("x è minore di 10") #nell if
    print("miao") #nell if
print("non sono nell if") #non nell if

if x8 == 10: #una comparazione x8 è uguale a 10?
    print("condizione")

if x8 != 10: #se x8 è diverso da 10
    print("condizione")

#si può usare anche <= e cose simili tipo >
#un numero compreso tra 10 e 20 facciamo
# 10 <= x <= 20 
#si puo usare and e or
#not si fa con not(x < 10)
#if x % 2 == 0: PER I NUMERI PARI

if x8 % 2 == 0:
    print("numero pari")
    if(x<10):
        print("numero pari e minore di 10")
else:
    print("numero dispari")
#------------------------------------------------------------------

#-----------09 WHILE
x9 = ["milano", "roma", "napoli"]
y9 = "ciao"

i = 0
while i < 6:
    print(i)
    if i == 3:
        break #appena arriva a 3 STOPPA
    i += 1 #incremento serve per uscire nel while

while i < 6:
    i += 1
    if i == 3:
        continue #salta il 3 passa alla successiva
    print(i)

while i < 6:
    print(i)
    i += 1
else: #teniamo traccia della fine eventualmente
    print("ho finito")

#----------------------------------------------------------------------------

#---------10 FOR
lista_citta = ["milano", "roma", "napoli"]

for citta in lista_citta: #per ogni elemento in lista elementi fai quanto segue
    print(citta)

stringa = "anguria"

for c in stringa:
    print(c)

for num in range(6): #come se avesse un range da 0 a 5
    print(num)
else:
    print("ho finito")

#possiamo anche mettere break e continue 
#possiamo avere un for nell if
#for e for servono per vedere in una tabella riga x colonna
#esempio:
for riga in range(6):
    for colonna in range(2):
        print("(" + str(riga) + ":" + str(colonna)+ ")")
else:
    print("ho finito")
#--------------------------------------------------------------

#--------12 COLLEZIONI

# liste, tuple, set e dizionari
# abbiamo 3 parentesi diverse, le liste, tuple, set ecc hanno proprietà diverse

# ORDINATA si può accedere con indice
# MODIFICABILE se possiamo aggiungere, rimuovere elementi
# IMMUTABILE se non si può fare
# DUPLICABILE ossia che ci sono elementi con lo stesso valore

#le LISTE sono ORDINATE, MODIFICABILI E DUPLICABILI.
#le TUPLE sono ORDINATE, IMMUTABILI E DUPLICABILI.
#i SET sono NON ORDINATE E NON DUPLICABILI.
#i DICTIONARY sono ORDINATE, MODIFICABILI E NON DUPLICABILI.

#---------- 12.1 LISTE---------------------------------------------

x10 = ["milano", "roma", "napoli"]
y10 = ["ciao", 1000, False] #permette di avere elementi mischiati
z10 = list(("milano", "roma", 100)) #si può fare anche con il costruttore list
#in list però serve () non []

print(type(y10))
print(len(x10)) #da 3 anche se l'indice parte da 0
print(x10[-1]) #parte dall'ultimo elemento in questo caaso darà napoli
print(x10[1:3]) #è un range da 1 al 3 da roma e napoli quindi esclude solo il 1
print(x10[:2]) #tutto fino al 2

x10[1] = "Brescia" #sostituisce
x10[1:3] = "Brescia", "Venezia" #sostituisce

#per INSERIRE si usa append(), extend(), insert()-------------------------
x10.append("Torino") #inserisce in fondo
x10.insert(1, "Ragusa") #inserisce nella posizione 1

aggiunta = ["Ascea", "casalvelino"]
x10.extend(aggiunta) #aggiunge come in APPEND ma con un'altra lista CAMBIA x

#PER RIMUOVERE si usa remove(), pop(), del(), clear() ---------------
x10.pop() #toglie l'ultimo
x10.pop(1) #toglie nell'indice

del x10[0] #toglie il primo valore in questo caso
del x10 #elimina la lista intera

x10 = ["milano", "roma", "napoli"]
x10.clear() #diventa vuota ma esiste ancora

for citta in x10: #finche ci sono elementi in x10, fai quanto segue
    print(citta)

for i in range(len(x10)): #finche si è nel range di x10, fai quanto segue
    print(x10[i])

i = 0
while i < len(x10):
    print(x10[i])
    i += 1

[print(citta) for citta in x10]  #per fare il for piu ridotta
#si fa cosi [espressione for item in Lista if condizione == true]
x10 = ["milano", "roma", "napoli"]
y10 = ["a", "z", "c"]

x10.sort() #SORT ordina in modo alfabetico o numerico la lista
x10.sort(reverse = True) #SORT reverso 
y10 = x10.copy() #copia assestante

#unire più liste insieme
z11 = x10 + y10
print("ciao" + z11[1])

for c in y10:
    x10.append(c)
print(x10)

#---------12.2 TUPLE------------------------------------------------
#creazione
x11  = ("milano", "roma", "napoli")
y11 = ("milano", True)

#una tupla di un solo valore
x11 = ("milano",) # con la virgola se è di un solo valore

print(len(x11)) #da 3

x11 = tuple(("milano", "roma", "napoli")) #doppia parentesi
#possiamo accere come per le liste
print(x11[1]) #stampa roma

if "milano" in x11: #se milano è nella tupla printa ok
    print("ok")

#ESCAMOTAGE PER MODIFICARE LA TUPLA
y12 = list(x11) #diventa una lista

y12[1] = "venezia" 

x11 = tuple(y12)
print(x11) #cosi ho modificato la tupla
#del cancella tutto quindi non va bene

#PER SPACCHETTARE
(xm, ym, zm) = x11 #prendono gli elementi della tupla

for citta in x11:
    print(citta)

for i in range(len(x11)):
    print(x11[i])

i = 0
while i < len(x11):
    print(x11[i])
    i += 1

y13 = x11 + y11
print(y13)
index_citta = x11.index("milano") #da il primo milano che trova
print(index_citta)

#----------12.3 SET------------------------------------------------
x12 = {"milano", "roma", "napoli"}
#possiamo fare len, type ecc..

y14 = set(("milano", "roma", "napoli"))

#NON HA INDICI
#print(x12[1]) #NON SI PUO' FARE
#POSSIAMO ACCEDERE SOLO CON IL LOOP
for z in x12:
    print(z) #stamperà in modo del tutto randomico

print("milano" in x12) #da true o false se c'è o se non c'è

#PER AGGIUNGERE E RIMUOVERE
x12.add("venezia") #si aggiunge NON C'è APPEND SI METTE RANDOM DENTRO

aggiunta = {"campobasso", "molise"}
x12.update(aggiunta)

#per rimuovere possoiamo usare remove, discard, pop, clear e del
#x12.remove("udine") #se non abbiamo l'elemento da ERRORE
x12.discard("udine") #se non abbiamo l'elemento va AVANTI NON DA ERRORE

x12.pop() #toglie l'ultimo in modo casuale però
x12.clear() #pulisce x12
del x12 #cancella x12 NON ESISTE PIU'

#usare UNION, INTERSECTION_UPDATE, INTERSECTION, SYMMETRIC_DIFFERENCE_UPDATE, SYMMETRIC_DIFFERENCE

x12 = {"milano", "roma", "napoli"}
#z12 = x.union(y14) #CREA UN NUOVO SET ESCLUDE ELEMENTI DUPLICATI
#update semplicemente aggiorna non ne crea uno nuovo

x12.intersection_update(y14) #RESTITUISCE ELEMENTI IN COMUNE SENZA CREARE UN NUOVO SET
z13 = x12.intersection(y14) #CREA  UN NUOVO SET CON GLI ELEMENTI IN COMUNE

#INVECE
#SIMMETRIC DIFFERENCE e SYMMETRIC DIFFERENCE UPDATE TIENE TUTTO TRANNE GLI ELEMENTI IN COMUNE

#------------12.4 DICTIONARY

#modificabili ma non permettono duplicati

#devono avere chiavi e valore come oggetti in javaScript
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 21,
    #NON AMMETTE DUPLICATI DI CHIAVE
}

print(persona["cognome"])
print(persona.get("cognome"))

print(persona.keys()) #crea una lista delle chiavi
print(persona.values()) #valori
print(persona.items()) #ci da una lista di tuple chiave valore

#possiamo anche fare cosi
appoggio = persona.values()
print(appoggio)

print("nome" in persona) #verifichiamo se una chiave esiste dentro 

#per modificare i valori possiamo fare cosi
persona["nome"] = "marco"
print(persona)
#oppure cosi
persona.update({"nome": "anna"})

#per aggiungere elementi
persona["colore"] = "blu" #se non esiste un elemento l'aggiunge

#PER ELIMINARE
#persona.pop("nome") #elimina nome
#persona.popitem() #elimina l'ultimo elemento
#persona.clear()
# del persona["nome"]
# del persona

#per ciclare
for w in persona:
    print(w) #dice la chiave
    print(persona[w]) #da il valore 

for w in persona.values(): #stessa cosa ma con keys
    print(w) #da il valore

for w, e in persona.items():
    print(w, e) #da entrambe sia chiave che valore

#per copiare un dizionario invece
pers = persona.copy() #copia
print(pers)

pers = persona #fa riferimento a persona
pers = dict(persona) #crea un dizionario nuovo con i dati di persona

#dizionari annidati
persona1 = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 21,
    "indirizzo": {
        "citta": "milano",
        "cap": "00000",
        "civico": 48
    }
}

print(persona1["indirizzo"]["cap"])

#----------------------------------------------------------------------------

#------ 13 FUNZIONI ---------------------------------------------------------

#blocco di codice riutilizzabile
def fai_la_pasta(tipo_pasta, metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti" + tipo_pasta)
    if metti_sugo:
        print("prepara sugo")

fai_la_pasta("fusilli", True)

#se non sappiamo quanti parametri abbiamo
def fai_il_caffe(*opzioni): #si fa cosi se non sappiamo quanti argomenti
    print("metti l'acqua")
    print("metti" + opzioni[0])
    if opzioni[1]:
        print("prepara macinino")
    
fai_il_caffe("moka", True)

#keyword arguments
fai_la_pasta(tipo_pasta="fusilli", metti_sugo = True) #passiamo gli argomenti cosi come chiave-valore
    
#parametri di default
def fai_la_pasta(tipo_pasta = "spaghetti", sugo = True): #se non passiamo niente come default ha spaghetti e sugo true
    print("metti l'acqua")
    print("fai bollire")
    print("metti" + tipo_pasta)

fai_la_pasta("fusilli", False) #se ci passiamo questi parametri non fa il default

#return di valori
def fai_la_pasta(tipo_pasta):
    print("metti l'acqua")
    print("fai bollire")
    print("metti" + tipo_pasta)
    return True #può avere anche 1, "Stringa" ecc come return

is_pasta_pronta = fai_la_pasta("fusilli") 
if is_pasta_pronta:
    print("pasta pronta")

#--------------------------------------------------------------------------------------------------

#----------14 CLASSI E OGGETTI --------------------------------------------------
#si usano oggetti ed entita del mondo reale

#creare classe
class Persona:
    nome = "Luca"
    cognome = "Rossi"


persona1 = Persona() #abbiamo creato una persona 
persona2 = Persona() #abbiamo creato due persone

#l'istanza è un oggetto ossia deriva da Persona persona1

print(persona1.nome) #stampo il nome

#COSTRUTTORE
class Persona_generica:
    def __init__(self, nome, cognome): #self è il riferimento a se stesso
        self.nome = nome
        self.cognome = cognome #costruttore finito

    def saluta(self): #metodo, funzione o anche azione che può fare una persona_generica
        print("ciao sono " + self.nome)
    
    def saluta_specifico(self, stringa):
        print("ciao " + stringa + " sono " + self.nome)

pers1 = Persona_generica("Marco", "Verdi") #creiamo noi l'oggetto, lo costruiamo noi
print(pers1.nome)

pers1.saluta() #esce a schemo "ciao sono marco" in questo caso
#self aiuta a capire con chi parliamo per es. in questo caso quale persona è, per capire di che istanza stiamo parlando
#self va messo davanti in ogni funzione 'def saluta(self)' , ma non dobbiamo specificarlo 'pers1.saluta()'
pers1.saluta_specifico("Michele")

pers1.nome = "Maria" #abbiamo cambiato il nome
pers1.saluta() 

#del pers1.nome #abbiamo rimosso il nome a pers1
#del pers1 #abbiamo eliminato l'oggetto

#--------------------------------------------------------------------------------------

#--------15 EREDITARIETA' -------------------------------------------------------
#l'ereditarietà riguarda cosa una classe eredità da altre classi in più anche eventualmente cose aggiuntive
class Persona_vivente:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def saluta (self):
        print("ciao sono" + self.nome)

class Insegnante(Persona_vivente): #qui diciamo insegnante estende Persona_Vivente
    #def __init__(self): #Ha sovrascritto o Overriding il metodo per inizializzare in questo caso
        #pass #pass serve per mettere niente in un metodo o in altro e non avere errore

    def __init__(self, nome, cognome, materia): #questo dice ok lo sovrascrivo però comunque si riferisce a PERSONA VIVENTE
        super().__init__(nome, cognome)
        self.materia = materia #insegnante ha in più materia
        
    def saluta(self): #OVERRIDE DEL METODO
        print("buongiorno sono " + self.nome)
    
    def dati_voto(self): #METODO IN PIU' DELLA SOTTOCLASSE
        print("bravo, 8")

person1 = Persona_vivente("Luca", "Rossi")
#insegn1 = Insegnante("Anna", "Neri") #prende il costruttore di Persona_vivente
insegn1 = Insegnante("Anna", "Neri", "Matematica")

#insegn1.saluta() #prende il metodo di Persona_vivente perche la eredita
insegn1.saluta() #saluta come fa la sottoclasse insegnante e non come persona vivente fa

#--------------------------------------------------------------------------------------------------------

#---- 16 SCOPE -------------------------------------------------------------------------------------------
#può essere locale o globale
#locale solo nella funzione

variabilefunzione = 100

def funzione():
    #variabilefunzione = 400 #variabile locale diversa dalla variabile fuori dalla funzione

    global variabilefunzione #global fa riferimento alla variabile globale
    variabilefunzione = 400 #cosi facendo mi riferisco alla variabile globale ossia quella che sta fuori la funzione
    def sottofunzione():
        print(variabilefunzione) #variabilefunzione ha solo la visibilità in def
    sottofunzione()
    return variabilefunzione #grazie al return abbiamo la variabile fuori

variabileglobale = funzione() #cosi, le variabili fuori dalle funzioni hanno scope globale

#----------------------------------------------------------------------------------------------------------

#-------- 17 MODULI --------------------------------------------------------------------------------------
# come se fosse una libreria file con insieme di funzione che vogliamo integrare nel programma

#pepr includere il modulo
import miomodulo
# miomodulo.saluta("Luca") #chiamiamo la funzione del modulo

personamodulo1 = miomodulo.personaggio1["nome"]
miomodulo.saluta(personamodulo1)

#si puo usare un alias per non scrivere sempre il nome
#import miomodulo as em
#quindi si usa em e non miomodulo d'ora in poi

#modulo platform
import platform
sistema = platform.system()
print(sistema)

#modulo math
import math
print(math.floor(2.90)) #arrotonda per difetto da 2
print(dir(math)) #tutte le funzioni di math

#come importare solo UNA PARTE DEL MODULO
#from miomodulo import personaggio1
#cosi possiamo solo usare personaggio1
#PYTHON MODULES PER I MODULI

#----------------------------------------------------------------------------

#---------- 18 DATETIME ----------------------------------------

#python non ha un suo tipo di data, quindi
import datetime

dataoggi = datetime.datetime.now() #prendiamo la data di ora
print(dataoggi)

#datagen = datetime.datetime(2012, 6, 13) #diamo una data
#print(datagen)

#string format time, formattiamo la data
print(dataoggi.strftime("%B")) #da gennaio ossia il mese corrente
#disponibile sulla documentazione tutti i possibili parametri

#possiamo combinare i parametri
print(dataoggi.strftime("%d %n %Y"))

#----------------------------------------------------------------------

#------------- 19 JSON ------------------------------------------------

#serve se python vuole collegare python con qualcosa frontend 
#backend python e frontend javascript si mandano dati con ajax e si inviano in JSON

import json 

oggettoJson = '{  "nome": "Luca", "cognome": "Rossi", "eta": 25 }' #formato json per esempio
#leggere un JSON
riceveJson = json.loads(oggettoJson) #diventa un dizionario
print(riceveJson["nome"])

#passare da python a JSON
oggettoDic = {  
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25 
}

riceveDic = json.dumps(oggettoDic)
print(riceveDic) #da una stringa ossia un JSON

#i dati convertibili da python a Json sono:
#dizionari, liste, tuple, int, float, True, false, None

altroJson = json.dumps(("rome", "napoli")) #qui abbiamo dato una tupla

#formattare e ordinare JSON
oggettoX = {  
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25 ,
    "isOnline": True,
    "interessi": ["calcio", "basket"],
    "moneteInTasca": 4.56,
    "fidanzata": None
}

oggettoOrdinato = json.dumps(oggettoX, indent=4, separators=(", ", "= "), sort_keys=True) #basta aggiungere indent per formattare
#inoltre i separatori servono per formattare
print(oggettoOrdinato)
#sort_keys = True invece ordina in modo alfabetico

#--------------------------------------------------------------------------------

#---------- 20 PIP ----------------------------------------------------------

#pip è un package menager , gestore di pacchetti creati da altri, funzionalità extra
#un pacchetto è tipo un modulo

#il sito per i pacchetti è pypi.org
#per questo esempio proviamo camelCase

#per installare un pacchetto py -m pip install nomepacchetto
#per rimuovere py -m pip unistall nomepacchetto e poi yes
#pip list per la lista dei pacchetti 

import camelcase  #poi si importa il modulo

c = camelcase.CamelCase()
frase = "ciao sono edo"
print(c.hump(frase))

#------------------------------------------------------------

#-------- 21 TRY EXCEPT ------------------------------------

#se succedono errori si devono gestire sennò si stoppa il programma

#try permette di testare un blocco di codice che dovrebbe generare l'errore
#except permette di raccogliere l'errore dopo il codice in try
#finally permette di eseguire un altro tipo di codice dopo try ed except

try: #prova a fare
    print(variabileNonDichiarata)
except: #nel caso c'è un problema fai
    print("la variabile non e' stata dichiarata")
    #pass se non si vuole far nulla
finally: #serve per mandare a schermo indifferentemente dal risultato
    print("finalmente")
#else: #se non c'è nessun problema fai
#    print("nessun problema")

print("eccezione gestita")

#possiamo specificare il tipo di errore 
#esempio:

#except NameError:
#print("namerror lanciata")
#except ErrorDiverso:
#print(" altro errore") 

#in questo caso lancia solo l'errore che deve lanciare
#se c'è solo except è generico quindi lancia sempre

#per lanciare un eccezione da noi
numero = -1

if x < 0:
    raise Exception("numero minore di zero") #lanciamo noi un errore e lo gestiamo

print("altro")

#------------------------------------------------------------

#-------- 22 USER INPUT -----------------------------------

person = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

operazioni = ("aggiungere", "modificare", "terminare")
operazione = input("cosa vuoi fare")

def start():
    if operazione == operazioni[0]:
        aggiunta = input("aggiungi separato da virgola")
        aggiungi(aggiunta.split(",")) #ci creerà una lista con i parametri separati
    elif operazione == operazioni[1]:
        pass


def aggiungi(param): #aggiunge nel dizionario quello che diamo in input
    chiave = param[0]
    valore = param[1]
    person[chiave] = valore #inserisce chiave valore
    print(person)

while True:
    if operazione == operazioni[2]:
        break
    start() #percche cosi resta sempre attivo il programma
    #per chiudere il programma aggiungiamo un elif con "terminare"

#--------------------------------------------------------------------------------------

#------- 23 FORMATTAZIONE STRINGA -------------------------------------

peso = 65
altezza = 176

#non si può fare, da errore
#frase = "ciao sono matteo e sono alto" + altezza

#quindi string formatting
frase = "ciao sono matteo e sono alto {0:.2f} cm e peso {1}" #si possono mettere valori in {} (cercare string format parameters)
# :.2f ossia 176.00 
# 0 e 1 sono gli indici ossia a quali argomenti si riferiscono le parentesi {}
frase = frase.format(altezza, peso) #attenzione all'ordine e devono essere tutti gli argomenti richiesti
print(frase)

frase1 = "ciao sono amedeo e sono alto {altezza} cm e peso {peso}"
print(frase1.format(peso = 100, altezza = 200)) #disordinati ma con indici nominali

#-------------------------------------------------------------------------------------

#------ 24 LAVORARE CON I FILE ------------------------------------------------------

# r - READ: apre il file per leggere, errore se non esiste
# a - APPEND: apre il file per aprire il file ma scrivere alla fine senza modificare 
#               se non esiste lo crea
# w - WRITE: apre il file per scrivere, se non esiste lo crea
# x - CREATE: crea il file, errore se gia esiste

#aprire un file 
#f = open("testo.txt") #scrivere senza niente e come scrivere r ossia READ

try: #provo a creare testo
    f = open("testo.txt", "x") #lo creo perche se non esiste con "r" DA ERRORE
except: #gia esiste lo leggo solamente
    f = open("testo.txt", "r") 

print(f.read()) 
print(f.read(1)) #esce solo la prima lettera in questo caso

print(f.readline()) #legge solo la prima riga
print(f.readline()) #legge ma stavolta la riga successiva

for riga in f:
    print(riga) #stampa tutte le righe

f.close() #quando abbiamo finito lo chiudiamo

#per scrivere si usa a e w
f = open("testo.txt", "a")
f.write("aggiunta testo alla fine")
#IL FILE PERO NON E' LEGGIBILE IN QUESTO CASO SI PUO' SOLO APPENDERE
#PER LEGGERLO SI DEVE RIAPRIRE IN LETTURA
#con f = open("testo.txt", "r")
f.close()

f = open("testo.txt", "w") #se non c'è testo.txt , lo crea
f.write("nuova aggiunta") #write va a sovrascrivere tutto
f.close()


#f = open("fileCreato.txt", "x") #gia esiste se si vuole creare un file che gia esiste DA ERRORE

#per eliminare il file 
import os

os.remove("testo.txt")

if os.path.exists("fileNonEsiste.txt"):
    pass
else:
    print("non esiste un file con questo nome")

#--------------------------------------------------------------------------------------------------