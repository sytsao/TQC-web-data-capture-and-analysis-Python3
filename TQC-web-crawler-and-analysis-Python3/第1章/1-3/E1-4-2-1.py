# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
         print('tag:', child.tag, 'attributes:', child.attrib)
         for grandchild in child:
             print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)
print(len(root))     # 菜單選項的數目
print(len(root[0]))  # 早餐選項的數目

