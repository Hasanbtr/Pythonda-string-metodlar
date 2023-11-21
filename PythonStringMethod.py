#Split Metodu

#Split metodu, karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar. 

#Örnek

message="Hello World how are you"
message=message.split()
print(message)

#Upper Metodu

#Upper metodu, karakterleri büyük harfe çevirir.

#Örnek

message2="Hello World how are you"
message2=message2.upper()
print(message2)

#Lower Metodu

#Lower metodu, karakterleri küçük harfe çevirir.

#Örnek
message3="HELLO WORLD HOW ARE YOU"
message3=message3.lower()
print(message3)

#title() metodu, karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.
#Örnek

message4="hello World how are you"
message4=message4.title()
print(message4)

#capitalize(), karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.
#Örnek

message5="hello World How are you"
message5=message5.capitalize()
print(message5)

#Strip Metodu
#Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 
#Örnek

message6="    hello World        "
message6=message6.strip()
print(message6)

#Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.
#Örnek

message7="hello World How are you"
message7=message7.strip('areohyou')
print(message7)

#Replace Metodu

#Replace metodu karakter güncellemesi için kullanılır. 

#Örnek
message8="hello World How are you"
message8=message8.replace('World','Mars')
print(message8)

#replace() metotlarını ard arda kullanabiliriz. 
message8=message8.replace('World','Mars').replace('you','we').replace('hello','merhaba')
print(message8)

#Find Metodu

#Find metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception döndürür.
message8=message8.find('are')
print(message8)

#Index Metodu

#index metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa find metodundan farklı olarak geriye -1 değerini döndürür
message9="hello World How are you"
message9=message9.index("World")
print(message9)

message10="hello World How are you"
#message10=message10.index("hsn")
print(message10)

#Ayrıca index ve find metodu için bir arama kapsamı belirtebiliriz.

#index("aranılacak ifade", "başlangıç indeksi","bitiş indeksi")

#Örnek
message10=message10.index('How',0,16)
print(message10)

#String Metot Uygulamaları

website = "http://www.sadikturan.com" 
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print('****************')
result=" Hello World "
sonuc1=result.strip() #bastaki ve sondaki bosluklari siler
sonuc2=result.lstrip()#sadece bastaki bosluklari siler
sonuc3=website.lstrip('h')#baştan itibaren 'h' karakteri silinir.
print(sonuc1)
print(sonuc2)
print(sonuc3)

#2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
sonuc4="www.sadikturan.com".strip('w.com')
print(sonuc4)

#3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc5='COURSE'.upper()
print(sonuc5)

#4- #3- 'COURSE' karakter dizisinin tüm karakterlerini buyuk harf yapın.
sonuc5='COURSE'.lower()
print(sonuc5)

#5-"python kursu: baştan sona python programlama Rehberiniz (40 saat)" dizisinin bas harflerini buyuk yapin
sonuc6="python kursu: baştan sona python programlama".title()
print(sonuc6)

#6- website' içinde kaç tane a karakteri vardır?
website=website.count('t')
print(website)

