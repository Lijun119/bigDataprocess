# -*- coding: utf-8 -*-
"""2024.04.01-2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lpgG87g63z1rPta4NkBajxdF26DlyZ4S
"""

#Version 1
import random
times3 = 0
times5 = 0
times7 = 0
others = 0
for i in range(1,101):
  flag = False
  randNum = random.randint(1,100)
  print(randNum, end = ' ')
  if randNum % 3 == 0:
    times3 += 1
    flag = True
  if randNum % 5 == 0:
    times5 += 1
    flag = True
  if randNum % 7 == 0:
    times7 +=1
    flag = True
  if flag == False:
    others += 1
print('\ntimes3 = %d, times5 =%d, times7 = %d'%(times3, times5, times7))
print('other = %d'%(others))