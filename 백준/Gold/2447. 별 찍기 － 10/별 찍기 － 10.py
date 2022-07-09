def starlines(n):
	if n==1:
		return ['*']

	stars = starlines(n//3)
	list = []
	for s in stars:
		list.append(s*3)
	for s in stars:
		list.append(s + ' '*(n//3) + s)
	for s in stars:
		list.append(s*3)
	return list

print('\n'.join(starlines(int(input()))))