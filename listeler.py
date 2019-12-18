# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:58:22 2019

@author: HAKKI
"""
# 1 20 -3 1 4 5 4




n=input("Bir dizi sayı girin: ")
#stringi listeye çevir
liste=n.split()

#listeyi inte çevir
for idx in range(len(liste)):
    liste[idx]=int(liste[idx])

#max ve min bul
print("Maximum sayı=", max(liste))
print("Minumum sayı=", min(liste))

#tekrar eden elemanlerı bul
yeni_liste=[]
tekrar_liste=[]
for ayni_sayi  in liste:
    if  ayni_sayi not in yeni_liste:
       yeni_liste.append(ayni_sayi)
    else:
       tekrar_liste.append(ayni_sayi)
        
print("Yeni liste= ", yeni_liste)
print("Tekrar eden sayılar= ", tekrar_liste)

#sayıları tek ve çift şeklinde ayır
cift_liste=[]
tek_liste=[]
for sayi in yeni_liste:
    if sayi%2==0:
        cift_liste.append(sayi)
    else:
        tek_liste.append(sayi)
print("Çift sayılar= ", cift_liste)
print("Tek sayılar= ", tek_liste)






        





