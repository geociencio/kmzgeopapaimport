# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmzgeopapaimport_dialog_base.ui'
#
# Created: Tue Nov 11 18:02:56 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_kmlppcsvDialogBase(object):
    def setupUi(self, kmlppcsvDialogBase):
        kmlppcsvDialogBase.setObjectName(_fromUtf8("kmlppcsvDialogBase"))
        kmlppcsvDialogBase.resize(520, 198)
        self.button_box = QtGui.QDialogButtonBox(kmlppcsvDialogBase)
        self.button_box.setGeometry(QtCore.QRect(265, 166, 251, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.jsonarcbase = QtGui.QLineEdit(kmlppcsvDialogBase)
        self.jsonarcbase.setGeometry(QtCore.QRect(110, 20, 320, 20))
        self.jsonarcbase.setObjectName(_fromUtf8("jsonarcbase"))
        self.label_1 = QtGui.QLabel(kmlppcsvDialogBase)
        self.label_1.setGeometry(QtCore.QRect(20, 0, 481, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(kmlppcsvDialogBase)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.examinarjson = QtGui.QPushButton(kmlppcsvDialogBase)
        self.examinarjson.setGeometry(QtCore.QRect(440, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.examinarjson.setFont(font)
        self.examinarjson.setObjectName(_fromUtf8("examinarjson"))
        self.formatosjson = QtGui.QComboBox(kmlppcsvDialogBase)
        self.formatosjson.setGeometry(QtCore.QRect(270, 50, 160, 22))
        self.formatosjson.setObjectName(_fromUtf8("formatosjson"))
        self.label_3 = QtGui.QLabel(kmlppcsvDialogBase)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.kmzarcentrada = QtGui.QLineEdit(kmlppcsvDialogBase)
        self.kmzarcentrada.setGeometry(QtCore.QRect(110, 80, 320, 20))
        self.kmzarcentrada.setObjectName(_fromUtf8("kmzarcentrada"))
        self.examinarkmz = QtGui.QPushButton(kmlppcsvDialogBase)
        self.examinarkmz.setGeometry(QtCore.QRect(440, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.examinarkmz.setFont(font)
        self.examinarkmz.setObjectName(_fromUtf8("examinarkmz"))
        self.label_4 = QtGui.QLabel(kmlppcsvDialogBase)
        self.label_4.setGeometry(QtCore.QRect(200, 55, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.destino = QtGui.QPushButton(kmlppcsvDialogBase)
        self.destino.setGeometry(QtCore.QRect(440, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.destino.setFont(font)
        self.destino.setObjectName(_fromUtf8("destino"))
        self.csvarch = QtGui.QLineEdit(kmlppcsvDialogBase)
        self.csvarch.setGeometry(QtCore.QRect(270, 110, 160, 20))
        self.csvarch.setObjectName(_fromUtf8("csvarch"))
        self.label_5 = QtGui.QLabel(kmlppcsvDialogBase)
        self.label_5.setGeometry(QtCore.QRect(140, 110, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.procesardat = QtGui.QPushButton(kmlppcsvDialogBase)
        self.procesardat.setGeometry(QtCore.QRect(359, 138, 75, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.procesardat.setFont(font)
        self.procesardat.setObjectName(_fromUtf8("procesardat"))
        self.datos = QtGui.QTextEdit(kmlppcsvDialogBase)
        self.datos.setGeometry(QtCore.QRect(10, 130, 241, 64))
        self.datos.setObjectName(_fromUtf8("datos"))

        self.retranslateUi(kmlppcsvDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), kmlppcsvDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), kmlppcsvDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(kmlppcsvDialogBase)

    def retranslateUi(self, kmlppcsvDialogBase):
        kmlppcsvDialogBase.setWindowTitle(QtGui.QApplication.translate("kmlppcsvDialogBase", "kmlppcsv", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Convertir KMZ a CSV exportados de Geopaparazzi en base a formato JSON", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Archivo JSON", None, QtGui.QApplication.UnicodeUTF8))
        self.examinarjson.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Examinar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Archivo KMZ", None, QtGui.QApplication.UnicodeUTF8))
        self.examinarkmz.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Examinar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Formato", None, QtGui.QApplication.UnicodeUTF8))
        self.destino.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Examinar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Carpeta de destino", None, QtGui.QApplication.UnicodeUTF8))
        self.procesardat.setText(QtGui.QApplication.translate("kmlppcsvDialogBase", "Procesar", None, QtGui.QApplication.UnicodeUTF8))

