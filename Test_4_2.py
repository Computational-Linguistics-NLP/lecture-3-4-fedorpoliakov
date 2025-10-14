Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> year = int(input())
1989
>>> if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
...     print('Високосный')
... else:
...     print('Обычный')
... 
...     
Обычный
