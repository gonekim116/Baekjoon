count = 0
target = int(input())
num = 666
goal = 0
while True:
	if '666' in str(num):
		count += 1
		if count == target:
			goal = num
			break
	num += 1
print(goal)