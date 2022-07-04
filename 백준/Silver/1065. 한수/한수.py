def check(n):
  if n <= 99:
    return True
  else:
    h = n // 100
    t = (n % 100) // 10
    o = n % 10
    d1 = h-t
    d2 = t-o
    if d1==d2:
      return True
    else: 
      return False

n = int(input())
count = 0
for i in range(1,n+1):
  if check(i):
    count += 1

print(count)