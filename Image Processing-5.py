
# coding: utf-8

# In[ ]:


myPoint_1 = [0,0]
myPoint_2 = [1,0]
myPoint_3 = [0,1]
myPoint_4 = [1,1]
 
import math
def uzaklik():
    value=(myPoint_1[0]-myPoint_2[0])**2 + (myPoint_1[1]-myPoint_2[1])**2
    return value
d_1_2 = math.sqrt(uzaklik())
d_1_2 #1.0

#İki vektör arasındaki uzaklığı bulan fonksiyon.
import math
def myDistance(a,b):
    myPoint_1=a
    myPoint_2=b
    a=(myPoint_1[0]-myPoint_2[0])**2
    b=(myPoint_1[1]-myPoint_2[1])**2
    return math.sqrt(a+b)
 
myPoint_1 = [0,0]
myPoint_2 = [1,0]
myPoint_3 = [0,1]
myPoint_4 = [1,1]
 
myDistance(myPoint_2,myPoint_3) #1.4142135623730951

#İki noktanın orta noktası bulundu.
a=myPoint_1[0]+myPoint_2[0]+myPoint_3[0]+myPoint_4[0]
b=myPoint_1[1]+myPoint_2[1]+myPoint_3[1]+myPoint_4[1]
centerPoint=[a/4,b/4]
centerPoint #[0.5, 0.5]

def findCenter(List_Of_Points):
    a=0
    b=0
    for point in List_Of_Points:
        a=a+point[0]
        b=b+point[1]
    l=len(List_Of_Points)
    return [a/l,b/l]
 
myPoint_1 = [0,0]
myPoint_2 = [1,0]
myPoint_3 = [0,1]
myPoint_4 = [1,1]
 
my_Point_List=[]
my_Point_List.append(myPoint_1)
my_Point_List.append(myPoint_2)
my_Point_List.append(myPoint_3)
my_Point_List.append(myPoint_4)
 
len(my_Point_List) #4
 
center=findCenter(my_Point_List)
center #[0.5, 0.5]

import numpy as np
my_Array=np.array([[1,2,3],[2,6,9]],np.int32)
my_Array.ndim, my_Array.shape
my_Array_1=my_Array.reshape(1,6)
print(my_Array)
print("")
print(my_Array_1)
 
#[[1 2 3]
# [2 6 9]]
#
#[[1 2 3 2 6 9]]

