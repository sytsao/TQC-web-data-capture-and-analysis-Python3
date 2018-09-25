# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print("coutry_data.xml的根節點："+root.tag)
print("根節點標籤裡的屬性和屬性值："+str(root.attrib))
for child in root:
    print(child.tag, child.attrib)
print("排名:"+root[0][0].text,"國內生產總值:"+root[0][2].text,)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)








