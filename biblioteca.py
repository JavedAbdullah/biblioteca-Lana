import mysql.connector as sql
import random

#viene stabilita la connessione tra il pc e il database creato su Google Cloud Platform attraverso mySQL e viene importato il database 'Libri'
dbLibri = sql.connect(host="35.238.217.33", user="root", passwd="1234", database="Libri")
#viene stabilita la connessione tra il pc e il database creato su Google Cloud Platform attraverso mySQL e viene importato il database 'Utenti'
dbUtenti = sql.connect(host="35.238.217.33", user="root", passwd="1234", database="Utenti")

#si creano due cursori che ci permetteranno di utilizzare le risorse del database attraverso il linguaggio SQL
cursorLibri = dbLibri.cursor()
cursorUtenti = dbUtenti.cursor()

class Libro:
    def __init__(self, titolo, autore, disponibilita):# costruttore che crea l'oggetto libro
        self.titolo = titolo
        self.autore = autore
        self.disponibilita = disponibilita

class LibroPrestato:
    def __init__(self, persona, titolo, autore, scadenza):# costruttore che crea l'oggetto libroPrestato
        self.persona = persona
        self.titolo = titolo
        self.autore = autore
        self.scadenza = scadenza

class Utente:
    def __init__(self, nome, cognome, id, libriPresi):# costruttore che crea l'oggetto Utente
        self.nome = nome
        self.cognome = cognome
        self.id = id
        self.libriPresi = libriPresi

def IDUtenti():# metodo che restituisce tutti gli ID degli utenti
    """IDUtenti

       metodo che restituisce tutti gli ID degli utenti

       Ritorna una lista degli ID di tutti gli utenti presenti nel database
    """   
    all_ID = []
    cursorUtenti.execute("SELECT * FROM utenti")# attraverso il cursore vengono prelevati dal database tutti gli utenti con i loro attributi
    ID_Utenti = cursorUtenti.fetchall()
    for id in ID_Utenti:
        all_ID.append(id[2])# tutti gli ID vengono inseriti nella lista all_ID
    
    return all_ID # il metodo ci restituisce la lista all_ID

def mostraLibriDisponibili():# metodo che restituisce una lista di libri disponibili in biblioteca
    """mostraLibriDisponibili

       metodo che restituisce una lista di tutti i libri presenti nel database sottoforma di oggetti di tipo libro

       Ritorna una lista di oggetti Libro
    """
    cursorLibri.execute("SELECT * FROM libri")# attraverso il cursore vengono prelevati dal database tutti i libri con i loro attributi
    libri = cursorLibri.fetchall()

    listaLibri = []

    for libro in libri:
        if(libro[2] == 'si'):
            listaLibri.append(Libro(str(libro[0]), str(libro[1]), str(libro[2])))# tutti i libri disponibili vengono inseriti nella lista listaLibri

    return listaLibri# il metodo ci restituisce la lista listaLibri

def cercaPerTitolo(titolo):# metodo che restituisce una lista di libri con lo stesso titolo
    """cercaPerTitolo

       metodo che restituisce una lista di libri con lo stesso titolo sotto forma di oggetti Libro

       Ritorna una lista di oggetti Libro
    """
    cursorLibri.execute("SELECT * FROM libri")# attraverso il cursore vengono prelevati dal database tutti i libri con i loro attributi
    libri = cursorLibri.fetchall()

    listaLibri = []

    for libro in libri:
        if(str(libro[0]) == titolo):
            listaLibri.append(Libro(str(libro[0]), str(libro[1]), str(libro[2])))# tutti i libri con lo stesso titolo vengono inseriti nella lista listaLibri
    
    return listaLibri# il metodo ci restituisce la lista listaLibri

def cercaPerNomeUtente(nomeUtente):# metodo che restituisce una lista di utenti con lo stesso nome
    """cercaPerNomeUtente

       metodo che restituisce una lista di utenti con lo stesso nome
    
       :type nomeUtente: string
       :param nomeUtente: stringa contenente il nome dell'utente

       Ritorna una lista degli utenti di tipo Utente con lo stesso nomeUtente 
    """
    cursorUtenti.execute("SELECT * FROM utenti")# attraverso il cursore vengono prelevati dal database tutti gli utenti con i loro attributi
    utenti = cursorUtenti.fetchall()

    listaUtenti = []

    for utente in utenti:
        if(str(utente[0]) == nomeUtente):
            listaUtenti.append(Utente(str(utente[0]), str(utente[1]), str(utente[2]), str(utente[3])))# tutti gli utenti con lo stesso titolo vengono inseriti nella lista listaUtenti
    
    return listaUtenti# il metodo ci restituisce la lista listaUtenti

