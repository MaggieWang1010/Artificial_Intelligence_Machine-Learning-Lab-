# -*- coding: utf-8 -*-
"""NumPy2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_jIFjADMZuyQ1SDBE6GK0oxWrdnQ_lNr
"""

######NumPy-ii
#-------------------------Commonly used NumPy functions-------------------
import numpy as np
a = np.random.randint(0,10,(5,5))
a.max() # max in all elem in matrix
a.min()
a.max(axis=0) # axis=0 is for each col
a.max(axis=1) # axis=1 is for each r
a.max(axis=1)	# axis=1 is for each row
print(a.flatten())	# flatten matrix
a.argmax()	# flatten matrix first and return max value's index a.argmin()
a.argmax(axis=0)	# max value's index in each column a.argmax(axis=1)	# max value's index in each row

a.mean()	# mean from all elem matrix
a.sum()	# sum of all elem in matrix

a.mean(axis=0)	# mean in each column a.mean(axis=1)	# mean in each row
a.std()	# standard deviation = sqrt(variance) a.std(axis=0)	# standard deviation in each col a.var()	# variance
a.var(axis=0)	# variance in each col

a.cumsum()	# array of cumulative sum 
            # a.cumsum() -> array([1,(1+2),(1+2+3),10,15,21])
a.cumprod()	# array of cumulative product # e.g.
            # a.cumprod() -> array([1,(1*2),(1*2*3),10,15,21])
np.sort(a)	# sort matrix row by row
np.argsort(a)	# return index matrix after sorting row by row

A = np.array([1,2,3])
B = np.array([4,5,6])

np.average(A, weights=B)	# B is matrix
# A=[1,2,3];	B=[4,5,6]
# np.average(A, weight=B) => 1*(4/(4+5+6)) + 2*(5/(4+5+6)) + 3*(6/(4+5+6)) mult = A*B
np.average(A)	# =np.mean(A)

a=np.array([[1,2],[3,4]])
b=np.array([[11,12],[13,14]])
np.vdot(a,b)	# e.g.


# np.vdot(a, b)	# 1*11 + 2*12 + 3*13 + 4*14 
a=np.array([1,2,3,6,7])
np.median(a)
# median value for 1,2,3,6,7 -> median=3
# median value for 1,2,6,7 -> (2+6)/2 = 4.0

a=np.array([1,0,0,2,3])
a.nonzero()	# a=[1,0,0,2,3]; a.nonzero()=[0, 3, 4] return nonzero elem index

np.inner(A,B)	# = A*B.T
np.dot(A,B)	# = A*B

np.outer(A,B)	# = A.T*B 
A=np.array([[1,2],[3,4]])
np.transpose(A)

A.trace()	# sum of all elements in quare-matrix A's diagonal A=np.array([3,1,3,4])
np.diff(A)	# if A=[3,1,3,4], then np.diff(A) = [(1-3),(3-1),(4-1)]

#-------------------------Histograms functions-------------------------
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4500)	# Create the same group number of random number for each time running

mean=150
sd=10 
N=1000

heights=np.random.normal(mean, sd, N)
#np.random.normal -> create random number based on mean/st/N

density=False	# Switch between regular histogram and pdf 
hist,bin_edges=np.histogram(heights, bins=50, density=density)
# np.histogram -> put elem in heights array into 50 bins 
cum_hist=np.cumsum(hist)	# add all elem in hist together
# Normalized histogram 
norm_hist = hist/N
# Cumulative Normalized histogram 
norm_cum_hist = np.cumsum(norm_hist)

bin_width=bin_edges[2]-bin_edges[1] 
print('Bin Width',bin_width)

plt.figure()	# create a new figure
# plt.plot(bin_edges[:-1], hist, color='green', label='heights histogram') # bin_edges[:-1] from 1st elem to last 2nd elem
plt.plot(bin_edges[:-1], cum_hist, color='green', label='heights histogram')

# plt.plot(bin_edges[:-1], norm_hist, color='green', label='heights histogram')

# plt.plot(bin_edges[:-1], norm_cum_hist, color='green', label='heights histogram')
plt.xlabel('Heights') 
plt.ylabel('Frequency') 
plt.grid()
plt.legend()
plt.title('Histogram/Density Function of Heights of college students') 
plt.show
#----------------Reshape function-------------------
import numpy as np
a=np.arange(9) 
b=a.reshape(3,3)

#b=a.reshape(5,3)	# Error ! no enough element in a 
b.flatten()	# single line array 
b.flatten(order='F')
# flatten by Fortran language seq. By default, it is C language seq. 
a=np.arange(12).reshape(4,3)
np.transpose(a)

b=np.arange(8).reshape(2,4) 
c=b.reshape(2,2,2)

np.rollaxis(c,2,1)	# change row & col 
np.swapaxes(c,1,2)
#----------------Numpy Arithematic operation--------------
a=np.arange(9).reshape(3,3) 
b=np.array([10, 10, 10])
np.add(a,b) 
np.subtract(a,b)
np.multiply(a,b) 
np.divide(a,b)
#----------------Slicing----------------------------
a=np.arange(20)
a[4:]	# from ind4 to the end
a[:4]	# from 1st to ind4 
a[slice(2,9,2)]	# from 2 to 8 with 2-step

#----------------Iterating over array-----------------
a=np.arange(0, 45, 5) 
a=a.reshape(3,3)
for x in np.nditer(a): # n-dimension iterator 
  print (x)

#----------------Iteration order(c-style & f-style)-----------
for x in np.nditer(a, order="C"):	# In c seq iteration 
  print(x)

for x in np.nditer(a, order="F"):	# In Fortran seq iteration 
  print(x)

#---------------Joining arrays----------------- 
a=np.array([[1,2],[3,4]]) 
b=np.array([[5,6],[7,8]])
np.concatenate((a,b))	# Join by col 
np.concatenate((a,b), axis=1)	# Join by row

#----------------Splitting array-----------------
a=np.arange(9)
np.split(a,3)	# create 3 arrays
np.split(a,[4,7])	# seperate from ind4 and ind7 into 3 pieces

#-----------------Resizing arrays-----------------
a=np.array([[1,2,3],[4,5,6]]) 
a.shape

b=np.resize(a, (3,2)) # change to 3x2 matrix
b=np.resize(a, (3,3)) # change to 3x3 matrix by repeating 1st row
#------------------Numpy practise example-----------------
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y) 
plt.show()

# Create a 6x6 2-dim array, and let 1 and 0 be placed alternatively across the diagonals
z=np.zeros((6,6),dtype=int)
z[1::2, ::2] = 1	# 1st:last:step

z[::2, 1::2] = 1	# 1st:last:step
# Find the total number and locations of missiong values in the array 
z=np.random.rand(10,10)
z[np.random.randint(10, size=5), np.random.randint(10, size=5)]=np.nan 
# np.random.randint(10, size=5) return array with 5 elem from 1 to 10
# z[[],[]] for elem index
np.isnan(z).sum() 
np.argwhere(np.isnan(z))

inds=np.where(np.isnan(z)) # return ind array 
z[inds]=0
#------------------Linear regression by scikit-learn library-------------------

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([1,3,5,7,9,11,13,15,17,19]).reshape((-1, 1))
# reshape((-1, 1)) : '-1' means unknown number of row; '1' means one column 
y = np.array([3,3,7,7,11,11,15,15,19,19])

model = LinearRegression().fit(x, y)

print('intercept:', model.intercept_) 
print('slope:', model.coef_)
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n') 
new_y = model.predict([[20]])
print('predicted response if x=20:', new_y , sep='\n')