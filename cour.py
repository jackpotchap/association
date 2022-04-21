# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cour.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(521, 625)
        self.label_numero = QtWidgets.QLabel(Dialog)
        self.label_numero.setGeometry(QtCore.QRect(10, 15, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.lineEdit_numero = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numero.setGeometry(QtCore.QRect(10, 60, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_numero.setFont(font)
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.label_erreur_numero = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero.setEnabled(True)
        self.label_erreur_numero.setGeometry(QtCore.QRect(10, 130, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_numero.setFont(font)
        self.label_erreur_numero.setObjectName("label_erreur_numero")
        self.label_erreur_Etu_Existe = QtWidgets.QLabel(Dialog)
        self.label_erreur_Etu_Existe.setGeometry(QtCore.QRect(10, 110, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Existe.setFont(font)
        self.label_erreur_Etu_Existe.setObjectName("label_erreur_Etu_Existe")
        self.label_erreur_Etu_Inexistant = QtWidgets.QLabel(Dialog)
        self.label_erreur_Etu_Inexistant.setGeometry(QtCore.QRect(10, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Inexistant.setFont(font)
        self.label_erreur_Etu_Inexistant.setObjectName("label_erreur_Etu_Inexistant")
        self.label_cour = QtWidgets.QLabel(Dialog)
        self.label_cour.setGeometry(QtCore.QRect(20, 170, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_cour.setFont(font)
        self.label_cour.setObjectName("label_cour")
        self.comboBox_cour = QtWidgets.QComboBox(Dialog)
        self.comboBox_cour.setGeometry(QtCore.QRect(10, 220, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_cour.setFont(font)
        self.comboBox_cour.setObjectName("comboBox_cour")
        self.pushButton_ajouter = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter.setGeometry(QtCore.QRect(10, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter.setFont(font)
        self.pushButton_ajouter.setObjectName("pushButton_ajouter")
        self.pushButton_quitter = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter.setGeometry(QtCore.QRect(330, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter.setFont(font)
        self.pushButton_quitter.setObjectName("pushButton_quitter")
        self.listView_cour_etudiant = QtWidgets.QListView(Dialog)
        self.listView_cour_etudiant.setGeometry(QtCore.QRect(20, 400, 461, 192))
        self.listView_cour_etudiant.setObjectName("listView_cour_etudiant")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_numero.setText(_translate("Dialog", "Numéro d\'étudiant"))
        self.label_erreur_numero.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\"> Numéro d\'étudiant invalide. Entrez une valeur numérique.</span></p></body></html>"))
        self.label_erreur_Etu_Existe.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant existe déjà. Entrez un nouvel étudiant.</span></p></body></html>"))
        self.label_erreur_Etu_Inexistant.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant n\'existe pas.</span></p></body></html>"))
        self.label_cour.setText(_translate("Dialog", "Cour"))
        self.pushButton_ajouter.setText(_translate("Dialog", "Ajouter"))
        self.pushButton_quitter.setText(_translate("Dialog", "Quitter"))
