# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

L=[x for x in os.listdir('.') if os.path.isfile(x) and
   x.find('5')!=-1 ]

for x in L:
    print(os.path.abspath(x))