def prendiPrestito(titolo, IDUtente): #il metodo permette di prendere in prestito un libro seguendo un iter preciso
    """prendiPrestito

       metodo che permette di prendere in prestito un libro seguendo un iter preciso
    
       :type titolo: string
       :param titolo: titolo del libro da prenotare

       :type IDUtente: string
       :param IDUtente: ID dell'utente

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    print(type(IDUtente))
    IDUtente = int(IDUtente)
    controllo = False

    cursorLibri.execute("SELECT * FROM libri")# attraverso il cursore vengono prelevati dal database tutti i libri con i loro attributi
    libri = cursorLibri.fetchall()# tutti i libri vengono inseriti in una lista
    
    for libro in libri:
        if(libro[0] == titolo):# ricerca del libro desiderato
            if(libro[2] == 'si'):# verifica della disponibilità del libro

                cursorUtenti.execute("SELECT ID, libriPresi FROM utenti")
                idUtenti = cursorUtenti.fetchall()# tutti gli ID degli utenti e il numero di libri prestati vengono inseriti nella lista

                for id in idUtenti:
                    if(id[0] == IDUtente):# ricerca dell'utente che ha richiesto il prestito

                        libriPresi = int(id[1] + 1)# il numero di libri prestati viene aggiornato
                        cursorUtenti.execute("UPDATE utenti SET libriPresi=(%s) WHERE ID=(%s)", (libriPresi, id[0],))# la tabella utenti viene aggiornata
                        dbUtenti.commit()

                        cursorLibri.execute("INSERT INTO libriPrestati(IDUtente, titolo, autore, giorniPrestito) VALUES(%s, %s, %s, 30)", (id[0],libro[0], libro[1],))
                        #all'interno della tabella libriPrestato del database Utenti viene inserito il libro che è stato prestato
                        dbLibri.commit()
                        
                        cursorLibri.execute("UPDATE libri SET disponibilità=('no') WHERE titolo=(%s)", (titolo,))# la disponibilità del libro nella tabella libri viene aggiornata
                        dbLibri.commit()  

                        controllo = True
            else:
                pass # se il libro non viene trovato all'interno della tabella libri del database Libri la ricerca di conclude

    return controllo # variabile che restituisce true se l'operazione di prestito è andata a buon fine

def prestitiUtente(ID):# metodo che restituisce una lista di libri prestati all'utente inserito
    """prestitiUtente

       metodo che restituisce una lista di libri prestati all'utente inserito
    
       :type ID: string
       :param ID: ID dell'utente

       Ritorna una lista di libri di tipo LibroPrestato contenente tutti i libri in fase di prestito
    """
    ID = int(ID)
    libriPrestati = []

    cursorLibri.execute("SELECT * FROM libriPrestati")# attraverso il cursore vengono prelevati dal database tutti i libri prestati con i loro attributi
    libri = cursorLibri.fetchall()

    for libro in libri:
        if(libro[0] == ID):# ricerca dei libri prestati ad un singolo utente
            libriPrestati.append(libro)# il libro trovato viene aggiunto alla lista
    
    return libriPrestati# il metodo ci restituisce la lista libriPrestati

def restituisciPrestito(IDUtente, titolo):# il metodo permettere di restituire un libro preso in prestito
    """restituisciPrestito

       metodo che permette di restituire un libro passandogli l'ID dell'utente che ha fatto il prestito e il titolo del libro
    
       :type IDUtente: string
       :param IDUtente: ID dell'utente

       :type titolo: string
       :param titolo: titolo del libro

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    IDUtente = int(IDUtente)

    cursorLibri.execute("SELECT * FROM libriPrestati")# attraverso il cursore vengono prelevati dal database tutti i libri prestati con i loro attributi
    libri = cursorLibri.fetchall()
    controllo = False

    for libro in libri:
        if(libro[1] == titolo):# ricerca del libro da restituire

            cursorLibri.execute("UPDATE libri SET disponibilità=('si') WHERE titolo=(%s)", (titolo,))# la disponibilità del libro resituito viene aggiornata
            dbLibri.commit()

            cursorLibri.execute("DELETE FROM libriPrestati WHERE titolo=(%s)", (titolo,))# il libro restituito viene eliminata dalla tabella libriPrestati
            dbLibri.commit()

            cursorUtenti.execute("SELECT ID, libriPresi FROM utenti")
            idUtenti = cursorUtenti.fetchall()# tutti gli ID degli utenti e il numero di libri prestati vengono inseriti nella lista

            for id in idUtenti:
                if(id[0] == IDUtente):

                    libriPresi = int(id[1] - 1)
                    cursorUtenti.execute("UPDATE utenti SET libriPresi=(%s) WHERE ID=(%s)", (libriPresi, id[0],))# il numero di libri in prestito all'utente viene aggiornato
                    dbUtenti.commit()

                    controllo = True

    return controllo

def infoUtente(ID):# metodo che permette di restituire tutte le informazioni riguardanti un utente 
    """infoUtente

       metodo che permette di restituire tutte le informazioni riguardanti un utente passando l'ID
    
       :type ID: string
       :param ID: ID dell'utente

       Ritorna una lista contenente le informazioni sull'utente
    """
    infoUtente = []

    cursorUtenti.execute("SELECT * FROM utenti")# attraverso il cursore vengono prelevati dal database tutti gli utenti con i loro attributi
    utenti = cursorUtenti.fetchall()

    for utente in utenti:
        if(utente[2] == int(ID)):
            infoUtente.append(utente)# nella lista vengono inserite le informazioni riguardanti l'utente
    
    return infoUtente# il metodo ci restituisce la lista infoUtente

