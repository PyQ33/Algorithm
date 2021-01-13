# decoding : json -> python structure
# by json.loads

import json

user ={
    'id':'gildong',
    'pw':'19237',
    'hobby': ['football','programming']
}
print(user)
# save to jsonfile
with open('user.json','w',encoding='utf-8') as file:
    json.dump(user, file, indent= 4)

json_data = json.dumps(user)
print(json_data)

data = json.loads(json_data)
print(data)
# -------------------------------------------------
# ecoding :  python structure -> json
# by json.dumps()

import json
user ={
    'id':'gildong',
    'pw':'19237',
    'hobby': ['football','programming']
}

json_data = json.dumps(user, indent=4)
print(json_data)