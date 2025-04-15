import json

json_file = 'sample-data.json'

json_data = {}

with open(json_file, 'r') as file:
    json_data = json.load(file)

i = 0
print("Interface Status")
print("="*85)
print("DN                                               Description           Speed       MTU")
print("---------------------------------------------   ------------------    -------   --------")
for data in json_data['imdata']:
    print(f"{data['l1PhysIf']['attributes']['dn']}                            {(data['l1PhysIf']['attributes']['speed'])}     {data['l1PhysIf']['attributes']['mtu']}")
    if i == 2:
        break
    else:
        i += 1