def aggiungiLibro(titolo, autore):# il metodo permette di aggiungere un libro
    """aggiungiLibro

       metodo che permette di aggiungere un libro al database
    
       :type titolo: string
       :param titolo: titolo del libro da aggiungere al database

       :type autore: string
       :param autore: autore del libro da aggiungere al database

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    titolo = titolo.upper()
    autore = autore.upper()

    cursorLibri.execute("Insert into libri(titolo, autore, disponibilità) values(%s, %s, %s)", (titolo, autore, 'si'))
    # il libro viene inserito nella tabella libri del database Libri con il titolo e l'autore inserito e la disponibilità viene impostata a 'si'
    dbLibri.commit()

    return True

def rimuoviLibro(titolo):# il metodo permette di rimuovere un libro
    """rimuoviLibro

       metodo che permette di rimuovere un libro dal database
    
       :type titolo: string
       :param titolo: titolo del libro da rimuovere dal database

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    titolo = titolo.upper()

    cursorLibri.execute("SELECT * FROM libri")# attraverso il cursore vengono prelevati dal database tutti i libri con i loro attributi
    libri = cursorLibri.fetchall()

    controllo = False
    
    for libro in libri:
        if(libro[0] == titolo):# ricerca del libro da eliminare

            cursorLibri.execute("DELETE FROM libri WHERE titolo=(%s)", (titolo,))# il libro viene eliminato dalla tabella libri
            dbLibri.commit()

            controllo = True

    return controllo

def aggiungiUtente(nome, cognome):# il metodo permette di aggiungere un utente
    """aggiungiUtente

       metodo che permette di aggiungere un utente al database
    
       :type nome: string
       :param nome: nome dell'utente da aggiungere al database

       :type cognome: string
       :param cognome: cognome dell'utente da aggiungere al database

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    nome = nome.upper()
    cognome = cognome.upper()
    ID = random.randint(10000000, 100000000)# l'ID viene generato attraverso random
    
    while ID in IDUtenti():# controllo sull'ID in modo che non sia già esistente
        ID = random.randint(10000000, 100000000)

    cursorUtenti.execute("Insert into utenti(nome, cognome, ID, libriPresi) values(%s, %s, %s, %s)", (nome, cognome, ID, 0))
    # l'utente viene inserito nella tabella utenti del database Utenti e i libriPresi vengono impostato a '0'
    dbUtenti.commit()

    return True

def rimuoviUtente(ID):# metodo che permette di rimuovere un utente
    """rimuoviUtente

       metodo che permette di rimuovere un utente dal database
    
       :type ID: string
       :param ID: ID dell'utente da rimuovere dal database

       Ritorna un boolean per verificare il corretto funzionamento della funzione
    """
    ID = int(ID)

    cursorUtenti.execute("SELECT * FROM utenti")# attraverso il cursore vengono prelevati dal database tutti gli utenti con i loro attributi
    utenti = cursorUtenti.fetchall()

    controllo = False

    for utente in utenti:
        if(utente[2] == ID):# ricerca dell'utente

            cursorUtenti.execute("DELETE FROM utenti WHERE ID=(%s)", (ID,))# l'utente viene eliminato dalla tabella utenti del database Utenti
            dbUtenti.commit()

            controllo = True

    return controllo

def getLibri():# metodo che restituisce una lista di tutti i libri appartenenti alla biblioteca
    """getLibri

       metodo che restituisce una lista di libri presenti nel database
    
       Ritorna una lista di libri di tipo Libro
    """
    cursorLibri.execute("SELECT * FROM libri")
    libri = cursorLibri.fetchall()

    listaLibri = []

    for libro in libri:
        listaLibri.append(Libro(str(libro[0]), str(libro[1]), str(libro[2])))

    return listaLibri

def getLibriPrestati():# # metodo che restituisce una lista di tutti i libri prestati dalla biblioteca
    """getLibriPrestati

       metodo che restituisce una lista di tutti i libri prestati dalla biblioteca

       Ritorna una lista di libri di tipo LibroPrestato
    """
    libriPrestati = []

    cursorLibri.execute("SELECT * FROM libriPrestati")
    libri = cursorLibri.fetchall()
    
    for libro in libri:
        libriPrestati.append(LibroPrestato(str(libro[0]), libro[1], libro[2], str(libro[3])))
    
    return libriPrestati

def getUtenti():# metodo che resituisce una lista di tutti gli utenti registrati alla biblioteca
    """getUtenti

       metodo che restituisce una lista di tutti gli utenti presenti nel database
    
       Ritorna una lista di utenti di tipo Utente
    """
    listaUtenti = []
    
    cursorUtenti.execute("SELECT * FROM utenti")
    utenti = cursorUtenti.fetchall()

    for utente in utenti:
        listaUtenti.append(Utente(utente[0], utente[1], str(utente[2]), str(utente[3])))

    return listaUtenti
