import numpy as np
import matplotlib.pyplot as plt
import read_json

obj=[64,128,256,512,1024,2048]
list_maxx=read_json.list_max
list_meann=read_json.list_mean
list_minn=read_json.list_min

list_maxx1=read_json.list_max1
list_meann1=read_json.list_mean1
list_minn1=read_json.list_min1

print list_meann
x=np.arange(len(obj))

fig, ax = plt.subplots()
rect1=ax.bar(x,list_meann,width=0.6,linewidth=1,align='center',color='green',label='chi phi trung binh')
rect2=ax.bar(x,list_meann1,width=0.6,linewidth=1,align='center',alpha=0.4,color='green',label='chi phi trung binh voi 40% node loi')

ax.plot(x,list_minn,color='red',marker='o',markersize=10,linewidth=1.0,label='chi phi min')
ax.plot(x,list_maxx,color="brown",marker='*', markersize=14, linewidth=1.0,label='chi phi max')

ax.plot(x,list_maxx1,color="blue",marker='*', markersize=14, linewidth=1.0,label='chi phi max voi 40% node loi')
plt.xlim(-1,10)
# plt.autoscale(enable=True,axis='x')
plt.xlabel('so luong node co trong vong ring')
plt.ylabel('chi phi trung binh cho viec lookup')
plt.title('chi phi trung binh cho thao tac lookup voi so node loi la 30%')
plt.xticks(x,obj)
ax.legend()
plt.show()

