#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''



from xml.etree import ElementTree as ET
tree = ET.parse('xo.xml')
root = tree.getroot()
print(root)
for child in root:
    print(child)
    print(child.tag,child.attrib)
    for gradechild in child:
        #print(gradechild)
        print(gradechild.tag,gradechild.text,gradechild.attrib)
'''
'''

from xml.etree import ElementTree as ET
str_xml = open('xo.xml','r').read()
root = ET.XML(str_xml)
print(root)
'''
'''

from xml.etree import ElementTree as ET
str_xml = open('xo.xml','r').read()
root = ET.XML(str_xml)
print(root.tag)
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('name','alex')
    node.set('age','18')

'''
from xml.etree import ElementTree as ET
root = ET.Element("famliy")
son1 = ET.Element('son',{'name':'er1'})
son2 = ET.Element('son',{'name':'er2'})
grandson1 = ET.Element('grandson',{'name':'er11'})
grandson2 = ET.Element('grandson',{'name':'er22'})

son1.append(grandson1)
son2.append(grandson2)
root.append(son1)
root.append(son2)
tree = ET.ElementTree(root)
tree.write('ooo.xml',encoding='utf-8',short_empty_elements=False)