
# coding: utf-8

# In[11]:

# x.jpg var (RGB) ----> imread ---> graylevel,BW(monochrome) ----> sparce matrix ve histogramda görecez
# histogram nasıl tutuluyor? bir resim var resimde değişik intensity değerleri var. (sayılardan oluşan 
# bir matrisde bir değerden kaç tane olduğunu tutar).Black-white aldığımızda 2 değer olacak 0dan kaç tane 
# var 1 kaç tane var. 1 ve 0 lar çok fazla oldugundan sparce matrıs konusuyoruz. RGB resimler için sparce
# matris anlamsız olur.

#myList = [1,3,4,2,1,5,6,9,5,2,1,40]
#myList #denedik, liste oluşmuş. ok.

import numpy as np
my_Numbers = np.random.randint(1,10,5)
my_Numbers  # -10 il 10 arasında 5 adet rastgele sayı üretti. ok.
myHistogram =[[my_Numbers[0],1]]
my_Numbers, myHistogram , len(myHistogram)


# In[49]:

import numpy as np
my_Numbers = np.random.randint(1,10,5)
my_Numbers #resım olmalı


# In[51]:

my_Numbers = np.random.randint(1,10,5)
my_Numbers  #resım olmalı


# In[63]:

my_Numbers2 = np.random.randint(1,10,5)
my_Numbers2  #resım olmalı Black-white


# In[66]:


myHistogram =[[1,0]]
for number in my_Numbers2:
    for item in range(1):
        if(myHistogram[item][0]==number):
            myHistogram[item][1]+=1 
        else:
            myHistogram.append([number,1])
        

myHistogram  #hangi elemandan kaç adet olduğunu tutuyor örenğin [(2,3),(3,1)] şeklinde 2 den 3 tane 3 den 1 tane var gibi. 


# In[ ]:

#a) Histogram(frekans) nedir? RGB,graylevel,BW(monochrome) bir resmin histogram grafiği nasıldır?
#b) BW monochrome resimler için histogram grafiğini list ile dictype ile oluşturunuz. **TUPPLE olmuyor histogram için!**
#c) 0/1 oranını bulunuz
#d) c şıkkında elde ettiğiniz oran değeri %20 ve altında bir değer ise resmi Matris(D,f) şeklindeki bir sparce matrise atayacak olan D ve f değerlerini elde ediniz
#e) d de elde ettiğiniz matris için farklı karşılaştırma değerlerinden vector-norm() fonksiyonunu yazın.
#f) d de elde ettiğiniz 2 veya daha fazla resmi karşılaştıran distance() fonksiyonunu yazınız.
#g) 2 tane sparce matris alan ve geriye bunların farkını gönderen fonksiyonu n defa çağırıp en küçük distance
#   değerini veren resmin indisini return eden fonksiyonu yazınız
#h) k-means = f şıkkındaki distance fonksiyonunu KNN Algoritmasına göre tekrar yazınız.
#i) Fonksiyonunun ön tanımını yazınız. (9  puan)
#j) Fonksiyonunun kendisini yazınız.
#
#Resim nedir nasıl elde edilir nasıl gösterilir nasıl saklanır?
#Resim işleme algoritmaları kaça ayrılır?
#1- Pixel yoğunluk intensity
#2- mekansal
#3- morphology alg.
#4- frecuancy faz-sıklık dönüşümü gerektiren fonksiyonlar
#
#1 için -> Bir resimdeki kırmızı tonu arttıran intensity fonksiyonunu yazınız.
#2 için -> Sobel mask nedir? Sobel mask ı graylevel bir resme uygulayan fonksiyonu yazınız. (Resimde türev alır)
#          Kenarları daha belirgin hale getirmiş olacaktır.
#3 için -> circle falan filan.
#4 için -> yok
#
#Resim işleme gerektiren uygulamalarda ne tür kısıtlamalar vardır.
#Marker nedir? Günlük hayatta kullanılan görüntü işleme teknolojilerin ne gibi kısıtlamaları vardır?
#Kendisine gönderilen bir resmi en küçük intensity a değerini c ye, b değerini d ye çeviren fonksiyonu yazınız.
#Odaklanma -> kamerayı dışarıdan içeriye doğru çevirince ekran bir anlık kararır siyah olur sonra 
#a) k-means: K en yakın komşu ve bayes algoritmaları ile OCR nasıl yapılır? 
#b) Birbirlerine göre avantaj ve dezavantaj nedir?
#c) OCR için resim üzerinde kaç karakter olduğunu nasıl buluruz.
#d) CCL
#Endüstriyel uygulamalarda 
#
# In[ ]:



