import ring
import config
import distance
import hashkey
import finger_table
import random
import ring
import json
import math
import main

def fault():
	k= int(math.ceil(config.NODES*0.4))
	node_fail= random.sample(main.nodes,k)
	for nod in node_fail:
		nod.status=False


def test1():
	k= config.NODES
	values=random.sample(range(1,2**20),2048)
	keys=[]
	for value in values:
		keyID=hashkey.hashkey(value)
		keys.append(keyID)
	list1=[]
	for node in main.nodes:
		if node.status==True:
			for key in keys:
				# print 'NodeID: ',node.NodeID, 'key: ',key
				t=node.lookup(key,duongdi=[])
				if t ==False:
					return "he thong bi loi hoat dong"
				list1.append(t)

	mean=sum(list1)*1.0/len(list1)
	dic = {'costs': list1, 'max': max(list1), 'min': min(list1),'mean': mean}
	a="topo_" + str(k) + "_nodes_" + str(2048) + "_keys_lookup_40%_fault.json"
	# print a
	with open(a,"w") as fw:
		json.dump(dic,fw)
	return json.dumps({'trung binh': mean,'max cost': max(list1),'min cost': min(list1)},indent=3)


		
