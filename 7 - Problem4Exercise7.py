#Reshape command (from Mat class) to form a new matrix z =[1 3 5;2 4 6]. 
#	30/08/2015		Draft Version

from numpy import *
a = array([[1,2,3,4,5,6]])
#print a

#3 Rows, 2 Columns
b = a.reshape(3,2)
#print b

#Invert to obtain expected results
c = transpose(b)
print 'Result'
print '-------'
print c

