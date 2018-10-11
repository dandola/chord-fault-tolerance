import numpy as np
import json
import random
import math
import config



def random_nodes():
	nodes = random.sample(range(2**20), config.NODES)
	arr_nodes=[]
	nodes_fail= nodes
	for i in range(90,0,-10):
		print i
		k= int(math.ceil(config.NODES*i*1.0/100))
		nodes_fail= random.sample(nodes_fail,k)
		arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false': nodes_fail, 'data': []})
	arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false':[], 'data': []})
	arr_nodes.reverse()
	a="test_" + str(config.NODES) + "_nodes.txt"
	with open(a,'w') as filedata:
		json.dump(arr_nodes,filedata)
	return True

def set_of_key():
	keys=[]
	part= int(math.ceil((2**160)*1.0/4000))
	keys = range(0,2**160,part)
	print len(keys)
	b="set_4000_keys.txt"
	with open(b,'w') as filedata:
		json.dump({'keys': keys},filedata)
		return True

def data_insert():
	times =range(5)
	arr_nodes=[]
	for i in times:
		nodes= random.sample(range(2**25),config.NODES)
		arr_nodes.append({'id_ring': 1, 'Nodes': nodes, 'Node_false':[], 'data':[]})
	a="data_insert/insert_data_1024nodes.txt"
	with open(a,'w') as filedata:
		json.dump(arr_nodes,filedata)
	return True


def create_ring():
	nodes=[]
	arr_nodes=[]
	key=14615016373309029182036848327162830196559325
	print key
	partition=int(2**160/1024)
	times=range(1024)
	for i in times:
		nodes.append((key+partition*i)%(2**160))
	times=range(0,10,1)
	count_fail = int(math.floor(1024*0.1))
	print "count_fail: ",count_fail
	for i in times:
		if i==0:
			arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false':[], 'data': [],'count_fail':0})
		else:
			arr_node_fail=[]
			fails= count_fail*i
			partition_i=int(2**160/fails)
			k= range(0,fails,1)
			for j in k:
				part = (nodes[0] + j*partition_i)%(2**160)
				for t in range(len(nodes)):
					if nodes[t] >= part:
						arr_node_fail.append(nodes[t])
						break
			arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false': arr_node_fail, 'data': [],'count_fail': len(arr_node_fail)})
	b="set_1024_nodes.txt"
	with open(b,'w') as filedata:
		json.dump(arr_nodes,filedata)
	return True


def read_file():
	a="topo_1024_nodes_2000_keys_lookup_with_chord_fault_tolerance.json"
	datas=[]
	with open(a,'r') as filedata:
		datas= json.load(filedata)
	for data in datas:
		print"max:",data['max'],", min:",data['min'],", mean:",data['mean'],", fails:", data['fails'],", requests:", data['requests'],", successes:",data['successes'],", overall_cost:",data['overall_cost'], ", max_overall_cost:", data['max_overall_cost']
	
set_of_key()


