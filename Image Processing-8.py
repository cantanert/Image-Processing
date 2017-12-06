
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
image1=plt.imread("stark.jpg")


# In[3]:


def convert_RGB_to_monochrome_BW(image_1):
    threshold=100
    img_2=np.zeros((image_1.shape[0],image_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if (image_1[i,j,0]/3+image_1[i,j,1]/3+image_1[i,j,2]/3)>threshold:
                # img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
                img_2[i,j]=1
            else:
                img_2[i,j]=0
    # print(img_1.shape)
    return img_2


# In[4]:


image1BW=convert_RGB_to_monochrome_BW(image1)


# In[5]:


plt.subplot(1,2,1), plt.imshow(image1)
plt.subplot(1,2,2), plt.imshow(image1BW, cmap="gray")
plt.show()


# In[6]:


def define_mask():
    mask = [[1,1,1],[1,1,1],[1,1,1]]
    mask, mask[1][2], mask[0][0], mask[2][2] # mask[3][1]  error!
    for i in range(3):
        for j in range(3):
            print (mask[i][j], end=" ")
        print()   #Matris formunda yazdırma
    return mask


# In[17]:


def my_dilation(img_1,mask):
    m=img_1.shape[0]
    n=img_1.shape[1] #img_1'in boyutları
    img_2 = np.random.randint(0,1,(m,n))
    for i in range(1,m-1): # Range 0 yerine 1'den başlasın
        for j in range(1,n-1):
            print(i,j,img_1[i,j])
            # apply_mask_1 for dilation,
            x_1=img_1[i,j] and mask[1][1]  #Bulunduğumuz merkez

            x_2=img_1[i-1,j-1] and mask[0][0] #SOL
            x_3=img_1[i-1,j] and mask[0][1]   #ORTA
            x_4=img_1[i-1,j+1] and mask[0][2] #SAG

            x_5=img_1[i+1,j-1] and mask[2][0] #SOL
            x_6=img_1[i+1,j] and mask[2][1]   #ORTA
            x_7=img_1[i+1,j+1] and mask[2][2] #SAG

            x_8=img_1[i,j-1] and mask[1][0] #SOL
            x_9=img_1[i,j+1] and mask[1][2] #SAG

            result = x_1 or x_2 or x_3 or x_4 or x_5 or x_6 or x_7 or x_8 or x_9
            img_2[i,j]=result

    return img_2


# In[18]:


image1BW.ndim  #must be 2


# In[19]:


mask = define_mask() #1 1 1
                     #1 1 1
                     #1 1 1


# In[21]:


image1BWdilated = my_dilation(image1BW, mask)


# In[23]:


plt.subplot(1,3,1), plt.imshow(image1,)
plt.subplot(1,3,2), plt.imshow(image1BW, cmap="gray")
plt.subplot(1,3,3), plt.imshow(image1BWdilated, cmap="gray")
plt.show()

