
# coding: utf-8

# In[2]:


# 1. kısım : image --> RGB --> Graylevel ---> Monachrome(BW)
# 2. kısım : labelling (T değerini parabolde kaydırarak en düşük varyanslı noktayı bulana kadar döngüde olacak 0-255)


# In[3]:


#Resmş okutup greylevela çevirelim

import matplotlib.pyplot as plt
import numpy as np


# In[44]:


img_1 = plt.imread("resim.jpg")
img_1.ndim
img_1.shape
#boyutları yarıya indirdi
img_2 = img_1[1:400:2,1:500:2]
img_2.ndim,img_2.shape
img_3 = np.zeros((img_2.shape[0:2]))
img_3.shape
img_4 = np.zeros((img_2.shape[0:2]))
img_4.shape


# In[49]:


threshold = 100
for i in range(img_2.shape[0]):
    for j in range(img_2.shape[1]):
        n = img_2[i,j,0]/3 + img_2[i,j,1]/3 + img_2[i,j,2]/3
        img_3[i,j]=n
        if n>threshold:  # 100 referans 100'e göre siyah/beyaz
            img_4[i,j]=255
        else:
            img_4[i,j]=0
            
plt.subplot(1,3,1),plt.imshow(img_2)
plt.subplot(1,3,2),plt.imshow(img_3,plt.cm.gray)
plt.subplot(1,3,3),plt.imshow(img_4,plt.cm.binary)
plt.imshow(img_4,plt.cm.binary)
plt.show()


# In[60]:


img1 = plt.imread("plaka.jpg")
img5 = np.zeros((img1.shape[0:2]))
img2=img1

threshold = 10
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        n=img2[i,j,0]/3 + img2[i,j,1]/3 + img2[i,j,2]/3 
        if n>threshold:
            img5[i,j]=255
        else:
            img5[i,j]=0
            
plt.subplot(1,2,1), plt.imshow(img2)
plt.subplot(1,2,2), plt.imshow(img5, plt.cm.binary)
plt.show()


