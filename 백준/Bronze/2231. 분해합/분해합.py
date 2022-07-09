n=int(input())
for i in range(1,n):
	min = i
	_ = i
	while _ > 0:
		i += _%10
		_ //= 10
	if i == n: print(min); quit()
print(0)