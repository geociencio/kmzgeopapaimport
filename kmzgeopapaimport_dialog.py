# -*- coding: utf-8 -*-
"""
/***************************************************************************
 KmzgeopapaimportDialog
                                 A QGIS plugin
 Importar tags a csv
                             -------------------
        begin                : 2025-07-07
        git sha              : $Format:%H$
        copyright            : (C) 2025 by Juan M. Bernales
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

import json
import webbrowser
from pathlib import Path
from zipfile import BadZipFile

from qgis.PyQt import QtCore, QtWidgets
from qgis.core import Qgis, QgsProject
from qgis.gui import QgsMessageBar

from . import kmz_geopapaimport
from .kmz_geopapaimport_dialog_base import Ui_kmz_geopapaimportDialogBase


class kmz_geopapaimportDialog(QtWidgets.QDialog, Ui_kmz_geopapaimportDialogBase):
    def __init__(self, parent=None, plugin=None):
        """Constructor."""
        super(kmz_geopapaimportDialog, self).__init__(parent)
        self.setupUi(self)
        self.messageBar = QgsMessageBar(self)
        self.plugin = plugin
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """Event that is sent to a widget when a drag and drop action enters it."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Event that is sent when a drag and drop action is completed."""
        urls = event.mimeData().urls()
        if not urls:
            return

        file_path = Path(urls[0].toLocalFile())

        if file_path.suffix.lower() == ".kmz":
            self.kmzarcentrada.setText(str(file_path))
            event.acceptProposedAction()
        elif file_path.suffix.lower() == ".json":
            self.jsonarcbase.setText(str(file_path))
            self.on_examinarjson_clicked(file_path=str(file_path))
            event.acceptProposedAction()
        else:
            event.ignore()

    @QtCore.pyqtSlot(name="on_examinarkmz_clicked")
    def on_examinarkmz_clicked(self):
        """Select kmz file."""
        kmz_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            self.tr("Select KMZ file"),
            "",
            self.tr("KMZ files (*.kmz *.KMZ)"),
        )
        if kmz_file:
            self.kmzarcentrada.setText(kmz_file)

    @QtCore.pyqtSlot(name="on_examinarjson_clicked")
    def on_examinarjson_clicked(self, file_path=None):
        """Select JSON file and populate formats."""
        if not file_path:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self,
                self.tr("Select JSON file"),
                "",
                self.tr("JSON files (*.json *.JSON)"),
            )
        if not file_path:
            return

        self.jsonarcbase.setText(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.formatosjson.clear()
            for item in data:
                self.formatosjson.addItem(item.get("sectionname", "Unnamed Section"))
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self.messageBar.pushMessage(
                self.tr("Error"),
                self.tr("Could not read or parse JSON file: {error}").format(error=e),
                level=Qgis.Critical,
            )

    @QtCore.pyqtSlot(name="on_destino_clicked")
    def on_destino_clicked(self):
        """Select destination folder."""
        folder = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            self.tr("Select destination folder"),
            "",
            QtWidgets.QFileDialog.ShowDirsOnly
            | QtWidgets.QFileDialog.DontResolveSymlinks,
        )
        if folder:
            self.csvarch.setText(folder)

    @QtCore.pyqtSlot(name="on_crsproject_clicked")
    def on_crsproject_clicked(self):
        """Set CRS from project."""
        prj = QgsProject.instance().crs()
        self.crsproj4string.setText(prj.toProj4())

    @QtCore.pyqtSlot(name="on_crsactlayer_clicked")
    def on_crsactlayer_clicked(self):
        """Set CRS from active layer."""
        layer = self.plugin.iface.activeLayer()
        if layer:
            crs = layer.crs()
            if crs.isValid():
                self.crsproj4string.setText(crs.toProj4())
            else:
                self.messageBar.pushMessage(
                    self.tr("Invalid CRS"),
                    self.tr("The active layer has an invalid CRS."),
                    level=Qgis.Warning,
                )
        else:
            self.messageBar.pushMessage(
                self.tr("No active layer"),
                self.tr("There is no active layer in QGIS."),
                level=Qgis.Info,
            )

    @QtCore.pyqtSlot(name="on_resetdata_clicked")
    def on_resetdata_clicked(self):
        """Reset all data fields."""
        self.kmzarcentrada.clear()
        self.jsonarcbase.clear()
        self.csvarch.clear()
        self.formatosjson.clear()
        self.crsproj4string.clear()
        self.datos.clear()
        self.gtprjbox.setChecked(False)

    @QtCore.pyqtSlot(name="on_procesardat_clicked")
    def on_procesardat_clicked(self):
        """Process data from KMZ file based on JSON definition."""
        try:
            # 1. Get user inputs
            kmz_file = self.kmzarcentrada.text()
            json_file = self.jsonarcbase.text()
            dest_folder = Path(self.csvarch.text())
            form_name = self.formatosjson.currentText()
            form_index = self.formatosjson.currentIndex()
            transform_coords = self.gtprjbox.isChecked()
            crs_proj4_string = self.crsproj4string.toPlainText()

            if not all([kmz_file, json_file, dest_folder, form_name]):
                raise ValueError(self.tr("All input fields are required."))

            # 2. Prepare for processing
            self.datos.setText(self.tr(f"Processing {form_name}..."))
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            output_path = kmz_geopapaimport.process_kmz_file(
                kmz_file,
                json_file,
                dest_folder,
                form_index,
                form_name,
                transform_coords,
                crs_proj4_string,
            )

            self.datos.append(self.tr(f"\nSuccess! File saved to:\n{output_path}"))

        except (ValueError, BadZipFile, FileNotFoundError, IndexError) as e:
            self.datos.append(self.tr(f"\nERROR: {e}"))
            self.messageBar.pushMessage(
                self.tr("Error"), str(e), level=Qgis.Critical, duration=5
            )
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    @QtCore.pyqtSlot(name="on_help_clicked")
    def on_help_clicked(self):
        """Open help file."""
        current_path = Path(__file__).resolve().parent
        help_file = current_path / "help" / "build" / "html" / "index.html"
        if help_file.exists():
            webbrowser.open(help_file.as_uri())
        else:
            self.messageBar.pushMessage(
                self.tr("Help file not found"),
                level=Qgis.Warning,
            )

    @QtCore.pyqtSlot(name="on_exit_clicked")
    def on_exit_clicked(self):
        """Exit."""
        self.close()
