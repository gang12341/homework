# reduec3
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2float(s):
    dot=s.split('.')
    s1=int(dot[0])
    s2=dot[1]
    return s1+reduce(
        lambda x,y:x*10+y,map(char2num,s2)
    )/(10**len(s2))





print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')