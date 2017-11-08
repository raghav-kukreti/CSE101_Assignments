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

		# Sort according to year
		# Sort in year according to lexicographic
		# sort in year, stream by GPA

		if(self_yr < other_yr):
			return True
		elif(self_yr == other_yr):
			if(self_prog < other_prog):
				return True
			elif(self_prog == other_prog):
				if(self_gpa > other_gpa):
					return True