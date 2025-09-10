
Guía de Usuario: KMZ Geopapa Import (v0.2)
===========================================

Este plugin para QGIS permite importar datos de archivos ``.kmz`` generados por la aplicación **Geopaparazzi**, convirtiéndolos en archivos CSV para su uso en QGIS u otro software.

Pasos para la importación
-------------------------

#. **Abrir el Plugin:**

   En QGIS, ve al menú "Complementos" (Plugins) y selecciona "Import kmz files" para abrir el diálogo de importación.

#. **Seleccionar Archivo KMZ:**

   Haz clic en el botón "..." junto al campo "KMZ File" y selecciona el archivo ``.kmz`` que exportaste desde Geopaparazzi.

#. **Elegir el Formulario:**

   El plugin analizará el archivo KMZ y listará todos los formularios (capas) que encuentre en el menú desplegable "Choose the form to process". Selecciona el formulario que deseas importar.

#. **Seleccionar Carpeta de Salida:**

   Haz clic en el botón "..." junto a "Output folder" para elegir la carpeta donde se guardará el archivo CSV resultante.

#. **(Opcional) Reproyectar Coordenadas:**

   Si deseas convertir las coordenadas originales (WGS84) a otro sistema de referencia:

   * Activa la casilla "Reproject to project CRS".
   * Elige el CRS de destino en el menú desplegable.
   * El archivo CSV de salida incluirá dos nuevas columnas, ``xtrsf`` y ``ytrsf``, con las coordenadas reproyectadas.

#. **Procesar:**

   Haz clic en el botón "Process". El plugin creará un archivo ``.csv`` en la carpeta de salida. El nombre del archivo se basará en el nombre del formulario que seleccionaste (ej. ``mi_formulario.csv``).

Resultado
---------

Al finalizar, encontrarás un archivo CSV en la carpeta de salida listo para ser cargado en QGIS como una capa de texto delimitado o para ser analizado en otro software.
