L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x if isinstance(x, str)!=True else  x.lower()  for x in L1 ]

print(L2)