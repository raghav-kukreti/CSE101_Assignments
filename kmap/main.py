import string

class kmap:
	num_cells = 0
	def __init__(self, vars):
		self.vars = vars
		kmap.num_cells = 2**vars

def getVars(vars):
	v = []
	letters = list(string.ascii_lowercase)
	for i in range(vars):
		v.append(letters[i])
	return v

def find_diff(term_one, term_two):
	# Check if they differ by one bit
	flag = 0
	for i in range(len(term_one)):
		if(term_one[i]!=term_two[i]):
			flag+=1

	return (flag==1)

# Replaces complement terms with Dont Care
# As working w/ int, DC = 9
# 0110 and 0111 becomes 0119

def replace_complements(item_1, item_2):
	temp = ""
	for i in range(len(item_1)):
		if(item_1[i] != item_2[i]):
			temp = temp+"-"
		else:
			temp=temp+item_1[i]
	return temp

def in_vector(arr, item):
	ch=0
	for i in arr:
		if (item == i):
			return True
			ch+=1
			break

	if(ch==0):
		return False

def reduce_minterms(minterms):
	new_minterms = []
	max_val = len(minterms)
	checked = [None]*max_val

	for i in range(max_val):
		for j in range(i, max_val):
			if(find_diff(minterms[i], minterms[j])):
				checked[i]=1
				checked[j]=1
				if(not in_vector(new_minterms,replace_complements(minterms[i],minterms[j]))):
					new_minterms.append(replace_complements(minterms[i],minterms[j]))
	
	for i in range(max_val):
		if(checked[i]!=1 and not in_vector(new_minterms,minterms[i])):
			new_minterms.append(minterms[i])										

	return new_minterms

def get_value(a, var):
	temp = ""
	var_s = getVars(var)
	if (a == '----'):
		return 1
	for i in range(len(a)):
		if(a[i] != '-'):
			if(a[i] == '0'):
				temp = temp + var_s[i] + "\'"
			else:
				temp = temp + var_s[i]

	return temp

def vector_equal(a,b):
	if(len(a) != len(b)):
		return False
	a.sort()
	b.sort()

	for i in range(len(a)):
		if (a[i] != b[i]):
			return False
			break

	return True

def main():
	kmap_one = kmap(4)
	# space separated input
	num_vars = int(input('Enter number of variables: '))
	int_minterms = list(map(int, input().split(',')))
	dont_cares = list(map(int, input().split(',')))
	
	# print(int_minterms)
	minterms = []

	for i in int_minterms:
		minterms.append(("{0:b}".format(i)).zfill(num_vars))

	minterms.sort()
	print(minterms)
	minterms = reduce_minterms(minterms)
	print(minterms)
	
	while not vector_equal(minterms, reduce_minterms(minterms)):
		minterms = reduce_minterms(minterms)
		minterms.sort()		

	for i in range(len(minterms)):
		print(get_value(minterms[i], num_vars) + " + ")

if __name__ == '__main__':
	main()