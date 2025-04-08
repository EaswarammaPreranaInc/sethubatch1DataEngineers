class Student:
    def get(self):
        self.roll_number = input("Enter Roll Number: ")
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender (M/F): ")
        self.marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter marks for Subject {i}: "))
            self.marks.append(mark)

    def compute(self):
        self.total = sum(self.marks)
        self.average = self.total / 3

        if any(mark < 40 for mark in self.marks):
            self.grade = 'Fail'
        elif self.average >= 70:
            self.grade = 'Distinction'
        elif self.average >= 60:
            self.grade = 'First class'
        elif self.average >= 50:
            self.grade = 'Second class'
        else:
            self.grade = 'Third class'

    def disp(self):
        print('Roll Number  :', self.roll_number)
        print('Student Name :', self.name)
        print('Gender       :', self.gender)
        print('Total Marks  :', self.total)
        print('Average      :', self.average)
        print('Grade        :', self.grade)

    def __str__(self):  # Note: It's double underscores on both sides: __str__
        return (f"Roll Number: {self.roll_number}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}")

# Main Program

# Creating a Student class object
s1 = Student()

# Reading inputs into object
s1.get()

# Storing results in object
s1.compute()

# Printing object using disp() method
s1.disp()

# Printing object using __str__() method
print(s1)
```

### Explanation Recap:
- `self.roll_number`, `self.name`, etc. are instance variables.
- `input()` reads user input.
- `sum()` calculates total, `any()` checks for marks below 40.
- `__str__()` gives a nice string format when using `print(object)`.
-----------------------------------------------------------------------------------------------------------
  Here's the complete program for rational number operations (add, subtract, multiply, divide) using a class in Python, with all your placeholder comments filled in:

```python
import math

class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        self.test()

    def test(self):
        while self.den == 0:
            print("Denominator cannot be zero. Please re-enter.")
            self.den = int(input("Enter denominator: "))

    def __str__(self):  # Double underscores for __str__
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
            self.num = None  # Flag for division not permitted
            self.den = None
        else:
            self.num = a.num * b.den
            self.den = a.den * b.num
            self.simplify()

    def simplify(self):
        if self.num == 0:
            self.den = 1  # 0/n = 0/1 for standard form
            return
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

# --- Main Program ---

# Create 6 objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Read rational numbers
print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Perform operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
f.div(a, b)

# Print results
print("Sum         :", c)
print("Difference  :", d)
print("Product     :", e)

# Division check
if f.num is not None:
    print("Division    :", f)
else:
    print("Division is not permitted")
```

---

### Example Run:

```
Enter first rational number:
Enter numerator: 2
Enter denominator: 3
Enter second rational number:
Enter numerator: 5
Enter denominator: 9
Sum         : 11 / 9
Difference  : 1 / 9
Product     : 10 / 27
Division    : 6 / 5
```
-----------------------------------------------------------------------------------------
Great homework, Sowmya! You're working with **polymorphism and `hasattr()`** — love it! Let's walk through the code together and explain everything with **expected outputs and detailed comments**.

---

### ✅ **Program: Check if object has `talk()` or `bark()` method using `hasattr()`**
```python
class Cat:
    def talk(self):
        print('Meow Meow Meow ....')

class Dog:
    def bark(self):
        print('Bhow Bhow Bhow ....')

class Goat:
    def talk(self):
        print('Mehar Mehar Mehar ....')
# end of the class

# Create a list with one object of each class
a = [Cat(), Dog(), Goat()]

# Loop through each object in the list
for x in a:
    # If the object has a method called 'talk', call it
    if hasattr(x, 'talk'):
        x.talk()
    else:
        x.bark()
