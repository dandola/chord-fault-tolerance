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

def init_list_successor():
	i=1
	while success.NodeID!= self.NodeID && i <= config.len_nodes:
		self.list_successor[i]=success
		for key_value in self.managekey_value:
			success.managekey_value.append(key_value)
		i+=1
		success=success.successor
	return True

def copy_data():
	pred= self.predecessor
	i=1 
	while pred.NodeID!= self.NodeID && i <= config.len_nodes:
		pred.list_successor[i]=pred
		for key_value in pred.managekey_value:
			self.managekey_value.append(key_value)
	return True

