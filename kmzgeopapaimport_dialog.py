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

import os
import urllib.parse
import webbrowser
from pathlib import Path
from zipfile import BadZipFile
from qgis.core import Qgis
from qgis.PyQt import QtCore
from qgis.PyQt.QtWidgets import QFileDialog, QDialog, QMessageBox, QApplication
from qgis.gui import QgsMessageBar
from qgis.utils import iface
from .kmzgeopapaimport_dialog_base import Ui_kmz_geopapaimportDialogBase


class kmz_geopapaimportDialog(QDialog, Ui_kmz_geopapaimportDialogBase):
    """Dialog for Kmzgeopapaimport plugin.
    It loads the kmzgeopapaimport_dialog_base.ui file to define the dialog
    layout and widgets.
    """

    def __init__(self, plugin_instance, iface, parent=None):
        """Constructor."""
        super(kmz_geopapaimportDialog, self).__init__(parent)
        self.iface = iface
        self.plugin_instance = plugin_instance
        # Set up the user interface from Designer
        self.setupUi(self)
        self.gtprjbox.setChecked(False)
        self.messagebar = QgsMessageBar(self)
        self.kmzarcentrada.setAcceptDrops(True)
        self.Cancel.clicked.connect(self.close)
        self.kmzarcentrada.textChanged.connect(self._update_kml_names)
        self.kmzarcentrada.textChanged.connect(self._update_placemark_names)

    def dragEnterEvent(self, event):
        """Event that is sent to a widget when a drag and drop action enters it."""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        """drop event"""
        if not event.mimeData().hasUrls:
            return
        # Get the first valid file URL
        file_urls = next(
            (url for url in event.mimeData().urls() if url.isLocalFile()), None
        )
        if not file_urls:
            event.ignore()
            return
        file_path = file_urls.url()
        # Remove the 'file:///' prefix if it exists
        if file_path.startswith("file:///"):
            file_path = file_path[len("file:///") :]
        # Decode URL-encoded characters (e.g., %20 for spaces)
        file_path = urllib.parse.unquote(file_path)
        # Normalize the path to handle any inconsistencies (e.g., double slashes, /./, /../)
        file_path = os.path.normpath(file_path)
        target_widget = self._get_drop_target_widget(event.pos())

        if not target_widget:
            event.ignore()
            return
        # Handle different drop targets
        try:
            if target_widget == self.kmzarcentrada:
                self._handle_kmz_drop(file_path)
            elif target_widget == self.csvarch:
                self._hancle_folder_drop(file_path)
            else:
                event.ignore()
        except ValueError as e:
            self.messagebar.pushMessage(
                "Error", str(e), level=Qgis.Critical, duration=5
            )
            event.ignore()

    def _update_kml_names(self):
        """Update the list of documento names based on the KMZ file."""
        kmz_file_path = self.kmzarcentrada.text()
        self.docsnames.clear()
        if kmz_file_path and Path(kmz_file_path).is_file():
            try:
                # Call the method in the main plugin class to get document names
                doc_names = self.plugin_instance.get_document_names(Path(kmz_file_path))
                if doc_names:
                    self.docsnames.addItems([doc_names])
                else:
                    self.messagebar.pushMessage(
                        "Info",
                        self.tr("No documents found in KMZ file."),
                        level=Qgis.Info,
                        duration=3,
                    )
            except Exception as e:
                self.messagebar.pushMessage(
                    "Error",
                    self.tr(f"Error loading documents: {e}"),
                    level=Qgis.Critical,
                    duration=5,
                )

    def _handle_kmz_drop(self, file_path):
        """Validate and process KMZ file drop"""
        if not file_path.lower().endswith(".kmz"):
            raise ValueError("Invalid file type. Please drop a .kmz file.")
        if not Path(file_path).is_file():
            raise ValueError("The dropped KMZ file does not exist.")
        self.kmzarcentrada.setText(file_path)
        self.kmzarcentrada.setToolTip(file_path)  # Show full path on hover

    def _handle_folder_drop(self, path):
        """Validate and process folder drop"""
        if not path(path).is_dir():
            raise ValueError("The dropped item is not a valid directory.")
        if not os.access(path, os.W_OK):
            raise ValueError("The dropped directory is not writable.")
        self.csvarch.setText(path)
        self.csvarch.setToolTip(path)  # Show full path on hover

    def _get_drop_target_widget(self, pos):
        """Determine which widget the drop occurred on"""
        widget = {
            self.kmzarcentrada: [".kmz"],
            self.csvarch: [],
        }  # Empty list means any file type (for folders)
        for widget, extensions in widget.items():
            if widget.geometry().contains(pos):
                return widget
        return None

    def _update_placemark_names(self):
        kmz_file_path = self.kmzarcentrada.text()
        self.formatosjson.clear()
        if kmz_file_path and Path(kmz_file_path).is_file():
            try:
                # Call the method in the main plugin class to get placemark names
                placemark_names = self.plugin_instance.get_placemark_names(
                    Path(kmz_file_path)
                )
                if placemark_names:
                    self.formatosjson.addItems(placemark_names)
                else:
                    self.messagebar.pushMessage(
                        "Info",
                        self.tr("No placemarks found in KMZ file."),
                        level=Qgis.Info,
                        duration=3,
                    )
            except Exception as e:
                self.messagebar.pushMessage(
                    "Error",
                    self.tr(f"Error loading placemarks: {e}"),
                    level=Qgis.Critical,
                    duration=5,
                )

    @QtCore.pyqtSlot(name="on_examinarkmz_clicked")
    def on_examinarkmz_clicked(self):
        """select kmz file"""
        kmz_file, _ = QFileDialog.getOpenFileName(
            self, self.tr("Select kmz file"), "", self.tr("KMZ Files (*.kmz *.KMZ)")
        )
        if not kmz_file:
            return
        self.kmzarcentrada.setText(kmz_file)

    @QtCore.pyqtSlot(name="on_destino_clicked")
    def on_destino_clicked(self):
        """select output directory"""
        self.csvarch.clear()
        folder = QFileDialog.getExistingDirectory(
            self,
            self.tr("Select Output Directory"),
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        if not folder:
            return
        self.csvarch.setText(folder)

    @QtCore.pyqtSlot(name="on_crsproject_clicked")
    def on_crsproject_clicked(self):
        """Set CRS from project."""
        prj = iface.mapCanvas().mapSettings().destinationCrs()
        self.crsproj4string.setText(prj.toProj())

    @QtCore.pyqtSlot(name="on_crsactlayer_clicked")
    def on_crsactlayer_clicked(self):
        """Set CRS from active layer."""
        layer = iface.activeLayer()
        self.crsproj4string.clear()
        if layer:  # If there is an active layer
            prj = layer.crs()
            if prj.isValid():
                self.crsproj4string.append(str(prj.toProj()))
            else:
                QMessageBox.information(
                    self,
                    self.tr("Invalid CRS"),
                    self.tr("The active layer does not have a valid CRS."),
                )
        else:
            QMessageBox.information(
                self,
                self.tr("No Active Layer"),
                self.tr("There is no active layer to get the CRS from."),
            )

    @QtCore.pyqtSlot(name="on_resetdata_clicked")
    def on_resetdata_clicked(self):
        """Reset all data fields."""
        self.kmzarcentrada.clear()
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
            kmz_file = Path(self.kmzarcentrada.text())  # Ensure it's a Path object
            output_dir = Path(self.csvarch.text())  # Ensure it's a Path object
            ncsv = self.formatosjson.currentText()  # Get the selected form name
            gtprjbox_checked = (
                self.gtprjbox.isChecked()
            )  # Boolean for coordinate transformation
            crs_proj4 = str(self.crsproj4string.toPlainText())  # Get CRS string

            if not all([kmz_file, output_dir, ncsv]):
                raise ValueError(self.tr("All input fields are required."))

            # 2. Prepare for processing
            self.datos.setText(self.tr(f"Processing {ncsv}..."))
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

            output_path = self.plugin_instance.process_kmz_data(
                kmz_file,
                output_dir,
                ncsv,
                gtprjbox_checked,
                crs_proj4,
            )

            self.datos.append(self.tr(f"\nSuccess! File saved to:\n{output_path}"))

        except (ValueError, BadZipFile, FileNotFoundError, IndexError) as e:
            self.datos.append(self.tr(f"\nERROR: {e}"))
            self.messageBar.pushMessage(
                self.tr("Error"), str(e), level=Qgis.Critical, duration=5
            )
        finally:
            QApplication.restoreOverrideCursor()

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
