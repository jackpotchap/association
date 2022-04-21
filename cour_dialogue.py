# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la classe casier
import cour
# Importer la boite de dialogue

import interfacecasier

# Import ls_Etudiants

from logique import ls_Etudiants


# Importer le main

from main import *
#Fonctions cacher labels erreur

def cacher_labels_erreur(objet):
    objet.label_erreur_Etu_Inexistant.setVisible(False)
    objet.label_erreur_numero.setVisible(False)
    objet.label_erreur_Etu_Existe.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE popup_casier ######
######################################################

class PopUpCour(QtWidgets.QDialog, cour.Ui_Dialog):
    def __init__(self,parent=None):
        super(PopUpCour, self).__init__(parent)

        self.setupUi(self)

        self.setWindowTitle("Casier des étudiants")
        cacher_labels_erreur(self)




