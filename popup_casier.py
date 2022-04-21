# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la classe casier
from casier import *

# Importer la boite de dialogue

import interfacecasier

# Import ls_Etudiants

from logique import ls_Etudiants

# Importer le main

from main import *
#Fonctions cacher labels erreur

def cacher_labels_erreur(objet):
    objet.label_err_cas_format.setVisible(False)
    objet.label_err_cas_nondispo.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE popup_casier ######
######################################################

class PopUpCasier(QtWidgets.QDialog, interfacecasier.Ui_Dialog):
    def __init__(self,p_etudiant,textbroswer ,parent=None):
        super(PopUpCasier, self).__init__(parent)
        self.etudiant = p_etudiant
        self.setupUi(self)
        self.textbroswer = textbroswer
        self.setWindowTitle("Casier des étudiants")
        cacher_labels_erreur(self)


        if self.etudiant.casier.Numero_casier != "":
            self.lineEdit_cas_num.setText(self.etudiant.casier.Numero_casier)
            self.comboBox_cas_taille.setCurrentText(self.etudiant.casier.taille_casier)
            self.comboBox_cas_loc.setCurrentText(self.etudiant.casier.localisation_casier)


    @pyqtSlot()
    def on_pushButton_cas_ajout_clicked(self):
        """
        Méthode du boutton confirmer
        :return:
        """


        # Instanciation d'un casier
        cas = Casier()

        # Entrée de données des attributs de la classe casier

        cas.Numero_casier = self.lineEdit_cas_num.text()
        cas.taille_casier = self.comboBox_cas_taille.currentText()
        cas.localisation_casier = self.comboBox_cas_loc.currentText()

        # Validation
        valid = True


        if cas.Numero_casier == "":
            self.lineEdit_cas_num.clear()
            self.label_err_cas_format.setVisible(True)
            valid = False
        for c in ls_Etudiants:
            if cas.Numero_casier == c.casier.Numero_casier:
                self.label_err_cas_nondispo.setVisible(True)
                valid = False

        if valid == True:
            self.etudiant.casier = cas
            self.textbroswer.clear()
            for elt in ls_Etudiants:


                self.textbroswer.append(elt.__str__())


    @pyqtSlot()
    def on_pushButton_cas_quit_clicked(self):
        """
        méthode boutton quitter
        :return:None
        """
        self.close()