```

---

### 🔍 **Line-by-line Explanation with Output**

1. **`x = Cat()`**  
   - `Cat` has a method `talk()`
   - So: `x.talk()` is called  
   ✅ Output: `Meow Meow Meow ....`

2. **`x = Dog()`**  
   - `Dog` **does NOT** have `talk()`  
   - So: `x.bark()` is called  
   ✅ Output: `Bhow Bhow Bhow ....`

3. **`x = Goat()`**  
   - `Goat` has a method `talk()`  
   - So: `x.talk()` is called  
   ✅ Output: `Mehar Mehar Mehar ....`

---

### 🧾 **Final Output**
```
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar Mehar Mehar ....
```

---

### 💡 Key Concept:
- `hasattr(x, 'talk')` helps check **at runtime** if the method exists.
- This is a classic example of **duck typing** in Python:  
  _"If it talks like a duck, it's a duck!"_

---
---------------------------------------------------------------------------------------------------
# Define an empty class named c1
class c1:
    pass
# End of the class

# Create an object 'a' of class c1
a = c1()

# Manually add an attribute 'x' to object 'a'
a.x = 10

# Ask user to enter a variable name to be added to the object
# 📝 Assume input: 'y'
varname = input('Enter variable name to be added to object: ')  # 'y'

# Ask user to enter value of that variable
# 📝 Assume input: 20
value = eval(input('Enter value of the variable: '))  # 20

# Dynamically add attribute to object using setattr()
setattr(a, varname, value)  # This creates a.y = 20

# Print the object's attribute dictionary using __dict__
print(a.__dict__)  # {'x': 10, 'y': 20}

# Print the value of existing attribute x
print(a.x)  # 10

# Start a loop to fetch variable values dynamically using getattr()
while True:
    try:
        # Ask user for variable name to retrieve
        varname = input('Enter variable name whose value is to be retrieved: ')
        # 📝 Assume input order: 'x', then 'y', then 'z'

        # Print value of that attribute using getattr()
        print(getattr(a, varname))

    except:
        # If the attribute does not exist, handle exception
        print(f'Invalid variable name: {varname}')
        break
🧾 Expected Interaction (Sample Run)
pgsql
Copy
Edit
Enter variable name to be added to object: y
Enter value of the variable: 20
{'x': 10, 'y': 20}
10
Enter variable name whose value is to be retrieved: x
10
Enter variable name whose value is to be retrieved: y
20
Enter variable name whose value is to be retrieved: z
Invalid variable name: z
💡 Summary of Key Concepts
✅ setattr(object, name, value) → adds/updates an attribute dynamically

✅ getattr(object, name) → fetches attribute by name

✅ __dict__ → returns a dictionary of all attributes of the object

❗ eval() → evaluates a string as Python code (be cautious when using it)

🚫 getattr() raises AttributeError if the attribute doesn’t exist, so we use try/except to catch it

--------------------------------------------------------------------------------------------------------------------
Great question, Sowmya! You're exploring how to dynamically set attributes on an object from a dictionary — and this is super useful in many real-world Python applications (like converting JSON to objects).

Here's the **completed program with comments**, using `setattr()` to convert the dictionary into an object, and `getattr()` to print the values.

---

### ✅ **Program: Convert Dictionary to Class Object using `setattr()` and `getattr()`**
```python
# Define an empty class Emp
class Emp:
    pass
# End of the class

# Define a dictionary with employee details
emp_dict = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 10000.0}

# Create an object 'e' of class Emp
e = Emp()

# Convert dictionary to object using setattr() in a loop
for key in emp_dict:
    setattr(e, key, emp_dict[key])  # e.Empno = 25, e.Ename = 'Rama Rao', e.Sal = 10000.0

# Print object 'e' contents using getattr()
print("Employee details from object:")
for key in emp_dict:
    print(f'{key} : {getattr(e, key)}')  # dynamically get and print attribute values
```

---

### 🧾 **Expected Output**
```
Employee details from object:
Empno : 25
Ename : Rama Rao
Sal : 10000.0
```

---

### 🧠 Key Points:
- `setattr(obj, name, value)` adds an attribute `name` to `obj` with value `value`.
- `getattr(obj, name)` retrieves the value of attribute `name` from `obj`.
- This pattern is useful for converting structured data (like dictionaries, or JSON) into objects.
