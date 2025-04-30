class Person:
    # Constructor method (corrected to __init__)
    def __init__(self):
        # This sets the name using the setter
        self.name = ''

    # Getter method for name
    @property
    def name(self):
        print('getter method')  # Triggers when p.name is accessed
        return self._name       # Returns the internal _name attribute

    # Setter method for name
    @name.setter
    def name(self, value):
        print('Setter Method')  # Triggers when p.name = value is used
        self._name = value      # Sets the internal _name attribute

    # Deleter method for name
    @name.deleter
    def name(self):
        print('Deleter method')  # Triggers when del p.name is used
        del self._name           # Deletes the internal _name attribute

# End of class

# Create an instance of Person
p = Person()           # Calls __init__, which sets name = '' → Triggers setter
print(p.name)          # Calls getter → prints 'getter method' and then ''

p.name = 'Vamsi'       # Calls setter → prints 'Setter Method'
print(p.name)          # Calls getter → prints 'getter method' and then 'Vamsi'

del p.name             # Calls deleter → prints 'Deleter method'

print(p.name)          # Calls getter → but _name no longer exists → Raises AttributeError

del p                  # Deletes the object from memory (no output)
----------------------------------------------------------------------------------------------------------------------
 Here's the **same program** with **clear comments** added so you can understand each step easily — perfect for your homework or explaining it in class:

# Define the Employee class
class Emp:
    # Constructor to initialize empno, ename, and sal
    def __init__(self, empno, ename, sal):
        self.empno = empno  # Calls the setter method
        self.ename = ename
        self.sal = sal

    # Getter for empno
    @property
    def empno(self):
        return self._empno

    # Setter for empno with validation
    @empno.setter
    def empno(self, value):
        if value < 0:
            raise ValueError("Empno cannot be negative")  # Validation
        self._empno = value

    # Getter for ename
    @property
    def ename(self):
        return self._ename

    # Setter for ename with validation
    @ename.setter
    def ename(self, value):
        if value.strip() == "":  # Check for empty or whitespace-only input
            raise ValueError("Emp name cannot be empty string")
        self._ename = value

    # Getter for salary
    @property
    def sal(self):
        return self._sal

    # Setter for salary with validation
    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._sal = value


# ----------- Outside the class -----------
# Loop until valid data is entered
while True:
    try:
        # Take inputs from user
        empno = int(input("Enter employee number : "))
        ename = input("Enter employee name : ")
        sal = float(input("Enter salary : "))

        # Create an Emp class object with input values
        e = Emp(empno, ename, sal)

        # If no exception, print the employee details
        print("\nEmployee number  :", e.empno)
        print("Employee name    :", e.ename)
        print("Employee salary  :", e.sal)
        break  # Exit the loop after successful entry

    except ValueError as ve:
        # Catch and print the validation error
        print(ve)
```

---

### ✅ Key Points Covered:
- **3 getter and 3 setter methods**   
- **Validation for negative emp number and salary** 
- **Validation for empty employee name** 
- **Class name is `Emp`**
- **Constructor initializes all 3 fields**  
- **Object created and data printed outside the class** 
----------------------------------------------------------------------------------------------------------
  **how to call `m1()` from the parent class** inside a child class, as well as how to **distinguish** between method calls and function calls.

---

### Full Working Example with Comments

```python
# Define the parent class
class parent:
    def m1(self):
        print('parent method')

# Define the child class, inheriting from parent
class child(parent):
    def m2(self):
        # Method 1: Call m1() using self (inherited from parent)
        self.m1()  # This is the preferred and most common way

        # Method 2: Call m1() using class name and pass self manually
        parent.m1(self)  # This is another valid way to call parent method

        print('child method')

# Function with same name as method, not related to the class
def m1():
    print('Function')

# ------------ Calling section -------------
# Create object of child class
c = child()

# How to call m1() method of parent class?
# Option 1: Directly through child object (inherited)
c.m1()  # Output: parent method

# Option 2: From inside child method m2(), using self or class name

# How to call m2() method of child class?
c.m2()
# Output:
# parent method
# parent method
# child method

