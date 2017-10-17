
a = input("Enter a string: ")
back = ''
for i in a:
	if (back != i):
		back = i
		print(back, end='')