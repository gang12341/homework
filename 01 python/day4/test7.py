# 序列化和反序列化
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
objs = json.loads(s)
print(s)
print(objs)