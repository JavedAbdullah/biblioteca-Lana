# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import funzioni as f

stylesheet = """

    QTabBar::tab:selected {background: #ffaa00;}
    QTabWidget>QWidget>QWidget{background: #484443;}
    QTabBar::tab:selected { color: white; }

    """

pagina1 = [0,0]
pagina2 = [0,0]
pagina3 = [0]
pagina4 = [0]

class Ui_Grafica(object):
    def setupUi(self, Grafica):
        Grafica.setObjectName("Grafica")
        Grafica.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Grafica.setWindowIcon(icon)


        ### pagina 1 -> prenotazioni
        self.tabWidget = QtWidgets.QTabWidget(Grafica)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet(stylesheet)

        self.tab_prenota = QtWidgets.QWidget()
        self.tab_prenota.setObjectName("tab_prenota")
        self.linea_cercaUtenteP1 = QtWidgets.QLineEdit(self.tab_prenota)
        self.linea_cercaUtenteP1.setGeometry(QtCore.QRect(40, 30, 601, 31))
        self.linea_cercaUtenteP1.setObjectName("linea_cercaUtenteP1")
        self.btn_cercaNUP1 = QtWidgets.QPushButton(self.tab_prenota)
        self.btn_cercaNUP1.setGeometry(QtCore.QRect(670, 30, 81, 31))
        self.btn_cercaNUP1.setObjectName("btn_cercaNUP1")


        self.tbl_utentiP1 = QtWidgets.QTableWidget(self.tab_prenota)
        self.tbl_utentiP1.setGeometry(QtCore.QRect(40, 80, 711, 111))
        self.tbl_utentiP1.setObjectName("tbl_utentiP1")
        self.tbl_libriP1 = QtWidgets.QTableWidget(self.tab_prenota)
        self.tbl_libriP1.setGeometry(QtCore.QRect(40, 320, 711, 141))
        self.tbl_libriP1.setObjectName("tbl_libriP1")
        self.btn_prenotaP1 = QtWidgets.QPushButton(self.tab_prenota)
        self.btn_prenotaP1.setGeometry(QtCore.QRect(300, 520, 191, 41))
        self.btn_prenotaP1.setObjectName("btn_prenotaP1")

        self.linea_cercaLibroP1 = QtWidgets.QLineEdit(self.tab_prenota)
        self.linea_cercaLibroP1.setGeometry(QtCore.QRect(40, 270, 601, 31))
        self.linea_cercaLibroP1.setObjectName("linea_cercaLibroP1")
        self.btn_cercaNLP1 = QtWidgets.QPushButton(self.tab_prenota)
        self.btn_cercaNLP1.setGeometry(QtCore.QRect(660, 270, 91, 31))
        self.btn_cercaNLP1.setObjectName("btn_cercaNLP1")

        self.lbl_nomeUtenteP1 = QtWidgets.QLabel(self.tab_prenota)
        self.lbl_nomeUtenteP1.setGeometry(QtCore.QRect(40, 10, 91, 16))
        self.lbl_nomeUtenteP1.setObjectName("lbl_nomeUtenteP1")
        self.lbl_nomeLibroP1 = QtWidgets.QLabel(self.tab_prenota)
        self.lbl_nomeLibroP1.setGeometry(QtCore.QRect(40, 245, 61, 16))
        self.lbl_nomeLibroP1.setObjectName("lbl_nomeLibroP1")
        self.btn_scegliUtenteP1 = QtWidgets.QPushButton(self.tab_prenota)
        self.btn_scegliUtenteP1.setGeometry(QtCore.QRect(40, 200, 711, 31))
        self.btn_scegliUtenteP1.setObjectName("btn_scegliUtenteP1")

        self.btn_scegliLibroP1 = QtWidgets.QPushButton(self.tab_prenota)
        self.btn_scegliLibroP1.setGeometry(QtCore.QRect(40, 470, 711, 31))
        self.btn_scegliLibroP1.setObjectName("btn_scegliLibroP1")

        self.lbl_utenteSceltoP1 = QtWidgets.QLabel(self.tab_prenota)
        self.lbl_utenteSceltoP1.setGeometry(QtCore.QRect(420, 230, 331, 20))
        self.lbl_utenteSceltoP1.setObjectName("lbl_utenteSceltoP1")

        self.lbl_libroSceltoP1 = QtWidgets.QLabel(self.tab_prenota)
        self.lbl_libroSceltoP1.setGeometry(QtCore.QRect(420, 499, 331, 21))
        self.lbl_libroSceltoP1.setObjectName("lbl_libroSceltoP1")

        self.btn_cercaNUP1.setStyleSheet("background-color: #ffaa00")
        self.btn_prenotaP1.setStyleSheet("background-color: #ffaa00")
        self.btn_cercaNLP1.setStyleSheet("background-color: #ffaa00")
        self.lbl_nomeUtenteP1.setStyleSheet('QLabel {color: white;}')
        self.lbl_nomeLibroP1.setStyleSheet('QLabel {color: white;}')
        self.btn_scegliUtenteP1.setStyleSheet("background-color: #ffaa00")
        self.btn_scegliLibroP1.setStyleSheet("background-color: #ffaa00")
        self.lbl_utenteSceltoP1.setStyleSheet('QLabel {color: white;}')
        self.lbl_libroSceltoP1.setStyleSheet('QLabel {color: white;}')

        # cerca nome utente passando il widget di testo e la tabella degli utenti
        self.btn_cercaNUP1.clicked.connect(lambda: f.setTableUtenti(self.linea_cercaUtenteP1.text(),self.tbl_utentiP1))
        # cerca nome libro passando il widget di testo e la tabella dei libri
        self.btn_cercaNLP1.clicked.connect(lambda: f.setTableLibri(self.linea_cercaLibroP1.text(),self.tbl_libriP1))
        # mette nella variabile pagina1[0] l'id dell'utente selezionato
        self.btn_scegliUtenteP1.clicked.connect(lambda: f.setInfoLibroeUtente(pagina1,0, self.tbl_utentiP1.currentItem()))
        # mette nella variabile pagina[1] il titolo del libro selezionato
        self.btn_scegliLibroP1.clicked.connect(lambda: f.setInfoLibroeUtente(pagina1,1, self.tbl_libriP1.currentItem()))
        # prenota il libro avente titolo pagina1[1] e id utente pagina[0]
        self.btn_prenotaP1.clicked.connect(lambda: f.prenotaLibro(pagina1))


        ### pagina 2 -> restituzioni
        self.tabWidget.addTab(self.tab_prenota, "")
        self.tab_restituisci = QtWidgets.QWidget()
        self.tab_restituisci.setObjectName("tab_restituisci")
        self.linea_cercaUtenteP2 = QtWidgets.QLineEdit(self.tab_restituisci)
        self.linea_cercaUtenteP2.setGeometry(QtCore.QRect(40, 30, 601, 31))
        self.linea_cercaUtenteP2.setObjectName("linea_cercaUtenteP2")

        self.btn_cercaUtenteP2 = QtWidgets.QPushButton(self.tab_restituisci)
        self.btn_cercaUtenteP2.setGeometry(QtCore.QRect(670, 30, 81, 31))
        self.btn_cercaUtenteP2.setObjectName("btn_cercaUtenteP2")

        self.btn_restituisciP2 = QtWidgets.QPushButton(self.tab_restituisci)
        self.btn_restituisciP2.setGeometry(QtCore.QRect(300, 500, 191, 41))
        self.btn_restituisciP2.setObjectName("btn_restituisciP2")

        self.lbl_nomeUtenteP2 = QtWidgets.QLabel(self.tab_restituisci)
        self.lbl_nomeUtenteP2.setGeometry(QtCore.QRect(40, 10, 71, 16))
        self.lbl_nomeUtenteP2.setObjectName("lbl_nomeUtenteP2")

        self.lbl_libriUtenteP2 = QtWidgets.QLabel(self.tab_restituisci)
        self.lbl_libriUtenteP2.setGeometry(QtCore.QRect(40, 240, 81, 21))
        self.lbl_libriUtenteP2.setObjectName("lbl_libriUtenteP2")

        self.btn_scegliUtenteP2 = QtWidgets.QPushButton(self.tab_restituisci)
        self.btn_scegliUtenteP2.setGeometry(QtCore.QRect(40, 200, 711, 31))
        self.btn_scegliUtenteP2.setObjectName("btn_scegliUtenteP2")

        self.lbl_utenteSceltoP2 = QtWidgets.QLabel(self.tab_restituisci)
        self.lbl_utenteSceltoP2.setGeometry(QtCore.QRect(420, 230, 331, 20))
        self.lbl_utenteSceltoP2.setObjectName("lbl_utenteSceltoP2")

        self.tbl_utentiP2 = QtWidgets.QTableWidget(self.tab_restituisci)
        self.tbl_utentiP2.setGeometry(QtCore.QRect(40, 80, 711, 111))
        self.tbl_utentiP2.setObjectName("tbl_utentiP2")
        self.tbl_utentiP2.setColumnCount(0)
        self.tbl_utentiP2.setRowCount(0)
        self.tbl_libriP2 = QtWidgets.QTableWidget(self.tab_restituisci)
        self.tbl_libriP2.setGeometry(QtCore.QRect(40, 270, 711, 171))
        self.tbl_libriP2.setObjectName("tbl_libriP2")
        self.tbl_libriP2.setColumnCount(0)
        self.tbl_libriP2.setRowCount(0)

        self.btn_scegliLibroP2 = QtWidgets.QPushButton(self.tab_restituisci)
        self.btn_scegliLibroP2.setGeometry(QtCore.QRect(40, 450, 711, 31))
        self.btn_scegliLibroP2.setObjectName("btn_scegliLibroP2")


        self.lbl_nomeUtenteP2.setStyleSheet('QLabel {color: white;}')
        self.btn_cercaUtenteP2.setStyleSheet("background-color: #ffaa00")
        self.btn_restituisciP2.setStyleSheet("background-color: #ffaa00")
        self.lbl_libriUtenteP2.setStyleSheet('QLabel {color: white;}')
        self.btn_scegliUtenteP2.setStyleSheet("background-color: #ffaa00")
        self.lbl_utenteSceltoP2.setStyleSheet('QLabel {color: white;}')
        self.btn_scegliLibroP2.setStyleSheet("background-color: #ffaa00")


        # cerca nome utente passando il widget di testo e la tabella degli utenti
        self.btn_cercaUtenteP2.clicked.connect(lambda: f.setTableUtenti(self.linea_cercaUtenteP2.text(), self.tbl_utentiP2))
        # conferma l'utente scelto e aggiorna la tabella per visualizzare i suoi libri
        self.btn_scegliUtenteP2.clicked.connect(lambda: f.libriInPrestito(pagina2, self.tbl_utentiP2.currentItem(), self.tbl_libriP2))
        # inserisce nella variabile pagina2[1] il titolo del libro scelto
        self.btn_scegliLibroP2.clicked.connect(lambda: f.setInfoLibroeUtente(pagina2,1, self.tbl_libriP2.currentItem()))
        # restituisce il libro pagina2[1] di pagina2[0]
        self.btn_restituisciP2.clicked.connect(lambda: f.restituisciLibro(pagina2))



        ### pagina 3 -> controllo database dei libri
        self.tabWidget.addTab(self.tab_restituisci, "")
        self.tab_database = QtWidgets.QWidget()
        self.tab_database.setObjectName("tab_database")
        self.linea_AutoreP3 = QtWidgets.QLineEdit(self.tab_database)
        self.linea_AutoreP3.setGeometry(QtCore.QRect(40, 70, 151, 31))
        self.linea_AutoreP3.setObjectName("linea_AutoreP3")
        self.linea_TitoloP3 = QtWidgets.QLineEdit(self.tab_database)
        self.linea_TitoloP3.setGeometry(QtCore.QRect(230, 70, 151, 31))
        self.linea_TitoloP3.setObjectName("linea_TitoloP3")

        self.btn_aggiungiLibroP3 = QtWidgets.QPushButton(self.tab_database)
        self.btn_aggiungiLibroP3.setGeometry(QtCore.QRect(410, 70, 91, 31))
        self.btn_aggiungiLibroP3.setObjectName("btn_aggiungiLibroP3")

        self.lbl_autoreP3 = QtWidgets.QLabel(self.tab_database)
        self.lbl_autoreP3.setGeometry(QtCore.QRect(40, 30, 81, 31))
        self.lbl_autoreP3.setObjectName("lbl_autoreP3")

        self.lbl_titoloP3 = QtWidgets.QLabel(self.tab_database)
        self.lbl_titoloP3.setGeometry(QtCore.QRect(230, 30, 71, 31))
        self.lbl_titoloP3.setObjectName("lbl_titoloP3")

        self.linea_CercaLibroP3 = QtWidgets.QLineEdit(self.tab_database)
        self.linea_CercaLibroP3.setGeometry(QtCore.QRect(40, 130, 611, 31))
        self.linea_CercaLibroP3.setObjectName("linea_CercaLibroP3")

        self.btn_cercaLibroP3 = QtWidgets.QPushButton(self.tab_database)
        self.btn_cercaLibroP3.setGeometry(QtCore.QRect(680, 130, 71, 31))
        self.btn_cercaLibroP3.setObjectName("btn_cercaLibroP3")

        self.tbl_libriP3 = QtWidgets.QTableWidget(self.tab_database)
        self.tbl_libriP3.setGeometry(QtCore.QRect(40, 190, 711, 221))
        self.tbl_libriP3.setObjectName("tbl_libriP3")
        self.tbl_libriP3.setColumnCount(0)
        self.tbl_libriP3.setRowCount(0)

        self.btn_rimuoviLibroP3 = QtWidgets.QPushButton(self.tab_database)
        self.btn_rimuoviLibroP3.setGeometry(QtCore.QRect(300, 500, 191, 41))
        self.btn_rimuoviLibroP3.setObjectName("btn_rimuoviLibroP3")

        self.btn_scegliLibroP3 = QtWidgets.QPushButton(self.tab_database)
        self.btn_scegliLibroP3.setGeometry(QtCore.QRect(40, 430, 711, 31))
        self.btn_scegliLibroP3.setObjectName("btn_scegliLibroP3")

        self.lbl_titoloP3.setStyleSheet('QLabel {color: white;}')
        self.lbl_autoreP3.setStyleSheet('QLabel {color: white;}')
        self.btn_aggiungiLibroP3.setStyleSheet("background-color: #ffaa00")
        self.btn_cercaLibroP3.setStyleSheet("background-color: #ffaa00")
        self.btn_rimuoviLibroP3.setStyleSheet("background-color: #ffaa00")
        self.btn_scegliLibroP3.setStyleSheet("background-color: #ffaa00")

        # aggiunge il libro passando il titolo e l'autore dai widget di testo
        self.btn_aggiungiLibroP3.clicked.connect(lambda: f.aggiungiLibroDatabase(self.linea_TitoloP3, self.linea_AutoreP3))
        # cerca il libro passando il titolo e visualizzalo nella tabella che viene passata
        self.btn_cercaLibroP3.clicked.connect(lambda: f.setTableLibri(self.linea_CercaLibroP3.text(),self.tbl_libriP3)) # bottone cerca per titolo libro
        # imposta il valore di pagina3 al titolo del libro
        self.btn_scegliLibroP3.clicked.connect(lambda: f.setLibro(pagina3, self.tbl_libriP3.currentItem()))
        # rimuove il libro passandogli il titolo
        self.btn_rimuoviLibroP3.clicked.connect(lambda: f.rimuoviLibroDatabase(pagina3))


        ### pagina 4 -> controllo database degli utenti
        self.tabWidget.addTab(self.tab_database, "")
        self.tab_utenti = QtWidgets.QWidget()
        self.tab_utenti.setObjectName("tab_utenti")
        self.linea_NomeP4 = QtWidgets.QLineEdit(self.tab_utenti)
        self.linea_NomeP4.setGeometry(QtCore.QRect(40, 40, 181, 31))
        self.linea_NomeP4.setObjectName("linea_NomeP4")
        self.linea_CognomeP4 = QtWidgets.QLineEdit(self.tab_utenti)
        self.linea_CognomeP4.setGeometry(QtCore.QRect(260, 40, 171, 31))
        self.linea_CognomeP4.setObjectName("linea_CognomeP4")

        self.btn_aggiungiUtenteP4 = QtWidgets.QPushButton(self.tab_utenti)
        self.btn_aggiungiUtenteP4.setGeometry(QtCore.QRect(470, 40, 111, 31))
        self.btn_aggiungiUtenteP4.setObjectName("btn_aggiungiUtenteP4")

        self.lbl_nomeP4 = QtWidgets.QLabel(self.tab_utenti)
        self.lbl_nomeP4.setGeometry(QtCore.QRect(40, 13, 47, 20))
        self.lbl_nomeP4.setObjectName("lbl_nomeP4")

        self.lbl_cognomeP4 = QtWidgets.QLabel(self.tab_utenti)
        self.lbl_cognomeP4.setGeometry(QtCore.QRect(260, 10, 47, 21))
        self.lbl_cognomeP4.setObjectName("lbl_cognomeP4")

        self.linea_cercaUtenteP4 = QtWidgets.QLineEdit(self.tab_utenti)
        self.linea_cercaUtenteP4.setGeometry(QtCore.QRect(40, 110, 561, 31))
        self.linea_cercaUtenteP4.setObjectName("linea_cercaUtenteP4")

        self.btn_rimuoviUtenteP4 = QtWidgets.QPushButton(self.tab_utenti)
        self.btn_rimuoviUtenteP4.setGeometry(QtCore.QRect(300, 500, 191, 41))
        self.btn_rimuoviUtenteP4.setObjectName("btn_rimuoviUtenteP4")

        self.tbl_utentiP4 = QtWidgets.QTableWidget(self.tab_utenti)
        self.tbl_utentiP4.setGeometry(QtCore.QRect(40, 160, 711, 251))
        self.tbl_utentiP4.setObjectName("tbl_utentiP4")
        self.tbl_utentiP4.setColumnCount(0)
        self.tbl_utentiP4.setRowCount(0)

        self.btn_cercaUtenteP4 = QtWidgets.QPushButton(self.tab_utenti)
        self.btn_cercaUtenteP4.setGeometry(QtCore.QRect(640, 110, 111, 31))
        self.btn_cercaUtenteP4.setObjectName("btn_cercaUtenteP4")

        self.btn_scegliUtenteP4 = QtWidgets.QPushButton(self.tab_utenti)
        self.btn_scegliUtenteP4.setGeometry(QtCore.QRect(40, 440, 711, 31))
        self.btn_scegliUtenteP4.setObjectName("btn_scegliUtenteP4")

        self.lbl_cognomeP4.setStyleSheet('QLabel {color: white;}')
        self.lbl_nomeP4.setStyleSheet('QLabel {color: white;}')
        self.btn_aggiungiUtenteP4.setStyleSheet("background-color: #ffaa00")
        self.btn_cercaUtenteP4.setStyleSheet("background-color: #ffaa00")
        self.btn_scegliUtenteP4.setStyleSheet("background-color: #ffaa00")
        self.btn_rimuoviUtenteP4.setStyleSheet("background-color: #ffaa00")


        # aggiunge un utente al database passandogli il nome ed il cognome
        self.btn_aggiungiUtenteP4.clicked.connect(lambda: f.aggiungiUtenteDatabase(self.linea_NomeP4, self.linea_CognomeP4))
        # cerca l'utente in base al nome
        self.btn_cercaUtenteP4.clicked.connect(lambda: f.setTableUtenti(self.linea_cercaUtenteP4.text(), self.tbl_utentiP4))
        # scegli l'utente di cui viene selezionato l'id e mettilo nella variabile pagina4
        self.btn_scegliUtenteP4.clicked.connect(lambda: f.setUtente(pagina4, self.tbl_utentiP4.currentItem().text()))
        # rimuovi l'utente in base all'id che si trova nella variabile pagina4
        self.btn_rimuoviUtenteP4.clicked.connect(lambda: f.rimuoviUtenteDatabase(pagina4))


        ### pagina 5 -> informazioni ogni database
        self.tabWidget.addTab(self.tab_utenti, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setEnabled(True)
        self.tab_info.setAutoFillBackground(False)
        self.tab_info.setObjectName("tab_info")
        self.tbl_infoP5 = QtWidgets.QTableWidget(self.tab_info)
        self.tbl_infoP5.setGeometry(QtCore.QRect(40, 210, 711, 341))
        self.tbl_infoP5.setObjectName("tbl_infoP5")
        self.tbl_infoP5.setColumnCount(0)
        self.tbl_infoP5.setRowCount(0)
        self.btn_mostraTuttiLibriP5 = QtWidgets.QPushButton(self.tab_info)
        self.btn_mostraTuttiLibriP5.setGeometry(QtCore.QRect(40, 40, 231, 31))
        self.btn_mostraTuttiLibriP5.setObjectName("btn_mostraTuttiLibriP5")
        self.btn_mostraTuttiUtentiP5 = QtWidgets.QPushButton(self.tab_info)
        self.btn_mostraTuttiUtentiP5.setGeometry(QtCore.QRect(520, 100, 231, 31))
        self.btn_mostraTuttiUtentiP5.setObjectName("btn_mostraTuttiUtentiP5")
        self.btn_mostraLibriDisponibiliP5 = QtWidgets.QPushButton(self.tab_info)
        self.btn_mostraLibriDisponibiliP5.setGeometry(QtCore.QRect(520, 40, 231, 31))
        self.btn_mostraLibriDisponibiliP5.setObjectName("btn_mostraLibriDisponibiliP5")
        self.btn_mostraLibriPrestatiP5 = QtWidgets.QPushButton(self.tab_info)
        self.btn_mostraLibriPrestatiP5.setGeometry(QtCore.QRect(40, 100, 231, 31))
        self.btn_mostraLibriPrestatiP5.setObjectName("btn_mostraLibriPrestatiP5")
        self.tabWidget.addTab(self.tab_info, "")

        self.btn_mostraLibriDisponibiliP5.setStyleSheet("background-color: #ffaa00")
        self.btn_mostraLibriPrestatiP5.setStyleSheet("background-color: #ffaa00")
        self.btn_mostraTuttiLibriP5.setStyleSheet("background-color: #ffaa00")
        self.btn_mostraTuttiUtentiP5.setStyleSheet("background-color: #ffaa00")

        # mostra tutti i libri del database
        self.btn_mostraTuttiLibriP5.clicked.connect(lambda: f.mostraTuttiLibri(self.tbl_infoP5))
        # mostra tutti i libri che sono in fase di prestito
        self.btn_mostraLibriPrestatiP5.clicked.connect(lambda: f.mostraLibriInPrestito(self.tbl_infoP5))
        # mostra tutti i libri disponibili alla prenotazione
        self.btn_mostraLibriDisponibiliP5.clicked.connect(lambda: f.mostraLibriDisponibili(self.tbl_infoP5))
        # mostra tutti gli utenti disponibili nel database
        self.btn_mostraTuttiUtentiP5.clicked.connect(lambda: f.mostraUtenti(self.tbl_infoP5))

        self.retranslateUi(Grafica)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Grafica)

    def retranslateUi(self, Grafica):
        _translate = QtCore.QCoreApplication.translate
        Grafica.setWindowTitle(_translate("Grafica", "Biblioteca Lana Rhoades"))
        Grafica.setMaximumWidth(Grafica.width())
        Grafica.setMaximumHeight(Grafica.height())
        self.btn_cercaNUP1.setText(_translate("Grafica", "CERCA"))
        self.btn_prenotaP1.setText(_translate("Grafica", "Prenota"))
        self.btn_cercaNLP1.setText(_translate("Grafica", "CERCA"))
        self.lbl_nomeUtenteP1.setText(_translate("Grafica", "Nome Utente"))
        self.lbl_nomeLibroP1.setText(_translate("Grafica", "Nome Libro"))
        self.btn_scegliUtenteP1.setText(_translate("Grafica", "Scegli Utente"))
        self.btn_scegliLibroP1.setText(_translate("Grafica", "Scegli Libro"))
        self.lbl_utenteSceltoP1.setText(_translate("Grafica", "<html><head/><body><p align=\"right\">SELEZIONA ID</p></body></html>"))
        self.lbl_libroSceltoP1.setText(_translate("Grafica", "<html><head/><body><p align=\"right\">SELEZIONA TITOLO</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prenota), _translate("Grafica", "Prenota"))
        self.btn_cercaUtenteP2.setText(_translate("Grafica", "CERCA"))
        self.btn_restituisciP2.setText(_translate("Grafica", "RESTITUISCI"))
        self.lbl_nomeUtenteP2.setText(_translate("Grafica", "Nome Utente"))
        self.lbl_libriUtenteP2.setText(_translate("Grafica", "Libri in possesso"))
        self.btn_scegliUtenteP2.setText(_translate("Grafica", "Scegli Utente"))
        self.lbl_utenteSceltoP2.setText(_translate("Grafica", "<html><head/><body><p align=\"right\">SELEZIONA ID</p></body></html>"))
        self.btn_scegliLibroP2.setText(_translate("Grafica", "Scegli Libro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_restituisci), _translate("Grafica", "Restituisci"))
        self.btn_aggiungiLibroP3.setText(_translate("Grafica", "AGGIUNGI"))
        self.lbl_autoreP3.setText(_translate("Grafica", "Autore"))
        self.lbl_titoloP3.setText(_translate("Grafica", "Titolo"))
        self.btn_cercaLibroP3.setText(_translate("Grafica", "CERCA"))
        self.btn_rimuoviLibroP3.setText(_translate("Grafica", "RIMUOVI"))
        self.btn_scegliLibroP3.setText(_translate("Grafica", "Scegli Libro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_database), _translate("Grafica", "Libri"))
        self.btn_aggiungiUtenteP4.setText(_translate("Grafica", "Aggiungi utente"))
        self.lbl_nomeP4.setText(_translate("Grafica", "Nome"))
        self.lbl_cognomeP4.setText(_translate("Grafica", "Cognome"))
        self.btn_cercaUtenteP4.setText(_translate("Grafica", "Cerca"))
        self.btn_rimuoviUtenteP4.setText(_translate("Grafica", "RIMUOVI"))
        self.btn_scegliUtenteP4.setText(_translate("Grafica", "Scegli Utente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_utenti), _translate("Grafica", "Utenti"))
        self.btn_mostraTuttiLibriP5.setText(_translate("Grafica", "Mostra Tutti Libri"))
        self.btn_mostraTuttiUtentiP5.setText(_translate("Grafica", "Mostra Tutti Gli Utenti"))
        self.btn_mostraLibriDisponibiliP5.setText(_translate("Grafica", "Mostra Tutti Libri Disponibili"))
        self.btn_mostraLibriPrestatiP5.setText(_translate("Grafica", "Mostra Tutti Libri Prestati"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), _translate("Grafica", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grafica = QtWidgets.QWidget()
    ui = Ui_Grafica()
    ui.setupUi(Grafica)
    Grafica.show()
    sys.exit(app.exec_())
