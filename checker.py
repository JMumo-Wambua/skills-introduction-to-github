from array import *

values1 =array('i', [5,7,9,3,0,7,2])

cheack = 0

for x in values1:
    if values1[0:6] == 2:
        print("Values are present")
        
    else:
        cheack +=1
print(cheack)