import math

class Triangle:
    def get(self):
        # Read three sides and assign to self
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Check if the three sides can form a triangle
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # Valid triangle, do nothing
        else:
            print('Not a triangle')
            exit()  # Stop execution if not a valid triangle

    def area(self):
        # Calculate semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Heron's formula
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        # Calculate perimeter
        return self.a + self.b + self.c

# Create object
if __name__ == '__main__':
    t = Triangle()

    # Read inputs into object
    t.get()

    # Validate the triangle
    t.test()

    # Print results
    print('Area :', t.area())
    print('Perimeter :', t.peri())

import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator (non-zero): "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero.")
            self.den = int(input("Re-enter denominator: "))

    def __str__(self):
        return f"{self.num} / {self.den}"

    def add(self, a, b):
        self.num = a.num * b.den + b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def sub(self, a, b):
        self.num = a.num * b.den - b.num * a.den
        self.den = a.den * b.den
        self.simplify()

    def mul(self, a, b):
        self.num = a.num * b.num
        self.den = a.den * b.den
        self.simplify()

    def div(self, a, b):
        if b.num == 0:
            self.num = None  # invalid
            self.den = None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num != 0:
            g = math.gcd(self.num, self.den)
            self.num //= g
            self.den //= g

# --- Main Program ---
if __name__ == '__main__':
        a = Rat()
        b = Rat()
        c = Rat()
        d = Rat()
        e = Rat()
        f = Rat()

        print("\nEnter first rational number:")
        a.get()
        print("Enter second rational number:")
        b.get()

        c.add(a, b)
        d.sub(a, b)
        e.mul(a, b)
        f.div(a, b)

        print("\nSum        :", c)
        print("Difference :", d)
        print("Product    :", e)

        if f.num is not None:
            print("Division   :", f)
        else:
            print("Division is not permitted (division by zero).")

class   Student:
	def   get(self):
		self.rno = int(input('Enter a rollno: ')) #How  to  read  roll  number  into  object  self
		self.sname = input('Enter a Name: ') # How  to  read  student  name  into  object  self
		self.gender = input('Enter a Gender : ') #How  to  read  gender  into  object  self
		self.m = [] #How  to  read  marks  of  3  subjects
		for i in range(3):
			mark = int(input(f'Enter mark {i+1}: '))
			self.m.append(mark)
	def   compute(self):
		self.tot = sum(self.m) #How  to  calculate  total  marks
		self.avg = self.tot/3 #How  to  calculate  average  marks
		if  any(mark<40 for mark in self.m): #At  least  one  subject  is  below  40
				self.grade = 'Fail' #How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70: #average  is  above  >= 70%
				self.grade = 'Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.avg >= 60: #average  is  above  >= 60%:
				self.grade = 'First  class' #How  to  initilaize  grade  to  'First  class'
		elif  self.avg >= 50: #average  is  above  >= 50%:
				self.grade = 'Second class' #How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade = 'Third class' #How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' , self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f'Roll No : {self.rno}, Name : {self.sname}, Gender : {self.gender}, Total : {self.tot}, Average : {self.avg :.2f},Grade : {self.grade}' #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
if __name__ == '__main__':
    s = Student() #How  to  create  Student  class  object
    s.get() #How  to  read  inputs  into  object
    s.compute() #How  to  store  results  in  object
    s.disp() #How  to  print  object  with  disp()  method
    print(s) #How  to  print  object  with  _str_()  method

class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a')    