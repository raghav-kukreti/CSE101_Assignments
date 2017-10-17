n = int(input())
check=0
for x in range(0,n):
	word = input()
	for x in range(0, len(word)-1) : 
		if (word[x] == word[x+1]):
			check=check+1
	if(check):
		print("YES")
	else:
		print("NO")
	check=0