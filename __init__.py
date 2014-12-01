# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Kmzgeopapaimport
                                 A QGIS plugin
 Importar tags a csv
                             -------------------
        begin                : 2014-11-11
        copyright            : (C) 2014 by Juan M. Bernales
        email                : juanbernales@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Kmzgeopapaimport class from file Kmzgeopapaimport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .kmzgeopapaimport import Kmzgeopapaimport
    return Kmzgeopapaimport(iface)
