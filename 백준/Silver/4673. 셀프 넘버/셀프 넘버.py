def d(n):
  s = n
  while n:
    s += n % 10
    n //= 10
  return s

li = [0]*10000

for num in range(1,10001):
  temp = d(num)
  while temp <= 10000:
    li[temp-1] += 1
    temp = d(temp)

for i,v in enumerate(li):
  if v == 0:
    print(i+1)
