
class Human(object):

	# def __init__(self):
	def setAge(self,age):
		self.age= age

	def getAge(self):
		return self.age;
	  

# class man(Human):
#     def getAge(self):
#         if self.age > 18:
#             return  getAge() +5
#         else:
#             return getAge()
   
# print(getAge)

h = Human()
h.setAge(60)
print(h.getAge())


   