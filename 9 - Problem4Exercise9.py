#9. Let v be the vector: v = [1 8 8 2 1 3 9 8]. Set a new variable x to be the number of 1s in the vector v 
#	31/08/2015		Draft Version

from numpy import *
a = array([1, 8, 8, 2, 1, 3, 9, 8])

#Create List from array
b = list(a)

#Count elements in list - Number of 1's
x = b.count(1)

print 'Number of 1s'
print x

