# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:58:04 2019

@author: HAKKI
"""
#İstanbul8 -->itnul4 0 2 4 6 8
#Başlangıç kelime, bitiş itbl değişim çift sayılar
kelime= input("Bir kelime girin: ")
s = len(kelime)

if s > 0 : 
  i = 0
  while i < s:
    print(kelime[i], end="")
    i = i+2
        