"""
	Name    : Raghav Dev Kukreti
	Group   : B1
	Roll No :	2017082

	Python code to calculate rank of a matrix.
"""
# Formulate the matrix of dimension MxN
def create_matrix(m, n):
	matrix = []
	for i in range(0,m):
	    matrix.append([])
	    for j in range(0,n):
	        matrix[i].append(int(input('Enter element at (' + str(i) + ', ' + str(j) + '): ')))
	return matrix

# Function to swap rows
def swap_rows(a, row1, row2):
	# swap rows
	for i in range(len(a)):
		temp=a[row1][i]
		a[row1][i]=a[row2][i]
		a[row2][i]=temp
	return(a)

# Function to carry out row transformation
def row_transform(a, x, row1, row2):
	for i in range(len(a)):
		a[row2][i] = a[row2][i] + x*a[row1][i]
	return(a)

# Finds rank through RR method
def find_rank(a):
	col=len(a[1])
	row=len(a)
	if(row < col):
		rank = row
	else:
		rank = col

	if (row>col):
		temp_arr=[]
		for m in range(col):
			row_arr=[]
			for n in range(row):
				row_arr.append(a[n][m])
			temp_arr.append(row_arr)
		a=temp_arr
		col,row=row,col
		# https://1movies.online/movie/pearl-harbor/6452-watch-online-free.html

	for i in range(rank):
		if a[i][i]!=0:
			for j in range(i+1,row):
				a = row_transform(a,-(a[j][i]//a[i][i]),i,j)
		else:
			ctr=1
			for k in range(i+1,row):
				if a[k][i]!=0:
					a=swap_rows(a,i,k)
					ctr=0
					break
				else:
					pass
			if(ctr==1):
				for m in range(row):
					a[m][i]=a[m][rank-1]
					a[m][rank-1]=a[i][m]
			row-=1
		ch=0
		for i in a:
			if i==[0]*col:
				ch+=1

	return (rank-ch)

if __name__ == '__main__':
	# a = create_matrix(1, 3)
	m = int(input('Enter number of rows: '))
	n = int(input('Enter number of cols: '))
	a=create_matrix(m,n)
	# swap_rows(a, 0, 1)
	# row_transform(a, 1, 0, 1)
	print(a)
	print(find_rank(a))
	print(a)

	# for i in range(len(a)):
		# print(a[i][0])
