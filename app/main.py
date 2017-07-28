import node
import ring
import config
import distance
import hashkey
import finger_table
import random
import ring
import json
import sys
rings=[]
nodes=[]
sys.setrecursionlimit(1500)
def create_ring(ring_id):
	new_ring= ring.Ring(ring_id)
	new_ring.create(nodes)
	rings.append(new_ring)
	str ='tao ring thanh cong!!!'
	print str
	return str

def join(NodeID,NodeID_old):
	node_joined= None
	for nod in nodes:
		if NodeID_old==nod.NodeID:
			node_joined= nod
			break
	if node_joined is None:
		print 'khong ton tai node joined: ', NodeID_old
		a= 'khong ton tai node joined: ' + str(NodeID_old)
		return a
	new_node = node.Node(NodeID)
	new_node.join(node_joined)
	nodes.append(new_node)
	# rings[0].nodes.append(new_node)
	return infor_nodes(new_node.NodeID)

def remove(NodeID):
	node=None
	for i in nodes:
		if NodeID== i.NodeID:
			node=i
			break
	if node is None:
		print 'khong ton tai node co NodeID la: ', NodeID
		result= 'khong ton tai node co NodeID la: ' + str(NodeID)
		return result
	if node.remove():
		nodes.remove(node)
		rings[0].nodes.remove(node)
		return 'remove thanh cong'


def lookup(NodeID,keyID=None,data=None):
	duongdi=[]
	node_joined=None
	for node in nodes:
		if NodeID==node.NodeID:
			node_joined= node
			break
	if node_joined is None:
		kq= 'khong co Node nao co ID: ' +  str(NodeID)
		return kq
	if keyID is None:
		keyID=hashkey.hashkey(data)
	return node_joined.lookup(keyID,duongdi)


def insert(NodeID,data):
	duongdi=[]
	node_old=None
	for nod in nodes:
		if nod.NodeID==NodeID:
			node_old=nod
			break
	if node_old is None:
		print 'khong ton tai node da tham gia co NodeID la: ', NodeID
		a= 'khong ton tai node da tham gia co NodeID la: ' + str(NodeID)
		return a
	return node_old.insert(data,duongdi)

def infor_nodes(node_id):
	if node_id==-1:
		list1=[] 
		i=0
		nod=nodes[0]
		while 1:
			a= {i:{'NodeID': nod.NodeID,'keyID': nod.keyID,'NodeID sucessor': nod.successor.NodeID,'NodeID predecessor': nod.predecessor.NodeID,'key-value': nod.managekey_value}}
			list1.append(a)
			i+=1
			nod= nod.successor
			if nod==nodes[0]:
				return json.dumps(list1,indent=4)
	for nod in nodes:
		if nod.NodeID==node_id:
			return nod.get_infor()
	print 'khong tim thay node co gia tri NodeID la: ', node_id
	return 'False'
	

def save():
	arr=[]
	for nod in nodes:
		if nod.managekey_value:
			for key_value in nod.managekey_value:
				data= {'NodeID': nod.NodeID, 'data': key_value['value']}
				arr.append(data)

	data={
		'id_ring': rings[0].Id_Ring,
		'Nodes': [x.NodeID for x in nodes],
		'data': arr
		}
	with open('data.txt','w') as filedata:
		print data
		json.dump(data,filedata)
		return True

def load():
	if rings ==[]:
		with open('data.txt','r') as filedata:
			data=json.load(filedata)
			print json.dumps(data)
			# data=json.dumps(data)
			id_ring=data['id_ring']
			Nodes= data['Nodes']
			key_value=data['data']
			# tao ring
			new_ring= ring.Ring(id_ring)
			new_ring.create(nodes,Nodes)
			rings.append(new_ring)
			# khoi tao key_value
			for i in key_value:
				print i['data']
				print insert(i['NodeID'],i['data'])
			return True
	else: 
		print('da ton tai ring')
		return False


# moi mot node insert 5 data
def insert_data():
	for nod in nodes:
		for i in range(10):
			data=random.randint(1,2**20)
			insert(nod.NodeID,data)
	return 'hoan thanh insert'
