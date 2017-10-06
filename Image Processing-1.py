#28.09.2017


# coding: utf-8

# In[1]:


a=10
print(a)


# In[2]:


import math
def findDistance(x,y):
    return math.sqrt(
    (x[0]-y[0])**2
        +
    (x[1]-y[1])**2
    )


# In[3]:


d=findDistance([3,0],[0,4])
d


# In[4]:


from scipy import ndimage
from scipy import misc
f=misc.face()
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()


# In[5]:


f.ndim


# In[6]:


f.shape


# In[7]:


type(f)


# In[14]:


f[:,:,2]=0
plt.imshow(f)
plt.show()


# In[10]:


type(f.shape)


# In[11]:


im_size=f.shape
im_size[0]


# In[13]:


center=[im_size[0]/2, im_size[1]/2]
center


# In[15]:


from scipy import ndimage
from scipy import misc
f=misc.face()


# In[16]:


for i in range(im_size[0]):
    for j in range(im_size[1]):
        if findDistance([i,j],center)>400:
            f[i,j,:]=0


# In[18]:


plt.imshow(f)
plt.show()


# In[ ]:


# 

