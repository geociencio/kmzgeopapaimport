# -*- coding: utf-8 -*-
"""
/***************************************************************************
 KmzgeopapaimportDialog
                                 A QGIS plugin
 Importar tags a csv
                             -------------------
        begin                : 2014-11-11
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Juan M. Bernales
        email                : juanbernales@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from os import path
import webbrowser
import func as fnc
from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__),
                               'kmzgeopapaimport_dialog_base.ui'))

class KmzgeopapaimportDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""

        super(KmzgeopapaimportDialog, self).__init__(parent)
        self.setupUi(self)

        QObject.connect(self.examinarjson, SIGNAL("clicked()"),
                        self.abrirjson)
        QObject.connect(self.examinarkmz, SIGNAL("clicked()"),
                        self.abrirkmz)
        QObject.connect(self.destino, SIGNAL("clicked()"), self.destin)
        QObject.connect(self.procesardat, SIGNAL("clicked()"), self.proces)
        QObject.connect(self.button_box, SIGNAL( "helpRequested()" ), self.helpbr)

    def abrirjson(self):
        """select json file"""
        #set ext
        filtrojson = str('''(*.json *.JSON)''')
        #open dialog
        self.arjson = QFileDialog.getOpenFileName(
                        self, str(QCoreApplication.translate( "dialog",
                        "Select json file")),
                        str(), filtrojson)

        if not self.arjson:
			return
        #show path
        self.jsonarcbase.setText(self.arjson)
        self.formatosjson.clear()
        self.DTS = fnc.nomjsonform(self.arjson)
        for dt in self.DTS:
            self.formatosjson.addItem(dt)

    def abrirkmz(self):
        """select kmz file"""
        #set ext
        FILTROKMZ = str('''(*.kmz *.KMZ)''')
        # open dialog
        self.arkmz = QFileDialog.getOpenFileName(self,
                    str(QCoreApplication.translate( "dialog",
                    "Select kmz file")), str(), FILTROKMZ)

        if not self.arkmz:
            return
        #show path
        self.kmzarcentrada.setText(self.arkmz)

    def destin(self):
        """select output directory"""
        CARPDESTINO = QFileDialog.getExistingDirectory(self,
                str(QCoreApplication.translate("dialog","Select Output Directory")),
                str(),QFileDialog.ShowDirsOnly)
        self.csvarch.setText(CARPDESTINO)
        self.carpdest = self.csvarch.text()

    def proces(self):
        '''process data'''
        fnc.datkmz(self.arkmz, self.arjson, self.carpdest,
                self.formatosjson.currentIndex(),
                unicode(self.DTS[self.formatosjson.currentIndex()]))
        self.datos.clear()
        self.datos.append(self.arjson)
        self.datos.append(self.arkmz)
        self.datos.append(str(self.formatosjson.currentIndex()))
        self.datos.append(self.carpdest + '\\' + unicode(
                        self.DTS[self.formatosjson.currentIndex()]) + '.csv')

    def helpbr(self):
        currentPath = path.dirname( __file__ )
        webbrowser.open(currentPath + "/help/help.html")

