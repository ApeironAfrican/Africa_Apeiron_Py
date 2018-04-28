
class Person:
	def __init__(self,name,job=None,pay=0):
		self.name = name
		self.job = job
		self.pay = pay

	def firstname(self):
		return self.name.split()[0]

	def lastname(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent))

class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self,name,'mgr',pay)

	def giveRaise(self, percent, bonus = 0.10):
		Person.giveRaise(self,percent + bonus)

if __name__ == '__main__':
	chris = Manager('Chris Jones', 50000)
	chris.giveRaise(0.20)
	print(chris)

#lists
courses = ["Maths","Biology","Physics","Chemistry"]
courses.append("Geography")
#reversed_list = courses.sort()
print(courses)
#print(reversed_list)

def prefix(s):
	n = len(s)
	A = [0] * n
	for j in range(n):
		total = 0
		for i in range(j + 1):
		total += s[i]
		A[j] = total/(j + 1)

	return A

prefix(5)
prefix(10)
prefix(15)
prefix(20)