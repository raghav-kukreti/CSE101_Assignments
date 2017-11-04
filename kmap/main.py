class kmap:
	num_cells = 0
	def __init__(self, vars):
		self.vars = vars
		kmap.num_cells = 2**vars

def find_diff(term_one, term_two):
	# Check if they differ by one bit
	str_one = str(term_one)
	str_two = str(term_two)
	flag = 0
	for i in range(len(str_one)):
		if(str_one[i]!=str_two[i]):
			flag+=1

	return (flag==1)

def check_if_exists()
def main():
	kmap_one = kmap(4)
	# space separated input
	num_vars = int(input('Enter number of variables: '))
	minterms = list(map(int, input().split(',')))
	dont_cares = list(map(int, input().split(',')))
	
	print(minterms)
	binary_minterms = []

	for i in minterms:
		binary_minterms.append(("{0:b}".format(i)).zfill(num_vars))

	print(binary_minterms)
	for i in range(len(binary_minterms)-1):
		print(find_diff(binary_minterms[i], binary_minterms[i+1]))


if __name__ == '__main__':
	main()