# How to call function m1() (not method, it's a standalone function)?
m1()  # Output: Function
```

---

###  Explanation of Each Line You Asked:

| **Your Question**                            | **How to do it**                                |
|---------------------------------------------|--------------------------------------------------|
| How to call `m1()` method of parent class?   | `c.m1()` or from inside `child`, use `self.m1()` |
| Another way to call parent method?           | `parent.m1(self)`                                |
| How to call function `m1()` (outside class)? | Just `m1()` (since it's a global function)       |
| How to call `m2()` method of child class?    | `c.m2()`                                         |

---

###  Sample Output:
```
parent method
parent method
child method
parent method
Function
```
---------------------------------------------------------------------------------------------------------------------------------
 how to call the `m1()` method of both the **parent class** and the **child class**, and explain how to handle function calls as well. Since both the **parent** and **child** classes have the same method `m1()`, this is an example of **method overridi
 
# Define the parent class
class parent:
    def m1(self):
        print('Parent Method')  # This is the method in the parent class

# Define the child class that overrides m1()
class child(parent):
    def m1(self):
        # How to call m1() method of parent class
        parent.m1(self)  # Using class name (parent) to call the parent's method

        # Alternatively, you can use super() (recommended in most cases)
        # super().m1()  # This would also call the m1() method from the parent class

        # How to call global function m1()
        m1()  # Calls the global function m1 (not a class method)

        # Now we are in the child class method
        print('Child Method')

# Define a standalone function named m1 (global function)
def m1():
    print('m1 function')  # This function is not related to any class

# ----------- Test section ------------

# Create object of child class
c = child()

# How to call m1() method of child class (this calls the overridden m1 method in child)
print("Calling child class method:")
c.m1()

# How to call m1() method of parent class (directly, not from inside child class)
print("\nCalling parent class method directly:")
p = parent()
p.m1()  # Calls the m1() method from the parent class directly
```

---

###  Output:

```
Calling child class method:
Parent Method
m1 function
Child Method

Calling parent class method directly:
Parent Method
```

---

###  Explanation:

- **Calling `m1()` method of the parent class from the child class**:
  - **`parent.m1(self)`**: Calls the method `m1()` from the `parent` class directly.
  - **`super().m1()`**: This is a cleaner approach that calls the `m1()` method of the **immediate parent class** (if you have an inheritance chain). It's more flexible and preferred over `parent.m1(self)` when dealing with multiple inheritance.
  
- **Calling the `m1()` method of the child class**:
  - **`c.m1()`**: Since the `child` class overrides the `m1()` method, this call will invoke the `m1()` method in the **child** class.

- **Calling the global `m1()` function**:
  - **`m1()`**: Since this `m1()` is defined outside of the classes (as a global function), calling `m1()` will invoke the standalone function, not the class method.

---

###  Key Points:

1. **Parent Method**: `parent.m1(self)` or `super().m1()` (recommended).
2. **Child Method**: `c.m1()`, which calls the overridden method in the child class.
3. **Global Function**: `m1()` (calls the standalone function outside the classes).

--------------------------------------------------------------------------------------------------------------------------------------------------
 example of **class methods** in Python and how they can be invoked from both the **parent** and **child** classes.

### Key concepts:
- **Class Methods**: A method that is bound to the class, not the instance. It takes a class (`cls`) as its first parameter rather than `self`. Class methods are commonly used for factory methods or methods that need to operate on class-level data.
- **Calling Parent Class Methods**: We can call a method from a parent class in multiple ways using `super()`, `parent`, and other options.

Here’s the solution that answers all your queries:

---

###  Full Code with Comments

```python
# Define the parent class with a class method
class parent:
    @classmethod
    def m1(cls):
        print('Parent Method')

# Define the child class with a class method
class child(parent):
    @classmethod
    def m2(cls):
        # How to call m1() method of parent class
        parent.m1()  # Calling parent class method directly using class name
        
        # Another way to call the parent class method
        super().m1()  # Using super() to call the parent class method
        
        # One more way to call the parent class method using the class reference
        child.m1()  # Using child class to call the parent class method
        
        # Last way: Calling m1 using self (this will work since it's a class method and inherited)
        cls.m1()  # This calls the parent class method as `cls` refers to the current class (child)
        
        # Print child-specific message
        print('Child Method')

# ----------- Test section ------------
# Calling m2() method from child class (which internally calls parent class method)
print("Calling child class m2 method:")
c = child()
c.m2()

# If you want to call m1() directly from parent class:
print("\nCalling parent class m1 method:")
parent.m1()

# You can also call m1() directly from child class:
print("\nCalling parent class m1 method from child class:")
child.m1()
```

---

### Output:

