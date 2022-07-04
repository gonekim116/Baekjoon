croa = ['c=','c-','dz=','d-','lj','nj','s=','z=']
s = input()
for c in croa:
  s = '.'.join(s.split(c))

print(len(s))