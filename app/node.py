import ring
import config
import distance
import hashkey
import finger_table
import random
import ring
import json
manage_key=[]
class Node(object):
	"""Node"""
	def __init__(self,NodeID):
		self.NodeID=NodeID
		self.keyID = hashkey.hashkey(NodeID)
		self.m=config.M
		self.successor= None
		self.predecessor= None
		self.managekey_value=[]
		self.finger=[]

		self.list_successor=[]
		self.status=True


	"""tim kiem successor"""
	def closest_preceding_node(self,keyID):
		for i in range(self.m-1,-1,-1):
			if(distance.distance(self.m,self.keyID,self.finger[i].node.keyID, keyID)):
				if self.finger[i].node.status==True:
					return self.finger[i].node
				else:
					while self.finger[i-1].node.status==False and i>0:
						if self.finger[i-1].node.status==False and self.finger[i-1].node.NodeID==self.successor.NodeID:
							i=0
							break
						i-=1
					if i==0:
						for node_success in self.list_successor:
							if node_success.status==True:
								if(distance.distance(self.m,self.keyID,node_success.keyID, keyID)):
									# print 'chuyen sang node co NodeID: ', node_success.NodeID
									return node_success
						return False
					return self.finger[i-1].node
		return self



	"""tim predecessor cua id"""
	def find_predecessor(self, keyID,duongdi=[]):
		node = self
		success=None
		if node.successor.status==True:
			success= node.successor
		else:
			for nod in node.list_successor:
				if nod.status==True:
					success=nod
					break
		if success is None:
			return False

		while not(distance.distance(self.m,node.keyID,keyID,success.keyID) or keyID == success.keyID):
			node = node.closest_preceding_node(keyID)
			if node ==False:
				return False
			if node.successor.status==True:
				success= node.successor
			else:
				for nod in node.list_successor:
					if nod.status==True:
						success=nod
						break
				if success is None:
					return False
			duongdi.append(node.NodeID)
		return node

	def find_successor(self,keyID,duongdi=[]):
		if self.successor.status==True:
			success=self.successor
		else:
			for suc in self.list_successor:
				if suc.status==True:
					success=suc
					break
		if(distance.distance(self.m,self.keyID,keyID,success.keyID) or keyID==success.keyID):
			if(distance.distance(self.m,success.predecessor.keyID,keyID,success.keyID) or keyID==success.keyID):
				return success
			else:
				return False
		else:
			node= self.closest_preceding_node(keyID)
			duongdi.append(node.NodeID)
			return node.find_successor(keyID,duongdi)


	# khoi tao danh sach successor cua node moi tao
	def init_list_successor(self):
		i=0
		success=self.successor
		while success.NodeID != self.NodeID and i < config.len_nodes:
			# print success.NodeID
			self.list_successor.append(success)
			if self.managekey_value:
				for key_value in self.managekey_value:
					success.managekey_value.append(key_value)
			i+=1
			success=success.successor

		return True

	def copy_data(self):
		pred = self.predecessor
		i=0
		while pred.NodeID != self.NodeID and i < config.len_nodes:
			# print pred.NodeID
			nod=self
			j=i
			while nod.NodeID!=pred.NodeID and j < config.len_nodes:
				if len(pred.list_successor) < j+1:
					pred.list_successor.append(nod)
				else:
					pred.list_successor[j]=nod
				nod=nod.successor
				j+=1
			if pred.managekey_value:
				for key_value in pred.managekey_value:
					self.managekey_value.append(key_value)
			pred= pred.predecessor
			i+=1
		return True


	"""khoi tao bang finger table cua node"""
	def init_finger_table(self,n):
		success=None
		for i in range(self.m):
			node_finger=finger_table.Finger(self.keyID, i)
			self.finger.append(node_finger)
		suc= n.find_predecessor(self.finger[0].start)
		if distance.distance(self.m,suc.keyID,self.finger[0].start,suc.successor.keyID) or suc.successor.keyID==self.finger[0].start:
			success=suc.successor
		else:
			for node_suc in suc.list_successor:
				if distance.distance(self.m,node_suc.predecessor.keyID,self.finger[0].start,node_suc.keyID) or node_suc.keyID==self.finger[0].start:
					success=node_suc
					break
		self.finger[0].node= success
		self.successor= self.finger[0].node  
		self.predecessor= self.successor.predecessor
		self.predecessor.successor=self
		self.successor.predecessor= self
		for i in range(self.m-1):
			if(distance.distance(self.m,self.keyID,self.finger[i+1].start,self.finger[i].node.keyID) or self.finger[i+1].start==self.keyID):
				self.finger[i+1].node = self.finger[i].node
			else:
				suc= n.find_predecessor(self.finger[i+1].start)
				if suc.successor.keyID >= self.finger[i+1].start:
					success=suc.successor
				else:
					for node_suc in suc.list_successor:
						if distance.distance(self.m,node_suc.predecessor.keyID,self.finger[i+1].start, node_suc.keyID) or node_suc.keyID==self.finger[i+1].start:
							success=node_suc
							break
				self.finger[i+1].node=success
		return True


	""" cap nhat node n vao cac finger table khac"""
	def update_others(self):
		for i in range(self.m): 
			if self.keyID >= 2**i:
				p=self.find_predecessor(self.keyID - 2**i)
			else:
				p= self.find_predecessor(self.keyID - 2**i + 2**self.m)
			p.update_finger_table(self,i)


	"""update bang table"""
	def update_finger_table(self,n,i):
		if(distance.distance(self.m, self.keyID, n.keyID, self.finger[i].node.keyID ) or self.keyID==n.keyID):
			self.finger[i].node=n
			p=self.predecessor
			if p == n: 
				return True
			p.update_finger_table(n,i)



	"""gan key-value cho new node"""
	def set_key_value(self):  
		node_successor=self.successor
		if node_successor.managekey_value:
			for i in range(len(node_successor.managekey_value)):
				if distance.distance(self.m, node_successor.managekey_value[i]['key'],self.keyID,node_successor.keyID) or node_successor.managekey_value[i]['key']==self.keyID:
					obj= node_successor.managekey_value[i]
					self.managekey_value.append(obj)
					node_successor.managekey_value.remove(obj)
					return True
		else:
			return True


	def join(self,n=None):
		if(n!=None):
			self.init_finger_table(n)
			# print'---------------NEXT-------------'
			self.set_key_value() 
			# print'---------------NEXT-------------'
			self.update_others()
			# print'---------------NEXT-------------'
			print 'next'
			self.init_list_successor()
			# print'---------------NEXT-------------'
			self.copy_data()
		else:
			print('node_goc_id: ',self.NodeID)
			for i in range(self.m):
				node_finger= finger_table.Finger(self.keyID,i)
				node_finger.node= self
				self.finger.append(node_finger)
			self.predecessor=self
			self.successor=self
	

	
	def insert(self,value,duongdi=[]):
		duongdi.append(self.NodeID)
		keyID= hashkey.hashkey(value)
		key_value={'key': keyID, 'value':value}
		if(distance.distance(self.m,self.predecessor.keyID,keyID, self.keyID) or keyID==self.keyID):
			if self.managekey_value:
				for keyvalue in self.managekey_value:
					if keyvalue['key']==keyID:
						keyvalue['value']= value
						for success in self.list_successor:
							if success.status==True:
								if success.managekey_value.count(key_value)==0:
									success.managekey_value.append(key_value)
								else:
									for kv in success.managekey_value:
										if kv['key']==keyID:
											kv['value']=value
						kq= {'duong di': duongdi,'NodeID': self.NodeID,'key-value': key_value}
						return json.dumps(kq,indent=4)

				self.managekey_value.append(key_value)
				# cap nhat ban sao sang cac node ke tiep
				for success in self.list_successor:
					if success.status==True:
						if success.managekey_value.count(key_value)==0:
							success.managekey_value.append(key_value)
						else:
							for kv in success.managekey_value:
								if kv['key']==keyID:
									kv['value']=value
				kq= {'duongdi': duongdi,'NodeID': self.NodeID,'key-value': key_value}
				return json.dumps(kq,indent=4)
			
			else:
				self.managekey_value.append(key_value)
				# cap nhat ban sao sang cac node ke tiep
				for success in self.list_successor:
					if success.status==True:
						if success.managekey_value.count(key_value)==0:
							success.managekey_value.append(key_value)
						else:
							for kv in success.managekey_value:
								if kv['key']==keyID:
									kv['value']=value

				kq= {'duongdi': duongdi,'NodeID': self.NodeID,'key-value': key_value}
				return json.dumps(kq,indent=4)
		else:
			node= self.find_successor(keyID,duongdi)
			if node==False:
				return "node chua data bi loi hoac khong hoat dong"
			else:
				return node.insert(value,duongdi)



	def fix_finger(self,n,i):
    		if self.finger[i].node.keyID==n.keyID:
				self.finger[i].node=n.successor
				p=self.predecessor
				if p==n:
    					return True
				p.fix_finger(n,i)



	def remove(self):
		node_successor= self.successor
		node_predecessor= self.predecessor
		for key_value in self.managekey_value:
			node_successor.managekey_value.append(key_value)
		node_successor.predecessor=node_predecessor
		node_predecessor.successor= node_successor
		for i in range(self.m): 
			if self.keyID >= 2**i:
				p=self.find_predecessor(self.keyID - 2**i)
			else:
				p= self.find_predecessor(self.keyID - 2**i + 2**self.m)
			p.fix_finger(self,i)
		return True


	def lookup(self, keyID,duongdi=[],count=0):
		# value= None
		duongdi.append(self.NodeID)
		if(distance.distance(self.m,self.predecessor.keyID,keyID,self.keyID) or self.keyID==keyID):
			for key_value in self.managekey_value:
				if key_value['key']==keyID:
					print 'gia tri data la: ', key_value['value']
					kq={'duongdi':duongdi,'key':key_value['key'],'data': key_value['value'],'thuoc Node': self.NodeID}
					count=len(duongdi)
					print 'cost: ', count
					return count
					# return json.dumps(kq,indent=3)
			print'da tim thay vi tri nhung khong co gia tri voi keyID = ',keyID,' thuoc node: ', self.NodeID
			kq={'duongdi':duongdi,'key':keyID,'data': None,'thuoc Node': self.NodeID}
			count=len(duongdi)
			print 'cost: ', count
			return count
			# return json.dumps(kq,indent=3)
		else:
			node=None 
			n = self.find_predecessor(keyID,duongdi)
			# print node
			if n==False:
				return False
			if n.successor.status==False:
				for nod in n.list_successor:
					if nod.status==True:
						node=nod
						break
			else:
				node=n.successor
			if node is None:
				return False
			if(distance.distance(self.m,n.keyID,keyID,node.keyID) or node.keyID==keyID):
				for key_value in node.managekey_value:
					if key_value['key']==keyID:
						print 'gia tri data la: ', key_value['value']
						kq={'duongdi':duongdi,'key':key_value['key'],'data': key_value['value'],'thuoc Node': node.NodeID}
						count=len(duongdi)
						print 'cost: ', count
						return count
						# return json.dumps(kq,indent=3)
				print'da tim thay vi tri nhung khong co gia tri voi keyID = ',keyID,' thuoc node: ', node.NodeID
				kq={'duongdi':duongdi,'key':keyID,'data': None,'thuoc Node': node.NodeID}
				count=len(duongdi)
				print 'cost: ', count
				return count
				# return json.dumps(kq,indent=3)
			# print node.NodeID
			return node.lookup(keyID,duongdi)
		


	def get_infor(self):
		print '-----------------------------------------------------------------'
		print 'NodeID: ', self.NodeID,' keyID : ',self.keyID
		print 'NodeID_successor: ',self.successor.NodeID
		print 'NodeD_predecessor: ',self.predecessor.NodeID
		print 'list-successor: '
		for list_successor in self.list_successor:
			print list_successor.NodeID
		print 'thong tin quan ly key-value: '
		if self.managekey_value:
			print self.managekey_value
		else:
			print 'manageKey-value rong'
		print '---------------------------finger table-------------------------'
		print 'index------------------------------start---------------------------------successor-NodeID-----'
		for fin in self.finger:
			print fin.index,'--------', fin.start,'------------',fin.node.NodeID
		print '---------------------------end------------------------------------'
		a={
		'status': self.status,
		'NodeID': self.NodeID,
		'keyID': self.keyID,
		'NodeID successor': self.successor.NodeID,
		'NodeID predecessor': self.predecessor.NodeID,
		'manage key-value': self.managekey_value,
		}
		return json.dumps(a,indent=4)


		
	


	