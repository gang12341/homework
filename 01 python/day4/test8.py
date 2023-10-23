# 正则
import re
def is_valid_email(addr):
    res = re.match(r'((\w+\.)*(\w+)+)@(\w+)\.com',addr)
    return res
def name_of_email(addr):
    res = re.match(r'<?([\w\s]+)>?(.*)@(\w+)\.(\w+)',addr)
    print(res)
    return res.group(1)
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')