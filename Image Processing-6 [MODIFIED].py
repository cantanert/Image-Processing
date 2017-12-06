
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
 
my_Numbers=np.random.randint(1,10,5)
my_Numbers #array([1, 2, 4, 3, 5])


# In[3]:


myHistogram=[]
myHistogram #[]


# In[4]:


for number in my_Numbers:
    for histItem in myHistogram:
         
        if(number==histItem[0]):
            histItem[1]=histItem[1]+1
        else:
            myHistogram.append(number,1)


# In[5]:


myHistogram


# In[6]:


var_1=(1,2,3)
var_2=(2,5,3)
var_3=(1,5,3)
var_4=(2,5,6)


# In[12]:


import numpy as np
import matplotlib.pyplot as plt
start=0
end=2
n=5
my_Numbers=np.random.randint(start,end,n)
img=plt.imread("stark.jpg")
myHistogram={}
my_Numbers #array([0, 1, 0, 1, 0])


# In[13]:


for number in my_Numbers:
        if number in myHistogram.keys():
            myHistogram[number]=myHistogram[number]+1
        else:
            myHistogram[number]=1


# In[14]:


my_Numbers, myHistogram, myHistogram[0]/myHistogram[1] 
#histogram da iki değer olmalı
#(array([0, 1, 0, 1, 0]), {0: 3, 1: 2}, 1.5)


# In[15]:


def convert_RGB_to_monochrome_BW(image_1):
    threshold=100
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if (img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3)>threshold:
                # img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
                img_2[i,j]=1
            else:
                img_2[i,j]=0
    # print(img_1.shape)
    return img_2


# In[17]:


img_1 = convert_RGB_to_monochrome_BW(r"stark.jpg")
plt.imshow(img_1, cmap="gray")
plt.show()


# In[19]:


img_1.ndim, img_1.shape #(2, (404, 404))
 


# In[21]:


i2 = img_1.reshape(1,img_1.shape[0]*img_1.shape[1])
i2.ndim, i2.shape #(2, (1, 160000))
#tek satır ve width*height sütunluk veri


# In[22]:


def get_Histogram(image): #resim monochrome olmalı
    my_Histogram = {}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            item=image[i,j]
            if item in my_Histogram.keys():
                my_Histogram[item]=my_Histogram[item]+1
            else:
                my_Histogram[item]=1
    return my_Histogram


# In[24]:


my_Histogram = get_Histogram(img_1)
my_Histogram
#Histogramda 0 ların ve 1 lerin sayısı tutuluyor


# In[27]:


x = my_Histogram[0.0]
y = my_Histogram[1.0]
print("Siyah-Beyaz Oranı: ", x/y) #Siyah-Beyaz Oranı: 5.0083195288054485 
#siyah (x) 136.051 , beyaz (y) 27.165 , x/y = 5.0083195288054485


# In[28]:


class myMatrix():
    def __init__(self,x,y):
        self.D=x
        self.F=y


# In[29]:


def create_D_F(img_1):
    d = {(i,j) for i in range(img_1.shape[0])
               for j in range(img_1.shape[1])
               if img_1[i,j]==1
        }
    f = {(i,j):1 for i,j in d}
    m=myMatrix(d,f)
    return m


# In[31]:


my_sparce_Matrix_1=create_D_F(img_1)
my_sparce_Matrix_1.D, my_sparce_Matrix_1.F

# çıktı -> ({  (266, 351), (109, 365), (381, 392), (312, 241), (185, 101), 
#              (5, 178), (171, 86), (104, 115), (157, 23), (30, 287), (284, 367),
#              (323, 275), ...},
#           {  (266, 351): 1, (109, 365): 1, (381, 392): 1, (312, 241): 1, (185, 101): 1,
#              (5, 178): 1, (171, 86): 1, (104, 115): 1, (157, 23): 1, (30, 287): 1, (284, 367): 1, 
#              (323, 275): 1, ...})

