
# coding: utf-8

# In[3]:



import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('puppy.png')
plt.imshow(image)
plt.show()

imageSize = image.shape
imageHeight = imageSize[0]
imageWidth = imageSize[1]
imageHeight,imageWidth  #test eni ve boyu test ettik.

center = [imageHeight/2,imageWidth/2] #resmin orta noktasının koordinatları
center


# In[4]:


import math
def findDistance(x,y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)  #iki nokta arası uzaklıgı bulan fonksiyon

plt.imshow(image)
plt.show()


# In[11]:


for i in range(imageHeight):
    for j in range(imageWidth):
        if findDistance([i,j],center)>130:   #  İki nokta arasındaki uzaklıgın 130 dan sonraki kısımlarını siyah yap. Yani merkez
            image[i,j,:]=0                   # etrefında 130 yarıçapında bir çember oluştur ve dışarda kalanları siyaha boya

plt.imshow(image)
plt.show()  #Siyah çerçeve oluşturdu.

