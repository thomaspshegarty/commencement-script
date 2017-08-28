import xlrd

def get_major(degree_name, s):
	if degree_name == 'MA':	
		student_major = s.grad_degrees1
		if student_major == "":
			student_major = s.grad_degrees2;
		elif student_major == 'Other':
			student_major = s.grad_degrees1_other;
		student_major = student_major.upper()
		return student_major;
			
	elif degree_name == 'BA':
		student_major = s.major_1
		if student_major == "":
			student_major = s.major_2;
		elif student_major == 'Other':
			student_major = s.major_2;
		student_major = student_major.upper()
		return student_major;

	elif degree_name == 'PhD':
		student_major = s.grad_degrees1
		if student_major == "":
			student_major = s.grad_degrees2;
		elif student_major == 'Other':
			student_major = s.grad_degrees1_other;
		student_major = student_major.upper()
		return student_major;

def get_minor(student):
	minor = student.minor_1
	if minor == 'Other' or minor == '':
		minor = student.minor_2
	return minor;

class Student(object):
	
	def __init__(self, worksheet, i):
		self.fields = list();
		self.first_name = worksheet.cell(i,0).value.encode('utf-8','ignore').upper()
		self.last_name = worksheet.cell(i,1).value.encode('utf-8','ignore').upper()
		self.pronunciation = worksheet.cell(i,2).value.encode('utf-8','ignore').upper()
		self.email_address = worksheet.cell(i,3).value.encode('utf-8','ignore')
		self.degree_level = worksheet.cell(i,4).value.encode('utf-8','ignore')
		self.major_1 = worksheet.cell(i,5).value.encode('utf-8','ignore')
		self.major_2 = worksheet.cell(i,6).value.encode('utf-8','ignore')
		self.minor_1 = worksheet.cell(i,7).value.encode('utf-8','ignore')
		self.minor_2 = worksheet.cell(i,8).value.encode('utf-8','ignore')
		self.special_programs = worksheet.cell(i,9).value.encode('utf-8','ignore')
		self.cluster_living = worksheet.cell(i,10).value.encode('utf-8','ignore')
		self.grad_degrees1 = worksheet.cell(i,11).value.encode('utf-8','ignore')
		self.grad_degrees1_other = worksheet.cell(i,12).value.encode('utf-8','ignore')
		self.grad_degrees2 = worksheet.cell(i,13).value.encode('utf-8','ignore')
		self.grad_degrees2_other = worksheet.cell(i,14).value.encode('utf-8','ignore')
		self.study_abroad = worksheet.cell(i,15).value.encode('utf-8','ignore')
		self.honors = worksheet.cell(i,16).value.encode('utf-8','ignore')
		self.extra = worksheet.cell(i,17).value.encode('utf-8','ignore')
		self.dissertation = worksheet.cell(i,18).value.encode('utf-8','ignore')
		self.post_grad = worksheet.cell(i,19).value.encode('utf-8','ignore')
		self.special_message = worksheet.cell(i,20).value.encode('utf-8','ignore');
	
class Major(object):

	def __init__(self):
		self.students = list();

	def set_name(self, name):
		self.major_name = name;

	def add_student(self, student):
		self.students.append(student);

class Degree(object):

	def __init__(self):
		self.students = list();

	def set_name(self, name):
		self.degree_name = name;

	def add_student(self, student):
		self.students.append(student);

	def order_majors(self):
		self.majors = list()
		for s in self.students:
			student_major = get_major(self.degree_name, s)
			major = Major()
			major_exists = False
			for m in self.majors:
				if student_major == m.major_name:
					major_exists = True
					major = m;
			if major_exists:
				major.add_student(s)
			else:
				major.set_name(student_major)
				major.add_student(s)
				self.majors.append(major);
