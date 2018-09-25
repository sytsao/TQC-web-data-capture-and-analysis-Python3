# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
for rank in root.iter("rank"):
    new_rank=int(rank.text)+1
    rank.text=str(new_rank)
    rank.set("updated","yes")
tree.write("E1-4-3-1-output.xml",encoding="utf-8")










