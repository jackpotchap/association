# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la classe casier


from PyQt5.QtGui import QStandardItemModel

import cour
# Importer la boite de dialogue
import cour_class
import etudiant
import interfacecasier

# Import ls_Etudiants

from logique import ls_Etudiants


# Importer le main

from main import *
#Fonctions cacher labels erreur

def cour_create(p_sigle_cours: str = "", p_titre_cours: str = "", p_nb_heure_de_cours: str = ""):

    cour_T = cour_class.Cour()

    try:
        cour_T.Nb_heure_de_cours = int(p_nb_heure_de_cours)
    except:
        print("heure invalide")
    else:
        if cour_T.Nb_heure_de_cours == -1:
            print("heure doit etre plus grand que zero")

    cour_T.Sigle_cours = p_sigle_cours
    if cour_T.Sigle_cours == "":
        print("Sigle_cours invalide doit etre d eformat A0000")

    cour_T.Titre_cours = p_titre_cours
    if cour_T.Titre_cours == "":
        print("titre dpot etre plis petit ou = a 60")

    return cour_T

ls_cour = {"prog":cour_create("A1000", "prog", "70"), "outils carriere":cour_create("B2000","outils carriere", "40"), "édu":cour_create("C3000", "édu", "20")}
print(ls_cour)
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
        for c in ls_cour:

            self.comboBox_cour.addItem(c)

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):

        valide = False
        e = etudiant.Etudiant()
        num = self.lineEdit_numero.text()
        try:
            e.NumEtud = num
        except:
            self.label_erreur_numero.setVisible(True)

        else:
            if e.NumEtud == "":
                self.label_erreur_numero.setVisible(True)
            else:
                for e in ls_Etudiants:
                    if e.NumEtud == num:
                        valide = True
                        if ls_cour[self.comboBox_cour.currentText()] in e.Ls_cour:
                            pass
                        else:
                            e.Ls_cour.append(ls_cour[self.comboBox_cour.currentText()])


                        self.listView_cour_etudiant.clearMask()

                        model = QStandardItemModel()
                        self.listView_cour_etudiant.setModel(model)
                        for c in e.Ls_cour:

                            model.appendRow(QStandardItem(c.__str__()))

                if valide is False:
                    self.label_erreur_Etu_Inexistant.setVisible(True)



    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
            """
            méthode boutton quitter
            :return:None
            """
            self.close()


