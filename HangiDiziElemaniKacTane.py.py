
# coding: utf-8

# In[64]:


import numpy as np
arrayExample = []
arraySize = 10

for i in range(arrayRange):       
    arrayExample.append(np.random.randint(10))  #1'den 10 kadar rastgele sayılar üreterek 10 elemanlı bir dizi oluşturduk
    
for i in range(len(arrayExample)):                               
    print(i+1,". eleman  :", arrayExample[i])        #Bu diziyi kontrol amaçlı yazdırdık.

print("------------------------------")
tempArray = []
for i in range(arraySize):
    temp = 0
    for j in arrayExample:
        if(i==j):
            temp +=1
    tempArray.append(temp)
    
for i in range(arraySize):
    for j in arrayExample:
        if(i==j):
            print("|",i," elemanından", tempArray[i], " adet var |")
            break
    
print("------------------------------")
    


    

