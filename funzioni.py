import biblioteca
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

# aggiorna la tabella dei libri da visualizzare passando il titolo del libro e la tabella in cui visualizzare
def setTableLibri(titolo, tabella):
    """setTableLibri

       imposta i valori della tabella dei libri

       :type titolo: string
       :param titolo: titolo del libro

       :type tabella: table widget
       :param tabella: tabella di visualizzazione
    """
    titolo = titolo.upper()

    listaLibri = biblioteca.cercaPerTitolo(titolo) # restituisce una lista dei libri con quel nome

    tabella.setRowCount(len(listaLibri))
    tabella.setColumnCount(3)

    tabella.setColumnWidth(0, 350)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 144)

    if(len(listaLibri)>0):
        for i in range(len(listaLibri)):
            titolo = listaLibri[i].titolo.strip()
            autore = listaLibri[i].autore.strip()
            disponibilita = listaLibri[i].disponibilita.strip()

            tabella.setItem(i, 0, QTableWidgetItem(titolo))
            tabella.setItem(i, 1, QTableWidgetItem(autore))
            tabella.setItem(i, 2, QTableWidgetItem(disponibilita))
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Errore")
        msg.setText("libro non trovato")
        x = msg.exec_()
# aggiorna la tabella degli utenti da visualizzare passando l'id dell'utente e la tabella in cui visualizzare
def setTableUtenti(idUtente, tabella):
    """setTableUtenti

       imposta i valori della tabella degli utenti

       :type idUtente: string
       :param idUtente: ID dell'utente

       :type tabella: table widget
       :param tabella: tabella di visualizzazione
    """
    idUtente = idUtente.upper()
    listaUtenti = biblioteca.cercaPerNomeUtente(idUtente)# restituisce una lista degli utenti con quell'id

    tabella.setRowCount(len(listaUtenti))
    tabella.setColumnCount(4)

    tabella.setColumnWidth(0, 200)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 200)
    tabella.setColumnWidth(2, 194)

    if(len(listaUtenti)>0):
        for i in range(len(listaUtenti)):
            nome = listaUtenti[i].nome.strip()
            cognome = listaUtenti[i].cognome.strip()
            id = listaUtenti[i].id.strip()
            libriPresi = listaUtenti[i].libriPresi.strip()

            tabella.setItem(i, 0, QTableWidgetItem(nome))
            tabella.setItem(i, 1, QTableWidgetItem(cognome))
            tabella.setItem(i, 2, QTableWidgetItem(id))
            tabella.setItem(i, 3, QTableWidgetItem(libriPresi))
    else:
        msg = QMessageBox()
        msg.setWindowTitle("Errore")
        msg.setText("utente non trovato")
        x = msg.exec_()
# imposta nella variabile lista[posizione] (posizione=0 -> utente, posizione=1 -> libro) l'item scelto (id oppure titolo del libro)
def setInfoLibroeUtente(lista,posizione, item):
    """setInfoLibroeUtente

       imposta il libro e l'utente scelto per le operazioni di prenotazione e restituzione dei libri

       :type lista: list
       :param lista: lista che contiene i valori di ID utente e del titolo del libro

       :type posizione: int
       :param tabella: semplice numero che indica dove inserire il valore da memorizzare nella lista (0 -> IDutente, 1 -> titoloLibro)

       :type item: string
       :param item: valore selezionato nella tabella
    """
    try:
        index = item.column()
        item = item.text()

        lista[posizione] = item
        msg = QMessageBox()

        if posizione==0:
            if not item.isalpha():
                infoUtente = biblioteca.infoUtente(item)
                nome = infoUtente[0][0]
                cognome = infoUtente[0][1]

                msg.setWindowTitle(f"successo")
                msg.setText(f"utente selezionato: {nome} {cognome}")

            else:
                msg.setWindowTitle(f"errore")
                msg.setText(f"non hai selezionato l'id!")
        else:
            if index == 0:
                msg.setWindowTitle(f"successo")
                msg.setText(f"libro selezionato: {item}")
            else:
                msg.setWindowTitle(f"errore")
                msg.setText(f"seleziona il titolo!")
    except:
        if posizione == 0:
            msg.setWindowTitle(f"errore")
            msg.setText(f"nessun utente selezionato")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText(f"nessun libro selezionato")
    x = msg.exec_()
