Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
for i in range(1,10):
    if i==7:
        print(i)

        
7
a=10
for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9
a=10
for i in range(1,10):
    if i==7:
        break
    print(i)

    
1
2
3
4
5
6
a=10
for i in range(10):
    if i==8:
        continue
    print(i)

    
0
1
2
3
4
5
6
7
9
a=10
for i in range(10):
    if i==6:
        pass

    
a=10
while (a<5):
    a=a+1
    print(a)

    

while (a<5):
    a=a+1
    print(a)

    
a=0
while (a<10):
    a=a+1
    print(a)

    
1
2
3
4
5
6
7
8
9
10
a=5
while (a<50):
    a=a+5
    print(a)

    
10
15
20
25
30
35
40
45
50
a=-5
>>> while (a<5):
...     a=a+1
...     print(a)
... 
...     
-4
-3
-2
-1
0
1
2
3
4
5
>>> a=5
>>> while (a<50):
...     a=a+5
...     if a==20:
...         break
...     print(a)
... 
...     
10
15
>>> a=5
>>> while (a<50):
...     a=a+5
...     if a==30:
...         continue
...     print(a)
... 
...     
10
15
20
25
35
40
45
50
