# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for country in root.findall('country'):
    rank=int(country.find("rank").text)
    if rank>50:
        root.remove(country)
tree.write("E1-4-3-2-output.xml",encoding="utf-8")











