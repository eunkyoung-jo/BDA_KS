#2018/11
import numpy as np
import matplotlib.pyplot as plt

a_list = list(range(10)) #explicitly given
print('list', type(a_list), a_list)
np_data = np.arange(10) #just like a list
print('numpy', type(np_data), np_data)
print(a_list.shape) # list object no have 'shape' method.
print(a_list.reshape) # no have 'reshape'
print(np_data.shape)
print(np_data.reshape(2,5))
print(np_data.reshape(2,5).T)

input('Show me the plots of list array and numpy array')
sp1=plt.subplot(311)
sp1.plot(a_list, 'ro', label='list')
plt.legend(loc='upper left')
plt.title('list vs. numpy')

sp2= plt.subplot(312)
sp2.plot(np_data, 'bx', label='numpy')
plt.legend(loc='upper left')

np_data = np.random.rand(10) # randomly represent data with a method.
sp3= plt.subplot(313)
sp3.plot(np_data, 'bo', label='numpy')
plt.legend(loc='upper center')

plt.show()
plt.close()