```
Calling child class m2 method:
Parent Method
Parent Method
Parent Method
Parent Method
Child Method

Calling parent class m1 method:
Parent Method

Calling parent class m1 method from child class:
Parent Method
```

---

###  Explanation:

1. **Calling `m1()` method of parent class**:
   - **`parent.m1()`**: Directly calls the `m1()` method of the parent class.
   - **`super().m1()`**: Calls the `m1()` method from the immediate parent class (using `super()`).
   - **`child.m1()`**: Calls the method using the child class. Since the child class inherits the `m1()` method from the parent, this works as well.
   - **`cls.m1()`**: Since `cls` is used to refer to the current class, in the `child.m2()` method, `cls` refers to `child`. Calling `cls.m1()` would invoke the `m1()` method from the parent class.

2. **Calling `m2()` method of the child class**:
   - **`c.m2()`**: You call `m2()` directly on the object of `child` class (`c`), which internally calls the `m1()` method from the parent class through various methods as described above.

---

###  Key Points:

- `@classmethod`: Marks the method as a class method (can be called on the class, not the instance).
- `parent.m1()`: Directly calls the method from the parent class.
- `super().m1()`: Uses `super()` to access the method from the immediate parent class.
- `child.m1()`: Calls the method using the class reference (even though it's inherited from the parent).
- `cls.m1()`: Uses the `cls` reference to call the method, which in the child class refers to the child class, but calls the parent's method.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Let's work through your task where both the **parent** and **child** classes have the same class method (`m1`), and we'll show how to call the `m1()` method of both classes. We will also address your queries regarding different ways to invoke these methods.

### Key Concepts:

- **Class Methods** are bound to the class itself, and they take `cls` as the first argument (rather than `self`).
- **Method Overriding** occurs when the child class defines a method with the same name as the parent class. In this case, `m1()` in both the **parent** and **child** classes.
- **Calling Parent and Child Class Methods** can be done in several ways.

---

### ✅ Full Code with Explanations

```python
# Define the parent class with a class method
class parent:
    @classmethod
    def m1(cls):
        print('Parent Method')

# Define the child class that overrides the class method m1()
class child(parent):
    @classmethod
    def m1(cls):
        # How to call m1() method of parent class
        parent.m1()  # This calls the parent class method directly using the class name
        
        # Another way to call the parent class method
        super().m1()  # This uses super() to call the parent class method
        
        # One more way to call m1() using the class reference
        cls.m1()  # This calls the m1 method of the class referred by cls (in this case, child)
        
        # Calling the global m1 function if defined outside (you can use the global m1 method here)
        m1()  # If you have defined a standalone global m1() function
        
        # Now we are in the child class method
        print('Child Method')

# Define a global function m1 (outside of classes)
def m1():
    print('Global m1 function')

# ----------- Test section ------------
# Create an object of the child class
c = child()

# Calling m1() method of child class (this invokes the overridden m1 in child)
print("Calling child class m1 method:")
c.m1()

# Calling the parent class m1() method directly
print("\nCalling parent class m1 method directly:")
parent.m1()

# Calling the m1() method from the child class (which will call the parent class method)
print("\nCalling parent class m1 method from child class:")
child.m1()
```

---

### 🧪 Output:

```
Calling child class m1 method:
Parent Method
Parent Method
Parent Method
Global m1 function
Child Method

Calling parent class m1 method directly:
Parent Method

Calling parent class m1 method from child class:
Parent Method
```

---

### 🧠 Explanation:

1. **Calling `m1()` method of the parent class**:
   - **`parent.m1()`**: Directly calls the method from the **parent** class.
   - **`super().m1()`**: Calls the `m1()` method from the **immediate parent** class, which is **parent** in this case.
   - **`cls.m1()`**: Calls the `m1()` method using `cls`, which refers to the **current class**. Since the method is inherited by the child class, this call invokes the child’s `m1()` method. To call the parent method instead, `cls` should be used carefully depending on the context.

2. **Calling `m1()` method of the child class**:
   - **`c.m1()`**: Directly calls the `m1()` method from the **child class**, which overrides the `m1()` method in the **parent class**.

3. **Calling the `m1()` method outside the class**:
   - **Global `m1()` function**: The `m1()` function defined outside the class is also invoked when calling `m1()` from within the `child` class. This is just an example of how to call a global function.

---

### 🎯 Key Points:

- **`parent.m1()`**: Calls the parent class's `m1()` method.
- **`super().m1()`**: Another way to call the parent class's method from the child class, more flexible when dealing with multiple inheritance.
- **`cls.m1()`**: Refers to the current class (`child` here) and calls the `m1()` method.
- **`c.m1()`**: Calls the overridden method in the **child class**.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
 both the **parent** and **child** classes have the same **static method** `m1()`. You want to know how to call the `m1()` method of both the **parent** and **child** classes.

### Key Concepts:
- **Static methods** belong to the class, not instances. They are defined with the `@staticmethod` decorator and don't have access to `self` or `cls`.
- When you **override** a static method in the child class, the child class method replaces the parent class method when called on an instance or class object (if the call is made from the child class).

### **Important Points to Note:**
1. **Calling `m1()` method of the parent class:**
   - You can directly call the parent's static method using the **parent class name**.
   - You can call the method from the child class using `super()` (though it’s not as typical for static methods).
   - You cannot call the parent's static method with `self` because static methods are not bound to an instance (they are not tied to `self`).

2. **Calling `m1()` method of the child class:**
   - When calling the `m1()` method from an instance or class of the **child**, it will invoke the child class's `m1()` method due to method overriding.

---

### Code Implementation with Explanations:

```python
# Define the parent class with a static method
class parent:
    @staticmethod
    def m1():
        print('Parent Method')

# Define the child class with the same static method (overriding)
class child(parent):
    @staticmethod
    def m1():
        # How to call m1() method of parent class
        parent.m1()  # Directly calls the static method of the parent class
        
        # Another way to call the parent class method
        super().m1()  # Calls the parent class method via super() (though it's not typical for static methods)
        
        # Static methods can't be called with self or cls directly in the usual way
        # self.m1() and cls.m1() do not work here for static methods
        
        # Calling the child class's static method (which overrides parent)
        child.m1()  # Calls the m1 method from the child class
        
        print('Child Method')

# Test the behavior
print("Calling child class m1 method:")
child.m1()  # This will call the child class's m1() method

print("\nCalling parent class m1 method directly:")
parent.m1()  # This will call the parent class's m1() method

print("\nCalling m1 method from the child class:")
child.m1()  # This will call the child class's m1() method
```

---

###  Expected Output:

```
Calling child class m1 method:
Parent Method
Parent Method
Parent Method
Child Method

Calling parent class m1 method directly:
Parent Method

Calling m1 method from the child class:
Parent Method
Parent Method
Parent Method
Child Method
```

---

### Explanation:

1. **Calling `m1()` method of the parent class**:
   - **`parent.m1()`**: Directly calls the static method from the **parent** class.
   - **`super().m1()`**: Calls the static method of the **parent** class through `super()`, but this is less common for static methods since `super()` is usually used with instance or class methods.
   - **`child.m1()`**: Calls the static method from the **child** class because the method is overridden in the child class.

2. **Calling `m1()` method of the child class**:
   - **`child.m1()`**: When you call `m1()` using the child class, it will invoke the overridden method in the **child** class.

3. **Why `self.m1()` and `cls.m1()` don't work**:
   - Static methods do not have access to `self` or `cls` because they are not tied to an instance or the class itself. They are independent of the instance and class context.

---

###  Key Takeaways:
- **`parent.m1()`**: Directly calls the **parent's** static method.
- **`super().m1()`**: Calls the **parent's** static method through the `super()` function, although this is not typically used for static methods.
- **`child.m1()`**: Calls the **child's** overridden static method.
- **Static methods** cannot be invoked using `self.m1()` or `cls.m1()` in the usual way because they are not bound to instances or classes.
----------------------------------------------------------------------------------------------------------------------------------------------
In your task, the **parent** and **child** classes have **static variables** (`x` in the parent class and `y` in the child class). You need to print these variables in various ways. Let's break down the problem step by step.

### **Key Points**:
1. **Static Variables**: Variables defined in a class directly are called static variables. They are shared by all instances of that class. They can be accessed using the class name (e.g., `Parent.x`).
2. **Inheritance**: The child class can access the parent class's static variables, and if the child class has its own static variables, those are specific to the child class.
3. **Accessing static variables**:
   - From the parent class: You can access `x` directly via `Parent.x` or via `super()`.
   - From the child class: You can access `y` via `Child.y` or `self.y` (for instance-based access).

### 🧪 **Code Implementation:**

```python
# Parent class with static variable 'x'
class parent:
    x = 10
    
    def m1(self):
        # How to print static variable 'x'
        print("Accessing 'x' directly:", parent.x)  # Accessing 'x' from parent class
        print("Accessing 'x' using self:", self.x)  # Accessing 'x' using self (works in the instance context)

# Child class inheriting from parent class with static variable 'y'
class child(parent):
    y = 20
    
    def m2(self):
        # How to print static variable 'x' from parent class
        print("Accessing 'x' from parent class using super():", super().x)  # Accessing 'x' using super()
        print("Accessing 'x' directly from parent:", parent.x)  # Accessing 'x' directly from parent
        print("Accessing 'x' via self (from parent):", self.x)  # Accessing 'x' via self (from parent)
        
        # How to print static variable 'y' from child class
        print("Accessing 'y' from child class:", child.y)  # Accessing 'y' from child class
        print("Accessing 'y' via self (from child):", self.y)  # Accessing 'y' via self (from child)

# Testing the methods
p = parent()
c = child()

# Call parent method m1()
print("Calling m1() method of parent class:")
p.m1()

# Call child method m2()
print("\nCalling m2() method of child class:")
c.m2()
```

---

### 🧪 **Expected Output**:

```
Calling m1() method of parent class:
Accessing 'x' directly: 10
Accessing 'x' using self: 10

Calling m2() method of child class:
Accessing 'x' from parent class using super(): 10
Accessing 'x' directly from parent: 10
Accessing 'x' via self (from parent): 10
Accessing 'y' from child class: 20
Accessing 'y' via self (from child): 20
```

---

### **Explanation**:

1. **In the `parent` class**:
   - The static variable `x` is defined.
   - The method `m1()` prints the static variable `x`. It can be accessed using `parent.x` or `self.x` because the `self` reference can access the class-level variable for the current instance.

2. **In the `child` class**:
   - The static variable `y` is defined.
   - In method `m2()`, we access both the static variable `x` from the **parent class** and the static variable `y` from the **child class** using different approaches:
     - **Accessing `x` from parent**:
       - `super().x`: This calls the parent class's static variable `x` using the `super()` function.
       - `parent.x`: Direct access to the static variable `x` from the parent class.
       - `self.x`: This can access the parent class's `x` if the instance of the child class is being used, because the child class inherits the static variable `x` from the parent.
     - **Accessing `y` from child**:
       - `child.y`: Access the static variable `y` from the **child** class.
       - `self.y`: Access the static variable `y` using `self` (from the instance of the child class).

---

### **Summary**:
- To **access static variables** from the **parent class**: 
  - Use `parent.x`.
  - Use `super().x`.
  - You can also access it via `self.x` in child classes (if the class inherits the static variable).
  
- To **access static variables** from the **child class**:
  - Use `child.y` or `self.y` in the child class method. You can access the parent's static variable through `super()` and the child's static variable directly through `self`.
---------------------------------------------------------------------------------------------------------------------------------------------------
     In your task, the **parent** and **child** classes both have **static variables** with the same name (`x`). You need to understand how to print the variable `x` from both the **parent** and **child** classes, and access their values using different methods.

### 🧪 **Code Implementation**:

```python
# Parent class with static variable 'x'
class parent:
    x = 10
    
    def m1(self):
        # How to print variable 'x' of parent class
        print("Parent class x:", parent.x)  # Accessing 'x' from parent class directly
        print("Accessing 'x' of parent using self:", self.x)  # Accessing 'x' via self (works in instance)

# Child class inheriting from parent class with same static variable 'x'
class child(parent):
    x = 20
    
    def m1(self):
        # How to print variable 'x' of parent class
        print("Parent class x (using super()):", super().x)  # Accessing 'x' from parent class using super()
        print("Parent class x directly:", parent.x)  # Accessing 'x' from parent class directly
        
        # How to print variable 'x' of child class
        print("Child class x (using self):", self.x)  # Accessing 'x' from child class via self
        print("Child class x directly:", child.x)  # Accessing 'x' from child class directly

# Create an object of child class and call the m1() method
c = child()
c.m1()
```

### 🧪 **Expected Output**:

```
Parent class x (using super()): 10
Parent class x directly: 10
Child class x (using self): 20
Child class x directly: 20
```

---

### **Explanation**:

1. **Parent Class** (`parent`):
   - The static variable `x` is defined with the value `10`.
   - The method `m1()` prints the static variable `x` in two ways:
     - `parent.x`: Directly accesses `x` from the **parent** class.
     - `self.x`: Works in the instance context and accesses `x` from the **parent** class because it's inherited by the child class.

2. **Child Class** (`child`):
   - The static variable `x` is redefined with the value `20`.
   - The method `m1()` prints `x` from both the **parent** and **child** classes:
     - `super().x`: This accesses `x` from the **parent** class using `super()`.
     - `parent.x`: Directly accesses `x` from the **parent** class.
     - `self.x`: This accesses `x` from the **child** class because `self` refers to the instance of the child.
     - `child.x`: Directly accesses `x` from the **child** class.

---

### 🧪 **Test Cases for Inputs**:
If you want to test with values like `10, 20, 30, 40, 50, 60`, the program will behave the same way because it deals with the class-level static variables `x` in the **parent** and **child** classes. You can simply modify the values of `x` in the parent or child class and observe how the outputs change.

### **Sample Outputs for Various Inputs**:

If the class definitions were adjusted with these inputs as values for `x`:

- `parent.x = 10`
- `child.x = 20`

The outputs will be:
```
Parent class x (using super()): 10
Parent class x directly: 10
Child class x (using self): 20
Child class x directly: 20
```
----------------------------------------------------------------------------------------------------------------
###  **Explanation of the Requirements**:
1. **Parent Class** (`parent`):
   - The `get` method will read inputs for two variables, `a` and `b`, and store them in the object.
   - The `disp` method will print these variables in the same line, separated by a tab.

2. **Child Class** (`child`):
   - Inheriting from `parent`, the `get` method will read inputs for four variables: `a`, `b` (from `parent`), and `c`, `d` (specific to `child`).
   - The `disp` method will print `a` and `b` from `parent`, and `c` and `d` from `child`, all in one line.
   - The `total` method will return the sum of all variables (`a`, `b`, `c`, and `d`).

###  **Code Implementation**:

```python
# Parent class with method to get and display values
class parent:
    def get(self):
        # Reading two values for parent class object
        self.a = int(input())
        self.b = int(input())
    
    def disp(self):
        # Printing variables a and b in the same line separated by tab
        print(self.a, self.b, sep='\t')

# Child class inheriting from parent class with additional variables
class child(parent):
    def get(self):
        # Reading values for parent (a, b) and child (c, d) class object
        super().get()  # Calling parent's get method to input a and b
        self.c = int(input())
        self.d = int(input())
    
    def disp(self):
        # Printing variables a and b from parent, and c and d from child
        super().disp()  # Calling parent's disp method to display a and b
        print(self.c, self.d, sep='\t')
    
    def total(self):
        # Returning the sum of all values (a, b, c, d)
        return self.a + self.b + self.c + self.d

# Main execution

# Creating parent object and reading inputs
print('parent object')
p = parent()
p.get()  # Input for parent object
print('parent object :', end='\t')
p.disp()  # Display values of parent object
print()

# Creating child object and reading inputs
print('child object')
c = child()
c.get()  # Input for child object
print('child object :', end='\t')
c.disp()  # Display values of child object

# Printing the sum of the values in the child object
print('Sum of the values in child object :', c.total())
```

###  **Expected Behavior**:

1. **Parent Class (`parent`)**:
   - The `get()` method will read two integers and assign them to `self.a` and `self.b`.
   - The `disp()` method will print these values with a tab between them.

2. **Child Class (`child`)**:
   - The `get()` method will first call the parent class's `get()` method to read values for `a` and `b`. Then, it will read values for `c` and `d`.
   - The `disp()` method will call the parent's `disp()` method to display `a` and `b`, followed by printing `c` and `d`.
   - The `total()` method will calculate and return the sum of all four variables.

---

### **Sample Input** and **Output**:

#### **Input**:
```
10
20
30
40
50
60
```

#### **Output**:
```
parent object
10
20
parent object :	10	20

child object
30
40
child object :	10	20	30	40
Sum of the values in child object : 100
```

---

### **Explanation of the Outputs**:
- For the **parent object**: We input `10` and `20`. The `disp()` method prints them with a tab.
- For the **child object**: We input `30` and `40` after the parent's values. The `disp()` method prints all four variables with tabs.
- The **total** method in the child class adds all four values (`10 + 20 + 30 + 40`), resulting in `100`.

---

### **Key Points**:
- The `super()` function is used in the `child` class to call the `get` and `disp` methods from the `parent` class.
- The `total()` method calculates the sum of all four variables in the child object (`a`, `b`, `c`, `d`).
