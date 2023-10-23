# @property
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,val):
        self._width = val

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,val):
        self._height = val

    @property
    def resolution(self):
        return self._width*self._height
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')