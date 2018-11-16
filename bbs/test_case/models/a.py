import os
a=os.path.dirname(__file__)
b=os.path.dirname(os.path.dirname(__file__))
b1=str(b)
b2=b.replace("/","\\")
b3=b.split('/test_case')[0]
b4=b.split('/')[1]
c=os.path.abspath(__file__)
d=os.path.realpath(__file__)
print(a)
print(b)
print(b1)
print(b2)
print(b3)
print(b4)
print(c)
print(d )