# -*- coding: utf-8 -*-
"""2024.04.01

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YxIR1mYXLg2SU_EzcyTjLd-wnRUxISkg
"""

import random
even = 0
odd = 0
for i in range(1,11):
  randNum = random.randint(1,100)
  print(randNum,end = ' ')
  if randNum %2 == 0:
    even += 1
  else:
    odd += 1
print('\neven = %d, odd = %d'%(even,odd))

import random
for i in range(1,11):
  randNum = random.randint(1,100)
  print('%4d'%(randNum),end = ' ')