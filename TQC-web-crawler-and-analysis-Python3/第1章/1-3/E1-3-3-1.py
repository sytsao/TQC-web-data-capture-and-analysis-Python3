# -*- coding: utf-8 -*-
import yaml
with open("PYD01-2-input.yaml",encoding="utf-8") as f:
     list_doc = yaml.load(f)

for sense in list_doc:
    if sense["name"] == "sense3":
         sense["value"] = 1234

with open("PYD01-2-output.yaml", "w",encoding="utf-8") as f:
    yaml.dump(list_doc, f)