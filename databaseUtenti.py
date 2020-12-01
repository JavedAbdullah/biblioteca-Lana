'''
import mysql.connector as sql 
import random
import biblioteca as b

dbUtenti = sql.connect(host="35.238.217.33", user="root", passwd="1234", database="Utenti")
# come argomento nel metodo connect si inserisce l'indirizzo IP dell'host, il nome dello user e la password
# questi 3 parametri vengono impostati in mySQL

print(dbUtenti)

if(dbUtenti): # controllo di sicurezza per verificare se la connessione con mySQL per creare il database è riuscita o no
    print("connessione riuscita")

else:
    print("connessione non riuscita")

mycursor = dbUtenti.cursor() # attivazione del cursore utilizzato per eseguire il codice in sql
mycursor.execute("Create database Utenti") # creazione del database Utenti
mycursor.execute("Show databases") # stampa di tutti i database

for db in mycursor: # stampa di controllo del database 
    print(db)

mycursor.execute("Create table utenti(nome varchar(200), cognome varchar(200), ID int, libriPresi int)") # creazione della tabella all'interno del database Utenti

with open('utenti.txt', encoding="utf8") as f: # lettura del file txt contenente gli utenti iniziali
    testoFile = f.read()

utenti = testoFile.split("\n")

for utente in utenti: # la tabella utenti viene riempita con gli utenti del file txt 
    nome = utente[:utente.index(":")]
    cognome = utente[utente.index(":")+1:]
    ID = random.randint(10000000, 100000000)

    while ID in b.IDUtenti():
        ID = random.randint(10000000, 100000000)
        
    mycursor.execute("Insert into utenti(nome, cognome, ID, libriPresi) values(%s, %s, %s, %s)", (nome.upper(), cognome.upper(), ID, 0))
    dbUtenti.commit()

dbUtenti.close()
'''