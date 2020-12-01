'''
import mysql.connector as sql

dbLibri = sql.connect(host="35.238.217.33", user="root", passwd="1234", database="Libri")
# come argomento nel metodo connect si inserisce l'indirizzo IP dell'host, il nome dello user e la password
# questi 3 parametri vengono impostati in mySQL

print(dbLibri)

if(dbLibri): # controllo di sicurezza per verificare se la connessione con mySQL per creare il database è riuscita o no
    print("connessione riuscita")

else:
    print("connessione non riuscita")

mycursor = dbLibri.cursor() # attivazione del cursore utilizzato per eseguire il codice in sql
mycursor.execute("Create database Libri") # creazione del database Libri
mycursor.execute("Show databases") # stampa di tutti i database

for db in mycursor: # stampa di controllo del database
    print(db)

mycursor.execute("Create table libri(titolo varchar(200), autore varchar(200), disponibilità varchar(200))") # creazione della tabella all'interno del database Libri
mycursor.execute("Create table libriPrestati(IDUtente int, titolo varchar(200), autore varchar(200), giorniPrestito int)") # creazione della tabella all'interno del database Libri

with open('libri.txt', encoding="utf8") as f: # lettura del file txt contenente gli utenti iniziali
    testoFile = f.read()

stringhe = testoFile.split("\n")

for libro in stringhe: # la tabella utenti viene riempita con gli utenti del file txt
    titolo = libro[:libro.index(":")]
    autore = libro[libro.index(":")+1:]
    mycursor.execute("Insert into libri(titolo, autore, disponibilità) values(%s, %s, 'si')", (titolo.upper(), autore.upper()))
    dbLibri.commit()

dbLibri.close()
'''
