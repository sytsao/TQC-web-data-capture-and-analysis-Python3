import json
print(json.dumps([0,1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=3))



