# -*- coding: utf-8 -*-
"""2024/04/15

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J5pkTMHuTENkPfCu7zlnJ2E1neyPVZMN
"""

#9*9 multiple table
#version 1
for x in range(1,10):
  for y in range(1,10):
    print('%d*%d=%2d'%(x,y,x*y))
  print()

n=eval(input())
total=0
for i in range(n,0,-1):
  total+=1.0/i
print('1/n+1/(n-1)+1/(n-2)+...+1=',total)

