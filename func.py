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
#!/usr/bin/env python
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import re
import json

def nomjsonform(arcjson):
    """get format"""
    json_data = open(arcjson)
    data = json.load(json_data)
    json_data.close()
    dtformname = []
    for dat in data:
        dtformname.append(dat['sectionname'])
    return dtformname

def datjson(arcjson, ind1):
    """get data"""
    json_data = open(str(arcjson))
    data = json.load(json_data)
    dtformitem = []
    for dat in data[ind1]['forms']:
        dtformitem.append(dat['formitems'][0]['key'])
    json_data.close()
    return dtformitem

def datkmz(arkmz, jsonar, descsv, ind, ncsv):
    """process data and save to file"""
    kmz = ZipFile(arkmz, 'r')
    arcsv = open(descsv + '\\' + ncsv + '.csv', 'w')
    archkml = kmz.open('kml.kml', 'r')
    root = ET.parse(archkml).getroot()
    texto = []
    dformitem = datjson(jsonar, ind)
    arcsv.write('formato;')
    for dfitem in dformitem:
        arcsv.write(str(dfitem) + ';')
    arcsv.write('lon;lat;alt' + '\n')
    for elm in root[0]:
        if elm.tag == '{http://www.opengis.net/kml/2.2}Placemark' and str(elm[1].text) == str(ncsv):
            TEXTO = (str(elm[2].text + ';' + re.sub(r',', ';', str(elm[4][0].text))))
            TEXTO = re.split(r'\n{2,}', TEXTO)
            TEXTO = re.sub(r'\n', '', TEXTO[1])
            TEXTO = re.sub(r'<table style="text-align: left; width: 100%;" border="1" cellpadding="5" cellspacing="2"><tbody><tr><td style="text-align: left; vertical-align: top; width: 50%;">.*?</td><td style="text-align: left; vertical-align: top; width: 50%;">', '', str(TEXTO))
            TEXTO = re.sub(r'</td></tr></tbody></table>', '', TEXTO)
            TEXTO = re.sub(r'<h2>.*?</h2>', ';', str(TEXTO))
            TEXTO = re.sub(r'<.*?>', '', str(TEXTO))
            arcsv.write(str(TEXTO) + '\n')
    del(TEXTO)
    arcsv.close()
