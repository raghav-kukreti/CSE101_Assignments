class student:
	"""Class of student"""
	def __init__(self, roll_no, f_name, l_name, prog, gpa):
		self.roll_no = roll_no
		self.f_name = f_name
		self.l_name = l_name
		self.prog = prog
		self.gpa = gpa
	def __str__(self):
		print(self.roll_no, self.f_name, self.l_name, self.prog, self.gpa)
		return ""
		
	def comes_before(self, other):
		other_yr = int(other.roll_no[0:4])
		other_prog = other.prog
		other_gpa = other.gpa
		self_yr = int(self.roll_no[0:4])
		self_prog = self.prog
		self_gpa = self.gpa

		if(self_yr < other_yr):
			return True
		else:
			if(self_prog < other_prog):
				return True
			else:
				if(self_gpa > other_gpa):
					return True

		# return true if self comes before true

def main():
	file = open('studentdata.txt', 'r')
	for i in file:
		print(i)
	pass

if __name__ == '__main__':
	main()
