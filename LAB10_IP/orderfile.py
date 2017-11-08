from app import student
# from app import comes_before

def readrecords():
	file = open('studentdata.txt', 'r')
	student_arr = []
	for i in file:
	# 2013196 Catelyn Stark M.Tech-CSE 6.36
		roll_no = int(i[0:7])
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
	for i in range(len(array)):
		if(array[i].comes_before(array[i+1])):
			print(array[i].roll_no, array[i+1].roll_no)
if __name__ == '__main__':
	main()