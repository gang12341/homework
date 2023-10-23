# 访问限制

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self._gender = gender
    def get_gender(self):
        return self._gender
    def set_gender(self,newgender):
        self._gender = newgender



# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')