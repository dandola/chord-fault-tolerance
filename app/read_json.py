import json


list_mean=[]
list_max=[]
list_min=[]

with open('topo_64_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])


with open('topo_128_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])


with open('topo_256_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])

with open('topo_512_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])

with open('topo_1024_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])

with open('topo_2048_nodes_2048_keys_lookup.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])

list_mean1=[]
list_max1=[]
list_min1=[]

with open('topo_64_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])

with open('topo_128_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])

with open('topo_256_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])

with open('topo_512_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])

with open('topo_1024_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])

with open('topo_2048_nodes_2048_keys_lookup_40%_fault.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])