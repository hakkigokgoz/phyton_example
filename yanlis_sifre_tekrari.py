# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:33:02 2019

@author: HAKKI
"""
#üç kere üst üste hatalı şifre girilirse şifre bloke oldu de
sifre="pass"
girilen_sifre=input("Şifrenizi Giriniz: ")
#başlangıç 0 değişim 1+ bitiş 3
i=0
if sifre!=girilen_sifre:
    while i<3:
        girilen_sifre=input("Şifrenizi Tekrar Giriniz: ")
        if sifre!=girilen_sifre:
            i=i+1
        print("Yanlış şifre.")
    print("Şifre bloke edildi!")  
else:
    print("Doğru şifre")
