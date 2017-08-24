import numpy as np
import matplotlib.pyplot as plt
import read_json

obj=[64,128,256,512,1024,2048]
fig, ax = plt.subplots(sharex=True)
y= np.asarray(read_json.list_mean)
print y
list_max=np.asarray(read_json.list_max)
print list_max

list_min=np.asarray(read_json.list_min)
print list_min
x=np.asarray([5,10,15,20,25,30])
error=[list_min,list_max]
# asymmetric_error= 0..5
ax.errorbar(x,y, yerr=error,fmt='o',elinewidth=1)
ax.set_title('chi phi lookup trung binh khi so node loi la 30%')
plt.xlabel('so luong node co trong ring')
plt.ylabel('chi phi lookup')
plt.ylim(0,35)
plt.xlim(0,35)
plt.xticks(x,obj)
plt.show()