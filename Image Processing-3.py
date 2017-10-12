
##12.10.2017


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[9]:


ls


# In[10]:


import matplotlib.pyplot as plt
import numpy as np

img_1 = plt.imread("test_1.jpg")


# In[11]:


img_1.ndim, img_1.shape


# In[34]:


plt.imshow(img_1[:,:,0])
plt.show()


# In[61]:


pixel_1_rgb = [0,0,0]
pixel_1_gray_level = 0

pixel_1_rgb = [10,0,0]
pixel_1_gray_level = 10

pixel_1_rgb = [0,10,0]
pixel_1_gray_level = 10

pixel_1_rgb = [10,10,10]
pixel_1_gray_level = 12

def converRGBPixelToGreyLevel(RGB_Pixel):
    return  RGB_Pixel[0]/3 + RGB_Pixel[1]/3 + RGB_Pixel[2]/3
    


# In[62]:


converRGBPixelToGreyLevel([2,5,7])


# In[63]:


img_2=np.zeros((img_1.shape[0], img_1.shape[1]))
img_2.shape


# In[64]:


for i in range (img_1.shape[0]):
    for j in range (img_1.shape[1]):
        img_2[i,j] = converRGBPixelToGreyLevel(img_1[i,j,:])


# In[65]:


#subplot using for viewing photos inline
plt.subplot(1,2,1)
plt.imshow(img_1)
plt.subplot(1,2,2)
plt.imshow(img_2, cmap='gray')
plt.show()


# In[66]:


import scipy


# In[67]:


import scipy.misc
scipy.misc.imsave('outfile.jpg', img_2)

