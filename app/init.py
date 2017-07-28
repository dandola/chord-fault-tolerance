from flask import Flask,request
import node
import distance
import main
import ring
import config
import json
import finger_table
app=Flask(__name__)
@app.route('/create',methods=['POST'])
def create():
	if request.method=='POST':
		id_ring= int(request.form['id_ring'])
		if(main.create_ring(id_ring)):
			return "tao ring thanh cong!"
		else:
    			return "tao ring loi"
		

@app.route('/join', methods=['POST'])
def join():
	if request.method=='POST':
		NodeID= int(request.form['NodeID'])
		id_node_joinded=int(request.form['NodeID_joined'])
		print'----------------------------tien hanh join---------------------------'
		return main.join(NodeID,id_node_joinded)
		

@app.route('/lookupkey',methods=['POST'])
def lookupkey():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])	
		keyID= int(request.form['keyID'])
		data=None
		print'----------------------------tien hanh lookup---------------------------'
		return main.lookup(id_node_joinded,keyID,data)

@app.route('/lookupdata',methods=['POST'])
def lookupdata():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])	
		data= int(request.form['data'])
		keyID=None
		print'----------------------------tien hanh lookup---------------------------'
		return main.lookup(id_node_joinded,keyID,data)
			

@app.route('/insert', methods=['POST'])
def insert():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])
		data= int(request.form['data'])
		print'----------------------------tien hanh insert---------------------------'
		return main.insert(id_node_joinded,data)


@app.route('/remove',methods=['POST'])
def remove():
	if request.method == 'POST':
		NodeID=int(request.form['NodeID'])
		print'----------------------------tien hanh remove---------------------------'
		return main.remove(NodeID)


@app.route('/infor', methods=['POST'])
def infor():
	if request.method=='POST':
		node_id= int(request.form['NodeID'])
		if node_id==-1:
			print'----------------------------------------------'
			print 'in tat ca cac thong tin co trong ring'
			return main.infor_nodes(node_id)
		else:
			return main.infor_nodes(node_id)



@app.route('/save')
def save():
	if main.save():
		return 'save thanh cong!!!'
	return 'false'


@app.route('/load')
def load():
	result= main.load()
	if result:
		return 'load ring thanh cong'
	else:
		return 'da ton tai ring'


@app.route('/insert_data')
def insert_data():
	return main.insert_data()




if __name__=='__main__':
	app.run(debug=True)
