# 装饰器
# -*- coding: utf-8 -*-
import time, functools
import datetime
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__,datetime.datetime.now()))
        return func(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')