# imposta nella variabile pagina[0] il titolo del libro selezionato
def setLibro(pagina, selezione):
    """setLibro

       imposta nella lista pagina[0] il titolo del libro selezionato

       :type pagina: list
       :param pagina: lista che contiene il valore del titolo

       :type selezione: string
       :param selezione: valore selezionato nella tabella
    """
    try:
        pagina[0] = selezione.text()
        index = selezione.column() # utile per capire se l'utente ha selezionato la colonna giusta
        msg = QMessageBox()
        if index == 0:
            msg.setWindowTitle(f"successo")
            msg.setText(f"libro selezionato: {pagina[0]}")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText(f"seleziona il titolo!")
    except:
        msg.setWindowTitle(f"errore")
        msg.setText("nessun libro selezionato")
    x = msg.exec_()
# imposta nella variabile pagina[0] l'id dell'utente
def setUtente(pagina, selezione):
    """setUtente

       imposta nella variabile pagina[0] l'id dell'utente

       :type idUtente: string
       :param idUtente: lista che contiene il valore di ID utente

       :type selezione: string
       :param tabella: valore selezionato nella tabella
    """
    try:
        pagina[0] = selezione
        pagina = pagina[0]
        msg = QMessageBox()
        if not pagina.isalpha():
            msg.setWindowTitle(f"successo")
            msg.setText(f"utente selezionato: {pagina}")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText("non hai selezionato l'id!")
    except:
        msg.setWindowTitle(f"errore")
        msg.setText("nessun utente selezionato")
    x = msg.exec_()
# prenota il libro passando una lista contenente in posizione 0 l'id utente, in posizione 1 il titolo del libro
def prenotaLibro(lista):
    """prenotaLibro

       prenota il libro

       :type lista: list
       :param lista: prenota il libro passando una lista contenente in posizione 0 l'id utente, in posizione 1 il titolo del libro
    """
    id = lista[0]
    libro = lista[1]
    msg = QMessageBox()
    if id == 0 or libro == 0:
        msg.setWindowTitle("errore")
        msg.setText("utente o libro non selezionato")
    else:
        controllo = biblioteca.prendiPrestito(libro, id)
        if controllo:
            infoUtente = biblioteca.infoUtente(id)
            nome = infoUtente[0][0]
            cognome = infoUtente[0][1]
            msg.setWindowTitle(f"successo")
            msg.setText(f"libro: {lista[1]} prenotato con successo da {nome} {cognome}")
        else:
            msg.setWindowTitle("errore")
            msg.setText("libro non prenotato")
    x = msg.exec_()
# restituisci il libro passando una lista contenente in posizione 0 l'id utente in posizione 1 il titolo del libro
def restituisciLibro(lista):
    """restituisciLibro

       resituisci il libro

       :type lista: list
       :param lista: restituisci il libro passando una lista contenente in posizione 0 l'id utente in posizione 1 il titolo del libro
    """
    idUtente = lista[0]
    libro = lista[1]

    infoUtente = biblioteca.infoUtente(idUtente)
    nome = infoUtente[0][0]
    cognome = infoUtente[0][1]

    if idUtente == 0 or libro == 0:
        msg = QMessageBox()
        msg.setWindowTitle(f"errore")
        msg.setText(f"utente o libro non selezionato")
        x = msg.exec_()
    else:
        if biblioteca.restituisciPrestito(idUtente, libro):
            msg = QMessageBox()
            msg.setWindowTitle(f"successo")
            msg.setText(f"libro: {lista[1]} restituito con successo da {nome} {cognome}")
            x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle(f"errore")
            msg.setText("errore nella restituzione del libro")
            x = msg.exec_()
# aggiunge un libro al database passandogli titolo ed autore
def aggiungiLibroDatabase(titolo, autore):
    """aggiungiLibroDatabase

       aggiunge un libro al database

       :type titolo: string
       :param titolo: titolo del libro che verrà aggiunto

       :type autore: string
       :param autore: autore del libro che verrà aggiunto
    """
    titolo = titolo.text()
    autore = autore.text()
    msg = QMessageBox()
    if titolo == "" or autore == "":
        msg.setWindowTitle("errore")
        msg.setText("i campi nome e autore non possono essere vuoti")
    else:
        if biblioteca.aggiungiLibro(titolo, autore):
            msg.setWindowTitle("successo")
            msg.setText(f"libro {titolo} di {autore} aggiunto al database")
        else:
            msg.setWindowTitle("errore")
            msg.setText(f"errore nell'aggiunta del libro {titolo}")
    x = msg.exec_()
