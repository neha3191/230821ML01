Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 ** 9
1953125
>>> 3//2
1
>>> 7//2
3
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20; a+= 30; a%=3;print(a)
2
>>> true * false
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    true * false
NameError: name 'true' is not defined
>>> True * False
0
>>> True &False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18 == 3)) and (9>3)
False
>>> True is False
False
>>> True in 'False'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    True in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> s1 = "nice to have it"
>>> s2 = "here"
>>> print(s1 + s2)
nice to have ithere
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a [3] [1] [2] [0]
'hello'
>>> a.insert(0 , s1)
>>> a
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.append(s2)
>>> a
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> 