n,limit = list(map(int,input().split(' ')))
li = list(map(int,input().split(' ')))

max = 0
for i in range(len(li)-2):
	for j in range(i+1,len(li)-1):
		for k in range(j+1,len(li)):
			sum = li[i] + li[j] + li[k]
			if sum > limit: continue
			else:
				if sum > max:	
					max = sum
print(max)