# rimuovi dal database un libro passandogli il titolo
def rimuoviLibroDatabase(titolo):
    """rimuoviLibroDatabase

       rimuovi un libro dal database

       :type titolo: string
       :param titolo: titolo del libro che verrà rimosso

       :type autore: string
       :param autore: autore del libro che verrà rimosso
    """
    titolo = titolo[0]
    msg = QMessageBox()
    if titolo == 0:
        msg.setWindowTitle(f"errore")
        msg.setText(f"nessun libro selezionato")
    else:
        if biblioteca.rimuoviLibro(titolo):
            msg.setWindowTitle(f"successo")
            msg.setText(f"libro {titolo} rimosso dal database")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText(f"errore nella rimozione del libro")
    x = msg.exec_()
# aggiunge utente al database passandogli nome e cognome
def aggiungiUtenteDatabase(nome, cognome):
    """aggiungiUtenteDatabase

       aggiunge un utente al database

       :type nome: string
       :param nome: nome dell'utente che verrà aggiunto

       :type cognome: string
       :param cognome: cognome dell'utente che verrà aggiunto
    """
    nome = nome.text()
    cognome = cognome.text()
    msg = QMessageBox()
    if nome == "" or cognome == "":
        msg.setWindowTitle(f"errore")
        msg.setText(f"i campi nome e cognome non possono essere vuoti")
    else:
        biblioteca.aggiungiUtente(nome, cognome)
        msg.setWindowTitle(f"successo")
        msg.setText(f"{nome} {cognome} aggiunto al database degli utenti correttamente")
    x = msg.exec_()
# rimuove utente dal database passandogli l'id dell'utente
def rimuoviUtenteDatabase(id):
    """rimuoviUtenteDatabase

       rimuove un utente dal database

       :type id: string
       :param id: id dell'utente che verrà rimosso
    """
    id = id[0]
    msg = QMessageBox()
    if id == 0:
        msg.setWindowTitle(f"errore")
        msg.setText("nessun utente selezionato")
    else:
        if biblioteca.rimuoviUtente(id):
            msg.setWindowTitle(f"successo")
            msg.setText(f"utente {id} rimosso con successo dal database")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText("errore nella rimozione dell'utente")
    x = msg.exec_()
# mostra in una tabella i libri dell'utente con l'id che viene passato e mette nella variabile lista[0] l'id selezionato
def libriInPrestito(lista, id, tabella):
    """libriInPrestito

       mostra in una tabella i libri dell'utente con l'id che viene selezionato nella tabella e lo mette nella variabile lista[0

       :type lista: list
       :param lista: lista che contiene i valori di ID utente e del titolo del libro

       :type id: string
       :param id: id dell'utente selezionato

       :type tabella: widget table
       :param autore: tabella di visualizzazione
    """
    try:
        index = id.column()
        id = id.text()
        lista[0] = id

        infoUtente = biblioteca.infoUtente(id)
        nome = infoUtente[0][0]
        cognome = infoUtente[0][1]

        msg = QMessageBox()

        if index == 2:

            msg.setWindowTitle(f"successo")
            msg.setText(f"utente selezionato: {nome} {cognome}")

            listaLibri = biblioteca.prestitiUtente(id)

            tabella.setRowCount(len(listaLibri))
            tabella.setColumnCount(3)

            tabella.setColumnWidth(0, 350)
            tabella.setColumnWidth(1, 200)
            tabella.setColumnWidth(2, 144)

            if(len(listaLibri)>0):
                for i in range(len(listaLibri)):

                    titolo = listaLibri[i][1]
                    autore = listaLibri[i][2]
                    scadenza = str(listaLibri[i][3])

                    tabella.setItem(i, 0, QTableWidgetItem(titolo))
                    tabella.setItem(i, 1, QTableWidgetItem(autore))
                    tabella.setItem(i, 2, QTableWidgetItem(scadenza))
            else:
                msg.setWindowTitle("Errore")
                msg.setText("libro non trovato")
        else:
            msg.setWindowTitle(f"errore")
            msg.setText(f"non hai selezionato l'id!")
    except:
        msg.setWindowTitle(f"errore")
        msg.setText(f"nessun utente selezionato")

    x = msg.exec_()

