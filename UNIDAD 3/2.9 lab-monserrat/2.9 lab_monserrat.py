'''
Nombre:Monserrat Orduña Basaldua
Fecha: 04/12/2023
Descripcion: laboratorio 2.9
'''

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
         host="10.10.20.48",
         port=830,
         username="developer",
         password="C1sco12345",
         hostkey_verify=False
)