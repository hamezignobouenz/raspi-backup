colors = ["black","white"] 
sizes = ["S","L","M"]
t = [(color,size) for color in colors for size in sizes]
print(t)

symbols = "%@)%&"
tuple(ord(symbol) for symbol in symbols)

import array

print(array.array('I',(ord(symbol)for symbol in symbols)))
print("\n")
print("now is time for some genexps bitch !")

for tsh in('%s %s' % (c,s) for c in colors for s in sizes):
    print(tsh)

print("\n")

travlist = [("USA","p1"), ("FR","P2"), ("ESP","p3")]
for pssp in sorted(travlist):
    print("%s/%s" % pssp)

for country, _ in travlist:
    print(country)

print("\n")
print("Is the underscore a variable ?")

print("\n")
print("\n")
print("time for some OS")
print("\n")
import os

_ , filename = os.path.split('/home/luciano/.ssh/the.file') 
print(filename)
print(_)

## Slicing
l = [10, 20, 30 ,40]

# Named tuple 
print('switching to named tuples')
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.90, (80.23,139.456))
print(tokyo)
print('Testing some text formatting on the named tuples')
print('{}, {}'.format(*tokyo.coordinates))
print("tokyo's GPS coordinates are {0.coordinates}".format(tokyo))

#############################
 # This is a cool comment in Python
##############################
#import numpy as np
#a = np.array([1,2,3,4])
#print(a)
#import pandas as pd
#s = pd.Series([1,2,3], index = ['a', 'b', 'c'])
#s.index
#s[['a','c']]
