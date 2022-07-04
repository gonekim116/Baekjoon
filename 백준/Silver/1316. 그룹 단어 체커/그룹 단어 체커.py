N = int(input())
sum = 0
for i in range(N):
  s = input()
  num = len(set(list(s)))
  temp = s[0]
  count = 1
  for c in list(s):
    if c != temp:
      count += 1
    temp = c
  if num == count:
    sum += 1

print(sum)