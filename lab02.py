t = int(input())
for x in range(t):
	num_pins = int(input())
	pin_codes = input()
	code = pin_codes.split(" ")
	for x in range(num_pins):
		if (code[x] == '110020' or code[x] == '110021'):
			code[x] = 'Okhla'
		elif (code[x] == '110055' or code[x] == '110056'):
			code[x] = 'Rohini'
		elif(code[x] == '110075'):
			code[x] = 'Dwarka'
		else:
			code[x] = 'Others'	

	for x in range(num_pins):
		print(code[x], end=' ', sep='')