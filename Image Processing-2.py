#05.10.2017

# coding: utf-8

# In[8]:


def createList(size):
    myList=[]
    for i in range (size):
        myList.append(i)
    return myList

def listIncrement(l,n):
    myL=[]
    for i in range (len(l)):
        myL.append(l[i]+n)
    return myL
#createList fonksiyonuyla 5 elemanlı bir dizi oluşturuldu
L_1=createList(5)
L_1
# OUTPUT =>  [0, 1, 2, 3, 4] 

#L_1 dizisinin her elemanına 5 eklenerek yeni bir diziye atayıp onu döndürür
L_2=listIncrement(L_1,5)
L_2

# OUTPUT =>  [5, 6, 7, 8, 9]


# In[9]:


get_ipython().magic('timeit myL_1=listIncrement(createList(1000),50)')


# In[13]:


import numpy as np
get_ipython().magic('timeit np.arange(1000)+1')


# In[14]:


size=10
my_10=np.arange(size)
my_10


# In[15]:


my_10+1


# In[16]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimage
import numpy as np


# In[17]:


img=mpimage.imread('C:\koala.jpg')


# In[18]:


img.ndim


# In[19]:


img.shape


# In[20]:


plt.imshow(img)
plt.show()


# In[21]:


img[:,100,:].max()


# In[22]:


img_1=img[1:375:2,:,:]
#1:375:2 x bileşeni için 375 -> 1 den oraya kadar 2şer 2şer git.


# In[23]:


img_1=img[:,1:500:2,:]
#1:500:2 y bileşeni için 500 -> 1 den oraya kadar 2şer 2şer git.


# In[27]:


#plt.subplot(1,2,1), plt.imshow(img)
#plt.subplot(1,2,2), plt.imshow(img_1)

plt.imshow(img_1)
plt.show()


# In[29]:


img.ndim,img.shape #RGB ve dimentions


# In[30]:


img_20=np.zeros((500,375,3))
img_20.shape


# In[31]:


for i in range(375):
    for j in range(500):
        img_20[j,i,:]=img[i,j,:]


# In[32]:


img_30=np.zeros((500,375,3))
img_30.shape


# In[33]:


for i in range(375):
    for j in range(500):
        img_30[j,i,:]=1-img[i,j,:]

#resmin negatigi


# In[37]:


img_40=np.zeros((500,375,3))
img_40.shape


# In[40]:


for i in range(375):
    for j in range(500):
        img_40[j,i,:]=img[i,j,:]
        
# x ve y ye göre s,metriğini aldı yani orjine göre ayna görüntüsünü aldı.
# 500-j-i yerine j yazsaydık sadece x eksenine göre simetrisini alacaktı


# In[42]:


plt.subplot(1,4,1),plt.imshow(img)
plt.subplot(1,4,2),plt.imshow(img_20)
plt.subplot(1,4,3),plt.imshow(img_30)
plt.subplot(1,4,4),plt.imshow(img_40)
plt.show()



