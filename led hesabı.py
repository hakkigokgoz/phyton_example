# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:11:56 2019

@author: HAKKI
"""

#led hesabı
print("***********************************************")
gerilim=int(input("Kaynak Gerilimini giriniz(V): "))
renk=input("Ledin rengini seçiniz:\n1-Kırmızı\n2-Sarı\n3-Yeşil\n4-Mavi\n")
if renk== "1".strip():#kırmızı
    renk=1.7
    akim=0.01
elif renk== "2":#sarı
    renk=2.1
    akim=0.01
elif renk=="3":#yeşil
    renk=2.2
    akim=0.01
elif renk=="4":#mavi
    renk=3.2
    akim=0.02
else :
    print("Geçersiz led rengi!")

led=int(input("Seri led sayisini giriniz: "))
if (gerilim<(led*renk)):
    print("Kaynak gerilimi led sayısı için yetersiz!")
else:
    direnchesapla=int((gerilim-(renk*led))/akim)
    if direnchesapla>1000:
        print((direnchesapla*0.001), "kΩ")
    else:
        print(direnchesapla, "Ω")


        

    