internal_mask_1=[[1,0],[0,0]]
internal_mask_2=[[0,1],[0,0]]
internal_mask_3=[[0,0],[1,0]]
internal_mask_4=[[0,0],[0,1]]
 
external_mask_1=[[0,1],[1,1]]
external_mask_2=[[1,0],[1,1]]
external_mask_3=[[1,1],[0,1]]
external_mask_4=[[1,1],[1,0]]
 
internal_mask_list=[internal_mask_1,internal_mask_2,internal_mask_3,internal_mask_4]
external_mask_list=[external_mask_1,external_mask_2,external_mask_3,external_mask_4]

import numpy as np
import matplotlib.pyplot as plt
size=3

img_1=np.random.randint(0,2,(size,size))
#img_1 -> fake image, you should read from a file
plt.subplot(1,2,1), plt.imshow(img_1,cmap='Greys',interpolation='nearest')

img=plt.imread("JupyterExample\\t-harfi.jpg")
plt.subplot(1,2,2), plt.imshow(img,cmap='Greys',interpolation='nearest')
plt.show()

def count_mask(image,mask):
    counter=0
    m,n=image.shape
    for i in range(m-1):
        for j in range(n-1):
            a=b=c=d=False
            if(image[i,j] == mask[0][0]):
                a=True
            if(image[i,j+1] == mask[0][1]):
                b=True
            if(image[i+1,j] == mask[1][0]):
                c=True
            if(image[i+1,j+1] == mask[1][1]):
                d=True         
            if(a and b and c and d):
                counter=counter+1
    return counter
    
def count_internal_mask(image):
    counter_internal=0
    for mask in internal_mask_list:
        counter_internal=counter_internal+count_mask(img_1,mask)
    return counter_internal
     
def count_external_mask(image):
    counter_external=0
    for mask in external_mask_list:
        counter_external=counter_external+count_mask(img_1,mask)
    return counter_external

c_1=count_internal_mask(img_1) 
c_2=count_external_mask(img_1) 
c_1, c_2 #(0,1)

import math
abs(c_1-c_2)/4 #0.25

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.misc import imsave
%matplotlib inline
 
def convert_RGB_to_gray_level(image_1):
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
    # print(img_1.shape)
    return img_2
 
def convert_RGB_to_monochrome_BW(image_1,threshold=100):
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
 
def create_mask_internal():
    i_m_1=np.array([[1,0],[0,0]])
    i_m_2=np.array([[0,1],[0,0]])
    i_m_3=np.array([[0,0],[1,0]])
    i_m_4=np.array([[0,0],[0,1]])
    i_m_l=[i_m_1,i_m_2,i_m_3,i_m_4]    
    return i_m_l
 
def create_mask_external():    
    e_m_1=np.array([[0,1],[1,1]])
    e_m_2=np.array([[1,0],[1,1]])
    e_m_3=np.array([[1,1],[0,1]])
    e_m_4=np.array([[1,1],[1,0]])
    e_m_l=[e_m_1,e_m_2,e_m_3,e_m_4]  
    return e_m_l
 
def count_object(image_name_with_path,threshold=150):
    img_file_1=image_name_with_path
    img_file_2=convert_RGB_to_gray_level(img_file_1)
    img_file_3=convert_RGB_to_monochrome_BW(img_file_1,threshold)
    image=img_file_3
    c_1=0
    c_2=0  
    m,n=image.shape
    for i in range(m-1):
        for j in range(n-1):
            for mask in create_mask_internal():
                if False not in (img_file_3[i:i+2,j:j+2]==mask):
                    #print("e mask bulundu")
                    c_1=c_1+1
            for mask in create_mask_external():
                if False not in (img_file_3[i:i+2,j:j+2]==mask):
                    #print("i mask bulundu")
                    c_2=c_2+1
    number_of_objects=math.fabs((c_2-c_1)/4)
    print("Resimdeki Toplam T Sayısı:", number_of_objects)
    return number_of_objects

image_file_1="JupyterExample\\test_t.jpg"
count_object(image_file_1)

image_file_2="JupyterExample\\test_karisik.jpg"
count_object(image_file_2)
