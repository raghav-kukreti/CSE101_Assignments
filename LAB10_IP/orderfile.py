from app import student
# from app import comes_before

def readrecords():
	file = open('studentdata.txt', 'r')
	student_arr = []
	for i in file:
	# 2013196 Catelyn Stark M.Tech-CSE 6.36
		roll_no = i[0:7]
		f_name = i[7: i.find(' ', 8)]
		end_index = i.find(' ', 8)+1
		l_name = i[end_index:i.find(' ', end_index)]
		end_index_2 = i.find(' ', end_index)+1
		branch = i[end_index_2: i.find(' ', end_index_2)]
		end_index_3 = i.find(' ', end_index_2) + 1
		gpa = float(i[end_index_3: i.find(' ', end_index_3)])
		temp = student(roll_no, f_name, l_name, branch, gpa)
		student_arr.append(temp)

	return student_arr

def orderrecords(array):
	pass

def main():
	array = readrecords()
	temp = student(None,None,None,None,None)
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if(array[j+1].comes_before(array[j])):
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

	for i in array:
		print(i.roll_no, i.f_name, i.l_name, i.prog, i.gpa)
if __name__ == '__main__':
	main()