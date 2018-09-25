import json
print(json.dumps(['two', {'bar': ('jaz', None, 2.0, 1)}]))
print(json.dumps("\"two\bar"))
print(json.dumps('\u4321'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "d": 0}, sort_keys=True))