def mostraTuttiLibri(tabella):
    """mostraTuttiLibri

       mostra in una tabella tutti i libri presenti nel database

       :type tabella: widget table
       :param tabella: tabella di visualizzazione
    """
    listaLibri = biblioteca.getLibri() # restituisce una lista dei libri con quel nome

    tabella.setRowCount(len(listaLibri))
    tabella.setColumnCount(3)

    tabella.setColumnWidth(0, 350)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 144)

    if(len(listaLibri)>0):
        for i in range(len(listaLibri)):
            titolo = listaLibri[i].titolo.strip()
            autore = listaLibri[i].autore.strip()
            disponibilita = listaLibri[i].disponibilita.strip()

            tabella.setItem(i, 0, QTableWidgetItem(titolo))
            tabella.setItem(i, 1, QTableWidgetItem(autore))
            tabella.setItem(i, 2, QTableWidgetItem(disponibilita))

def mostraLibriInPrestito(tabella):
    """mostraLibriInPrestito

       mostra in una tabella i libri che sono in fase di prestito con l'utente che li ha presi e i giorni mancanti alla scadenza

       :type tabella: widget table
       :param tabella: tabella di visualizzazione
    """
    listaLibri = biblioteca.getLibriPrestati() # restituisce una lista dei libri con quel nome

    tabella.setRowCount(len(listaLibri))
    tabella.setColumnCount(4)

    tabella.setColumnWidth(0, 150)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 200)
    tabella.setColumnWidth(3, 144)

    if(len(listaLibri)>0):
        for i in range(len(listaLibri)):
            persona = listaLibri[i].persona.strip()
            persona = biblioteca.infoUtente(persona)
            persona = persona[0][0]+" "+persona[0][1]
            titolo = listaLibri[i].titolo.strip()
            autore = listaLibri[i].autore.strip()
            scadenza = listaLibri[i].scadenza.strip()

            tabella.setItem(i, 0, QTableWidgetItem(persona))
            tabella.setItem(i, 1, QTableWidgetItem(titolo))
            tabella.setItem(i, 2, QTableWidgetItem(autore))
            tabella.setItem(i, 3, QTableWidgetItem(scadenza+" GIORNI"))

def mostraLibriDisponibili(tabella):
    """mostraLibriDisponibili

       mostra in una tabella i libri disponibili al prestito

       :type tabella: widget table
       :param autore: tabella di visualizzazione
    """
    listaLibri = biblioteca.mostraLibriDisponibili() # restituisce una lista dei libri con quel nome

    tabella.setRowCount(len(listaLibri))
    tabella.setColumnCount(3)

    tabella.setColumnWidth(0, 350)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 144)

    if(len(listaLibri)>0):
        for i in range(len(listaLibri)):
            titolo = listaLibri[i].titolo.strip()
            autore = listaLibri[i].autore.strip()
            disponibilita = listaLibri[i].disponibilita.strip()

            tabella.setItem(i, 0, QTableWidgetItem(titolo))
            tabella.setItem(i, 1, QTableWidgetItem(autore))
            tabella.setItem(i, 2, QTableWidgetItem(disponibilita))

def mostraUtenti(tabella):
    """mostraUtenti

       mostra in una tabella tutti gli utenti presenti nel database

       :type tabella: widget table
       :param autore: tabella di visualizzazione
    """
    listaUtenti = biblioteca.getUtenti()

    tabella.setRowCount(len(listaUtenti))
    tabella.setColumnCount(4)

    tabella.setColumnWidth(0, 200)
    tabella.setColumnWidth(1, 200)
    tabella.setColumnWidth(2, 200)
    tabella.setColumnWidth(2, 194)

    if(len(listaUtenti)>0):
        for i in range(len(listaUtenti)):
            nome = listaUtenti[i].nome.strip()
            cognome = listaUtenti[i].cognome.strip()
            id = listaUtenti[i].id.strip()
            libriPresi = listaUtenti[i].libriPresi.strip()

            tabella.setItem(i, 0, QTableWidgetItem(nome))
            tabella.setItem(i, 1, QTableWidgetItem(cognome))
            tabella.setItem(i, 2, QTableWidgetItem(id))
            tabella.setItem(i, 3, QTableWidgetItem(libriPresi))
