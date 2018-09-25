# -*- coding: utf-8 -*-
import yaml
import json
with open("GE1-8n-input.json",encoding = 'utf-8-sig') as file:
    data = json.load(file)

with open("GE1-8n-output.yaml", "w",encoding="utf-8") as f:
    yaml.dump(data, f,default_flow_style=False, allow_unicode=True)