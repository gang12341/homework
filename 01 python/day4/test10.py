# base64

import base64

def safe_base64_decode(s):
    n = len(s)
    if  n%4==0:
        return base64.b64decode(s)
    else:
        news=s
        while n%4!=0:
            n+=1
            news = news+'='
        return base64.b64decode(news)
    

# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')