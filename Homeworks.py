✔  Anaconda & Jupyter Notebook kurulumu gerçekleştirildi ve alıştırmalar yapıldı.

✔  Görüntü işlemede kullanılan uygulamalara örnek olarak masaüstü ortamında Adope Photoshop ve Photoscape X Pro, 
mobil olarak IOS'da ise Snapseed, InkHunter, BlendEditor gibi uygulamalar incelendi.

✔  Python programlama dili basicleri öğrenilip, rastgele sayılar içeren dizi oluşturup, hangi elemandan kaç adet 
olduğunu çıktı veren programla uygulamaya geçildi.


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

            ÇIKTISI >>>   1 . eleman  : 2
                          2 . eleman  : 1
                          3 . eleman  : 5
                          4 . eleman  : 2
                          5 . eleman  : 2
                          6 . eleman  : 9
                          7 . eleman  : 0
                          8 . eleman  : 1
                          9 . eleman  : 5
                          10 . eleman  : 9
                          ------------------------------
                          | 0  elemanından 1  adet var |
                          | 1  elemanından 2  adet var |
                          | 2  elemanından 3  adet var |
                          | 5  elemanından 2  adet var |
                          | 9  elemanından 2  adet var |
                          ------------------------------
                 
                 
✔ Python'da bir resim okut. Okuttuğun resmin üzerine, orjinal resimi yuvarlak bir şekilde ortada bırakcak
   bir çerçeve ile kapla. Python kütüphanlerini kullan.
   
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
            
            import math   #sqrt fonksiyonu için lazım olan kütüphane
            def findDistance(x,y):
                return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)  #iki nokta arası uzaklıgı bulan fonksiyon

            plt.imshow(image)
            plt.show()    #test amaçlı resime bakış

            for i in range(imageHeight):
                for j in range(imageWidth):
                    if findDistance([i,j],center)>130:   #  İki nokta arasındaki uzaklıgın 130 dan sonraki kısımlarını siyah yap. Yani merkez
                        image[i,j,:]=0                   # etrefında 130 yarıçapında bir çember oluştur ve dışarda kalanları siyaha boya

            plt.imshow(image)
            plt.show()  #Siyah çerçeve oluşturdu.
   
   
  ✔ 
   
