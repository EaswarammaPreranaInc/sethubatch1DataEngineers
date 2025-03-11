 `isspace()` method:

print('\n  A\t'.isspace())  # False (contains 'A')
print('\n  \t'.isspace())  # True (only whitespace characters)
print('\n  7\t'.isspace())  # False (contains '7')
print('\n'.isspace())       # True (newline is a whitespace character)
print('\n  $\t'.isspace())  # False (contains '$')
print('\t'.isspace())       # True (tab is a whitespace character)
print(''.isspace())         # False (empty string is not considered whitespace)
print(' '.isspace())        # True (only a space character)

### **Explanation of Fixes:**
1. **Incorrect Syntax:** `('\n  A\t' . isspace())` → There should be no space before `.isspace()`.
2. **`isspace()` Method:** It checks if all characters in a string are whitespace.
3. **Edge Cases:** An empty string `''` returns `False` because there are no characters to check.

---------------------------------------------------------------------------------------------------------------------------------------------------------
a, b, c = 25, 10.8, 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a, b, c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a, b, c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a, b, c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a, b, c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x=a, y=b, z=c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z=a, y=b, x=c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z=a, y=b, x=c))
```

---

### **Output Explanation:**
1️⃣ **First print statement:**  
   - `{}` placeholders are filled in order (positional arguments).  
   - `a = 25`, `b = 10.8`, `c = 'Hyd'`.  
   - **Output:**  
     ```
     a  :  25   b  :  10.8   c  :  Hyd  
     ```

2️⃣ **Second print statement:**  
   - `{0}` = `a`, `{1}` = `b`, `{2}` = `c` (explicit positional indices).  
   - **Output:**  
     ```
     a  :  25   b  :  10.8   c  :  Hyd  
     ```

3️⃣ **Third print statement:**  
   - `{2}` = `c`, `{1}` = `b`, `{0}` = `a` (reversed order).  
   - **Output:**  
     ```
     a  :  Hyd   b  :  10.8   c  :  25  
     ```

4️⃣ **Fourth print statement:**  
   - `{2}` is always `c = 'Hyd'`, so it's repeated.  
   - **Output:**  
     ```
     a  :  Hyd   b  :  Hyd   c  :  Hyd  
     ```

5️⃣ **Fifth print statement:**  
   - Named placeholders `{x}`, `{y}`, `{z}` mapped correctly.  
   - `{x} = a = 25`, `{y} = b = 10.8`, `{z} = c = 'Hyd'`.  
   - **Output:**  
     ```
     a  :  25   b  :  10.8   c  :  Hyd  
     ```

6️⃣ **Sixth print statement:**  
   - Different variable mapping: `{x} = c = 'Hyd'`, `{y} = b = 10.8`, `{z} = a = 25`.  
   - **Output:**  
     ```
     a  :  Hyd   b  :  10.8   c  :  25  
     ```

7️⃣ **Seventh print statement:**  
   - `{z}` is always `a = 25`, so it's repeated.  
   - **Output:**  
     ```
     a  :  25   b  :  25   c  :  25  
     ```

---

### **Final Output:**
```
a  :  25   b  :  10.8   c  :  Hyd  
a  :  25   b  :  10.8   c  :  Hyd  
a  :  Hyd   b  :  10.8   c  :  25  
a  :  Hyd   b  :  Hyd   c  :  Hyd  
a  :  25   b  :  10.8   c  :  Hyd  
a  :  Hyd   b  :  10.8   c  :  25  
a  :  25   b  :  25   c  :  25  
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Here's a Python program that determines whether a user input is an alphabet, digit, white space, or special character. It also classifies alphabets into uppercase and lowercase.  

# Get user input (only a single character)
char = input("Enter a character: ")

# Check if it's an alphanumeric character (letter or digit)
if char.isalnum():  
    print("Alphanumeric character")
    
    # Check if it's an alphabet
    if char.isalpha():
        print("Alphabet character")
        
        # Check if it's uppercase or lowercase
        if char.isupper():
            print("Upper case alphabet")
        elif char.islower():
            print("Lower case alphabet")
    
    # Check if it's a digit
    elif char.isdigit():
        print("Digit character")

# Check if it's a whitespace character (space, tab, enter)
elif char.isspace():
    print("White space")

# If it's not alphanumeric or whitespace, it's a special character
else:
    print("Special character")
```

---

### **Expected Outputs:**
1. **Input: `'A'`**  
   **Output:**  
   ```
   Alphanumeric character
   Alphabet character
   Upper case alphabet
   ```

2. **Input: `'a'`**  
   **Output:**  
   ```
   Alphanumeric character
   Alphabet character
   Lower case alphabet
   ```

3. **Input: `'7'`**  
   **Output:**  
   ```
   Alphanumeric character
   Digit character
   ```

4. **Input: `'$'`**  
   **Output:**  
   ```
   Special character
   ```

5. **Input: `<space>`**  
   **Output:**  
   ```
   White space
   ```

6. **Input: `<tab>`**  
   **Output:**  
   ```
   White space
   ```

7. **Input: `<enter>`**  
   **Output:**  
   ```
   White space
   ```

---
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Here's a Python program to reverse a string without using slicing (`[::-1]`):  

```python
# Get user input
string = input("Enter any string: ")

# Initialize an empty string for the reversed result
reversed_string = ""

# Iterate over the original string in reverse order using a loop
for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

# Display the reversed string
print("Reverse String:", reversed_string)
```

---

### **Explanation (Using `Hyd` as input)**  
1. Start with an empty string: `b = ''`
2. Iterate through the string in reverse:
   - `i = 2`, `a[-1] = 'd'`, `b = '' + 'd' = 'd'`
   - `i = 1`, `a[-2] = 'y'`, `b = 'd' + 'y' = 'dy'`
   - `i = 0`, `a[-3] = 'H'`, `b = 'dy' + 'H' = 'dyH'`
3. Final output: **`dyH`**

---

### **Expected Output:**
#### **Input:**  
```
Enter any string: Rama Rao
```
#### **Output:**  
```
Reverse String: oaR amaR
```

This method does not use slicing but relies on a loop to construct the reversed string. 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Here's a Python program to reverse the order of words in a sentence **without using slicing (`[::-1]`)**:  

```python
# Get user input
sentence = input("Enter any sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Initialize an empty string for the reversed sentence
reversed_sentence = ""

# Iterate over the words list in reverse order using a loop
for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + " "

# Remove the trailing space and display the result
print("Reverse order of words:", reversed_sentence.strip())
```

---

### **Step-by-Step Explanation:**
1. **Input:** `"Hyd is green city"`
2. **Splitting (`split()`)** → `['Hyd', 'is', 'green', 'city']` (stored in `words`)
3. **Iterate through `words` in reverse order:**
   - `i = 3`, `words[-1] = 'city'`, `reversed_sentence = '' + 'city '`
   - `i = 2`, `words[-2] = 'green'`, `reversed_sentence = 'city ' + 'green '`
   - `i = 1`, `words[-3] = 'is'`, `reversed_sentence = 'city green ' + 'is '`
   - `i = 0`, `words[-4] = 'Hyd'`, `reversed_sentence = 'city green is ' + 'Hyd '`
4. **Final Output:** `"city green is Hyd"`

---

### **Expected Output:**
#### **Input:**
```
Enter any sentence: students are getting bored
```
#### **Output:**
```
Reverse order of words: bored getting are students
```

This method **avoids slicing** and follows a logical approach using a loop. 
--------------------------------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to **reverse each word** in a sentence while keeping the word order the same:  

```python
# Get user input
sentence = input("Enter any sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Reverse each word using a loop and slicing
reversed_words = [word[::-1] for word in words]

# Join the reversed words into a single string
reversed_sentence = " ".join(reversed_words)

# Display the result
print(reversed_sentence)
```

---

### **Step-by-Step Explanation:**
1. **Input:** `"Hyd is green city"`
2. **Splitting (`split()`)** → `['Hyd', 'is', 'green', 'city']`
3. **Reverse each word using slicing (`[::-1]`)**:
   - `"Hyd"` → `"dyH"`
   - `"is"` → `"si"`
   - `"green"` → `"neerg"`
   - `"city"` → `"ytic"`
4. **Join the reversed words:** `"dyH si neerg ytic"`

---

### **Expected Output:**
#### **Input:**
```
Enter any sentence: hyd is green city
```
#### **Output:**
```
dyh si neerg ytic
```

This approach efficiently **reverses each word** while keeping the original order of words intact. 
-----------------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to **sort a string in alphabetical order** using the `sorted()` function and `join()` method:  

```python
# Get user input
string = input("Enter any string: ")

# Sort the characters of the string
sorted_string = "".join(sorted(string))

# Display the sorted string
print("Sorted string:", sorted_string)
```

---

### **Step-by-Step Explanation:**
1. **Input:** `"RAJESH"`
2. **`sorted(string)`** → `['A', 'E', 'H', 'J', 'R', 'S']`
3. **`"".join(sorted(string))`** → `"AEHJRS"`
4. **Final Output:** `"AEHJRS"`

---

### **Expected Output:**
#### **Input:**
```
Enter any string: RAJESH
```
#### **Output:**
```
Sorted string: AEHJRS
```

This approach works for both **uppercase and lowercase letters**. 
-------------------------------------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to **sort a string such that alphabets appear in alphabetical order and digits appear in ascending order**:  

```python
# Get user input
string = input("Enter any string: ")

# Separate alphabets and digits
alphabets = sorted([char for char in string if char.isalpha()])
digits = sorted([char for char in string if char.isdigit()])

# Concatenate sorted alphabets and digits
sorted_string = "".join(alphabets) + "".join(digits)

# Display the result
print("Sorted string:", sorted_string)
```

---

### **Step-by-Step Explanation (For input `"Z9K3PA7D51"`):**
1. **Separate alphabets and digits**  
   - Alphabets: `['Z', 'K', 'P', 'A', 'D']`
   - Digits: `['9', '3', '7', '5', '1']`
2. **Sort them**  
   - Sorted alphabets: `['A', 'D', 'K', 'P', 'Z']`
   - Sorted digits: `['1', '3', '5', '7', '9']`
3. **Concatenate sorted results:** `"ADKPZ13579"`
4. **Final Output:** `"ADKPZ13579"`

---

### **Expected Output:**
#### **Input:**
```
Enter any string: Z9K3PA7D51
```
#### **Output:**
```
Sorted string: ADKPZ13579
```

This method effectively separates **letters and numbers**, sorts them independently, and then **combines them**. 
----------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Input:**
```
Enter list: [25 , 10.8 , 'Hyd' , True]
```

#### **Execution Steps:**
1. **`a = input('Enter list: ')`**
   - The input function takes user input as a **string**.
   - So, `a` will be the string:
     ```
     "[25 , 10.8 , 'Hyd' , True]"
     ```

2. **`print(type(a))`**
   - Since `input()` always returns a string, the output will be:
     ```
     <class 'str'>
     ```

3. **`print(a)`**
   - The variable `a` contains the **string representation** of the list:
     ```
     [25 , 10.8 , 'Hyd' , True]
     ```

4. **`b = eval(a)`**
   - The `eval()` function **evaluates** the string `a` as a Python expression.
   - Since `a` contains a valid **list representation**, `eval(a)` converts it into an **actual list**:
     ```
     [25, 10.8, 'Hyd', True]
     ```

5. **`print(b)`**
   - Prints the evaluated list:
     ```
     [25, 10.8, 'Hyd', True]
     ```

6. **`print(type(b))`**
   - Since `b` is now an **actual list**, its type is:
     ```
     <class 'list'>
     ```

---

### **Final Output:**
```
Enter list: [25 , 10.8 , 'Hyd' , True]
<class 'str'>
[25 , 10.8 , 'Hyd' , True]
[25, 10.8, 'Hyd', True]
<class 'list'>
```

### **Key Takeaways:**
- `input()` always takes user input as a **string**.
- `eval()` **converts a string representation of a Python expression** into an actual Python object.
- Be **careful** when using `eval()`, as it can execute arbitrary code.
----------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
a = [10, 20, 15, 18]  # List a is created
b = a  # b is assigned the reference of a
print(a is b)  # Checking if a and b refer to the same object
print(a == b)  # Checking if a and b have the same values
b[2] = 12  # Modifying b[2], which also modifies a (since they share the same reference)
print(a)  # Printing the updated list
```

---

### **Execution Steps & Output:**

1. **`a = [10, 20, 15, 18]`**
   - A list `a` is created in memory.

2. **`b = a`**
   - `b` is assigned the reference of `a`, meaning both `a` and `b` point to the **same list in memory**.

3. **`print(a is b)`**
   - `is` checks if `a` and `b` refer to the **same memory location**.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
a = [10, 20, 15, 18]
b = [100, 200, 150]

print(a + b)      # Valid: Concatenates two lists
print(a + 5)      # Error: Cannot add list and integer
print(a + '5')    # Error: Cannot add list and string
print([10, 20] + (30, 40))  # Error: Cannot concatenate list and tuple
```

---

### **Execution & Expected Outputs:**

1. **`print(a + b)`**
   - Lists `a` and `b` are concatenated.
   - **Output:**
     ```python
     [10, 20, 15, 18, 100, 200, 150]
     ```

2. **`print(a + 5)`**
   - **Error:** You **cannot** add an integer (`5`) directly to a list.
   - **Error Message:**
     ```python
     TypeError: can only concatenate list (not "int") to list
     ```

3. **`print(a + '5')`**
   - **Error:** You **cannot** add a string (`'5'`) to a list.
   - **Error Message:**
     ```python
     TypeError: can only concatenate list (not "str") to list
     ```

4. **`print([10, 20] + (30, 40))`**
   - **Error:** You **cannot** concatenate a **list** with a **tuple**.
   - **Error Message:**
     ```python
     TypeError: can only concatenate list (not "tuple") to list
     ```

---

### **Final Output:**
```
[10, 20, 15, 18, 100, 200, 150]
TypeError: can only concatenate list (not "int") to list
TypeError: can only concatenate list (not "str") to list
TypeError: can only concatenate list (not "tuple") to list
```

---

### **Key Takeaways:**
1. **Lists can be concatenated using `+`, but only with other lists.**
2. **Integers and strings cannot be directly added to a list using `+`.**
3. **Lists and tuples cannot be concatenated directly.**
-------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
list = [25, 10.8, 'Hyd', True]

# Unpacking list into three variables
a, *b, c = list  
print('a :', a)  # a gets the first element (25)
print('b :', b)  # b gets the middle elements ([10.8, 'Hyd'])
print('c :', c)  # c gets the last element (True)
print(type(b))   # type of b is <class 'list'>

# Another unpacking pattern
x, *y = list  
print('x :', x)  # x gets the first element (25)
print('y :', y)  # y gets the remaining elements ([10.8, 'Hyd', True])

# Another unpacking pattern
*p, q = list  
print('p :', p)  # p gets all elements except the last ([25, 10.8, 'Hyd'])
print('q :', q)  # q gets the last element (True)
```

---

### **Execution & Expected Outputs:**
#### **Initial List:**
```
list = [25, 10.8, 'Hyd', True]
```

1. **`a, *b, c = list`**
   - `a = 25`
   - `b = [10.8, 'Hyd']`  (all middle elements)
   - `c = True`
   - **Output:**
     ```
     a : 25
     b : [10.8, 'Hyd']
     c : True
     <class 'list'>
     ```

2. **`x, *y = list`**
   - `x = 25`
   - `y = [10.8, 'Hyd', True]` (remaining elements)
   - **Output:**
     ```
     x : 25
     y : [10.8, 'Hyd', True]
     ```

3. **`*p, q = list`**
   - `p = [25, 10.8, 'Hyd']` (all elements except the last)
   - `q = True`
   - **Output:**
     ```
     p : [25, 10.8, 'Hyd']
     q : True
     ```

---

### **Final Output:**
```
a : 25
b : [10.8, 'Hyd']
c : True
<class 'list'>
x : 25
y : [10.8, 'Hyd', True]
p : [25, 10.8, 'Hyd']
q : True
```

---

### **Key Takeaways:**
1. **`*variable` collects multiple elements into a list.**
2. **Unpacking can be used to extract the first, last, or middle elements easily.**
3. **`type(b)` is `<class 'list'>` because `*b` collects multiple values into a list.**
--------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Error Analysis**

#### **Code:**
```python
list = [25, 10.8, 'Hyd', True]

# Unpacking attempt with 5 variables (Error)
a, b, c, d, e = list  # ❌ Error: list has only 4 elements
```
Since `list` has **only 4 elements**, but we are trying to unpack it into **5 variables**, Python will throw an error:

**Error Message:**
```python
ValueError: not enough values to unpack (expected 5, got 4)
```

---

### **Corrected Code & Execution**
```python
list = [25, 10.8, 'Hyd', True]

# Correct unpacking
a, b, *c, d = list  
print('a :', a)  # First element (25)
print('b :', b)  # Second element (10.8)
print('c :', c)  # Middle elements (['Hyd'])
print('d :', d)  # Last element (True)
```
**Output:**
```
a : 25
b : 10.8
c : ['Hyd']
d : True
```
---

### **Next Error Case**
```python
a, b, *c, d, e = list  # ❌ Error: list has 4 elements but expecting 5 variables
```
**Error Message:**
```python
ValueError: not enough values to unpack (expected 5, got 4)
```
Similarly, the next line:
```python
a, b, *c, d, e, f = list  # ❌ Error: list has only 4 elements, expecting 6 variables
```
will **also throw an error**.

---

### **Final Notes:**
1. ✅ `a, b, *c, d = list` **(Valid: `c` collects middle elements)**
2. ❌ `a, b, c, d, e = list` **(Error: Too many variables for the list size)**
3. ❌ `a, b, *c, d, e = list` **(Error: Too many variables)**
4. ❌ `a, b, *c, d, e, f = list` **(Error: Even more variables)**

Always ensure that the number of variables matches the **length of the list**, especially when using `*` to collect multiple values.
-----------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
list = [25, 10.8, 'Hyd', True]

# Unpacking the list
a, b, _, d = list  

print('a :', a)  # First element (25)
print('b :', b)  # Second element (10.8)
print('_ :', _)  # Third element ('Hyd') - _ is just a normal variable
print('d :', d)  # Fourth element (True)
```

---

### **Execution & Expected Outputs:**
1. `a = 25`
2. `b = 10.8`
3. `_ = 'Hyd'` (**Note:** `_` is just a variable name; it still holds the value `'Hyd'`.)
4. `d = True`

**Final Output:**
```
a : 25
b : 10.8
_ : Hyd
d : True
```

---

### **Key Takeaways:**
1. **`_` is just a normal variable** in Python. Although it's conventionally used to indicate "ignore this value," it **still holds the assigned value** (`'Hyd'` in this case).
2. If you don't intend to use the value at all, you **can still access it later**, but it is **not automatically ignored**.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Error Analysis**

#### **Code:**
```python
list = [25, 10.8, 'Hyd', True, 3 + 4j]

# Attempting to unpack the list
a, b, a, d, a = list  

print('a :', a)  
print('b :', b)  
print('d :', d)  
```

---

### **Understanding Variable Assignment**
1. **List values:** `[25, 10.8, 'Hyd', True, (3 + 4j)]`
2. **Variable assignment:**
   - `a = 25` (First occurrence of `a`)
   - `b = 10.8`
   - `a = 'Hyd'` (Overwrites the previous `a`)
   - `d = True`
   - `a = 3 + 4j` (Overwrites `a` again)

---

### **Final Variable Values**
- `a = 3 + 4j` (**Final value of `a` after multiple assignments**)
- `b = 10.8`
- `d = True`

**Output:**
```
a : (3+4j)
b : 10.8
d : True
```

---

### **Key Takeaways**
1. **Python allows multiple assignments of the same variable name in unpacking**, but each new assignment overwrites the previous one.
2. **Only the last assigned value of `a` is retained (`3+4j`).**
3. **No error occurs**, but the previous values of `a` are lost.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
list = [25, 10.8, 'Hyd', True, 3 + 4j]

# Unpacking the list
a, b, _, d, _ = list  

print('a :', a)  # First element (25)
print('b :', b)  # Second element (10.8)
print('_ :', _)  # Last occurrence of `_` (3 + 4j)
print('d :', d)  # Fourth element (True)
print('_:', _)   # `_` still holds (3 + 4j)
```

---

### **Understanding Variable Assignment**
1. **List values:** `[25, 10.8, 'Hyd', True, (3 + 4j)]`
2. **Variable assignment:**
   - `a = 25`
   - `b = 10.8`
   - `_ = 'Hyd'` (**first assignment**)
   - `d = True`
   - `_ = 3 + 4j` (**overwrites `_`**)

---

### **Final Variable Values**
- `a = 25`
- `b = 10.8`
- `_ = 3 + 4j` (**Final value due to overwrite**)
- `d = True`

---

### **Expected Output**
```
a : 25
b : 10.8
_ : (3+4j)
d : True
_: (3+4j)
```

---

### **Key Takeaways**
1. **`_` is just a normal variable** in Python, not a special character.
2. **Only the last assigned value remains** in `_`, which is `(3+4j)`, because it gets overwritten.
3. If `_` is truly meant to ignore values, **don't use it multiple times where values matter**—use different variable names instead.
--------------------------------------------------------------------------------------------------------------------------------------------------------
### **Error Analysis:**
```python
list = [25, 10.8, 'Hyd', True, 3 + 4j]
a, *b, c, *d, e = list  # ❌ SyntaxError
```

---

### **Understanding the Issue**
- In Python **unpacking**, the `*` operator is used to capture multiple elements into a list.
- However, **only one `*` operator is allowed per unpacking assignment**.

---

### **Why is this an error?**
- The statement **`a, *b, c, *d, e = list`** tries to use **two starred (`*`) variables**:  
  - `*b`  
  - `*d`  
- Python **does not allow** multiple starred expressions in a single unpacking.

**Result:**  
```python
SyntaxError: multiple starred expressions in assignment
```

---

### **Correct Approach**
To fix this, you should use **only one `*` variable**:

```python
list = [25, 10.8, 'Hyd', True, 3 + 4j]
a, *b, c, d = list  # ✅ Correct

print('a :', a)  # 25
print('b :', b)  # [10.8, 'Hyd']
print('c :', c)  # True
print('d :', d)  # (3 + 4j)
```

---

### **Key Takeaways**
✅ **Only one `*` variable is allowed in unpacking.**  
❌ **Trying to use multiple `*` results in a `SyntaxError`.**
---------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
list = [[25, 10.8], 'Hyd', True]  

# Unpacking the list into three variables
a, b, c = list  

print('a : ', a)  
print('b : ', b)  
print('c : ', c)  
```

---

### **Understanding Variable Assignment**
The list contains **three elements**:
```python
[
  [25, 10.8],   # First element (a)
  'Hyd',        # Second element (b)
  True          # Third element (c)
]
```

- `a = [25, 10.8]`  → First element (a sublist)
- `b = 'Hyd'`       → Second element (a string)
- `c = True`        → Third element (a boolean)

---

### **Expected Output:**
```
a :  [25, 10.8]
b :  Hyd
c :  True
```

---

### **Key Takeaways:**
✅ **Unpacking works as long as the number of variables matches the number of elements in the list.**  
✅ **Lists inside a list are treated as a single element.**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
list = [[25, 10.8], 'Hyd', True]  

# Unpacking the list
[a, b], c, d = list  

print('a :', a)  
print('b :', b)  
print('c :', c)  
print('d :', d)  
```

---

### **Understanding Variable Assignment**
The list contains **three elements**:
```python
[
  [25, 10.8],   # First element (a sublist)
  'Hyd',        # Second element (a string)
  True          # Third element (a boolean)
]
```

- `[a, b] = [25, 10.8]`  
  - `a = 25`
  - `b = 10.8`
- `c = 'Hyd'`
- `d = True`

---

### **Expected Output:**
```
a : 25
b : 10.8
c : Hyd
d : True
```

---

### **Second Part:**
```python
a, b, c, d = list  # ❌ ERROR
```
- The **list** has **three** elements.
- The unpacking expects **four** variables (`a, b, c, d`).
- **This causes a `ValueError`** because the number of variables **does not match** the number of elements in the list.

#### **Error Message:**
```
ValueError: too many values to unpack (expected 4)
```

---

### **Key Takeaways**
✅ **Nested unpacking works as long as the structure matches.**  
❌ **The second unpacking attempt fails because the number of elements doesn’t match the variables.**
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
a = [10, 20, 15, 18]
b = [10, 20, 15, 18]
c = [10, 20, 25, 9]
d = [10, 20, 7, 22]

print(a == b)   # True  
print(a is b)   # False  
print(a < c)    # True  
print(a > d)    # True  
print(a >= c)   # False  
print(a <= d)   # False  
print(a != c)   # True  
print(a != b)   # False  
print(a == c)   # False  
```

---

### **Understanding Each Comparison:**

1️⃣ **`a == b` → `True`**
   - Both lists have **the same elements** in **the same order**.

2️⃣ **`a is b` → `False`**
   - `a` and `b` **are different objects** in memory, even though they have identical values.
   - `is` checks for **identity (same memory location)**, not just equality.

3️⃣ **`a < c` → `True`**
   - Python compares lists **element by element**.
   - First two elements (`10, 20`) are **equal**.
   - The third element in `a` is `15`, but in `c` it is `25`.  
     **Since `15 < 25`, `a < c` is `True`**.

4️⃣ **`a > d` → `True`**
   - First two elements (`10, 20`) are **equal**.
   - The third element in `a` is `15`, but in `d` it is `7`.  
     **Since `15 > 7`, `a > d` is `True`**.

5️⃣ **`a >= c` → `False`**
   - We already determined that `a < c` is `True`,  
     so `a >= c` must be `False`.

6️⃣ **`a <= d` → `False`**
   - Since `a > d` is `True`,  
     `a <= d` must be `False`.

7️⃣ **`a != c` → `True`**
   - `a` and `c` have different elements (`15` vs `25`).

8️⃣ **`a != b` → `False`**
   - Since `a == b` is `True`,  
     `a != b` must be `False`.

9️⃣ **`a == c` → `False`**
   - `a` and `c` are **not identical**, so this is `False`.

---

### **Final Output:**
```
True
False
True
True
False
False
True
False
False
```

---

### **Key Takeaways**
✅ **Lists are compared element by element.**  
✅ **`is` checks if two lists are the same object in memory, not just equal in value.**  
✅ **Lexicographic (dictionary-like) comparison applies for `<, >, <=, >=` operators.**
-------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
a = [10, 20, 15, 18]
b = [20, 18, 15, 10]

print(a == b)   # False
print(a is b)   # False
```

---

### **Understanding Each Comparison:**

1️⃣ **`a == b` → `False`**
   - **Equality (`==`)** checks if the elements in both lists are **identical in order**.
   - `a = [10, 20, 15, 18]`
   - `b = [20, 18, 15, 10]`
   - The order of elements **differs**, so `a == b` is **False**.

2️⃣ **`a is b` → `False`**
   - **Identity (`is`)** checks if `a` and `b` **refer to the same object in memory**.
   - `a` and `b` are two separate lists, even if they had the same elements.
   - Since they are **different objects**, `a is b` is **False**.

---

### **Final Output:**
```
False
False
```

---

### **Key Takeaways**
✅ **`==` checks for value equality, not object identity.**  
✅ **`is` checks if both lists refer to the same memory location.**  
✅ **Order matters when comparing lists with `==`.**
-----------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis**

#### **Code:**
```python
a = [25, 10.8, 'Hyd', True]
print(len(a))  # Output: 4

b = []
print(len(b))  # Output: 0

c = [[10, 20], 30, 40]
print(len(c))  # Output: 3
```

---

### **Understanding the `len()` Function**
- **`len(list)`** returns the **number of elements** present in the list.
- It does **not** count individual elements within nested lists.

---

### **Breakdown of Each Case**
1️⃣ **`len(a)` → `4`**
   - `a = [25, 10.8, 'Hyd', True]`
   - There are **4 elements** in the list.

2️⃣ **`len(b)` → `0`**
   - `b = []` (empty list)
   - Since there are **no elements**, the length is **0**.

3️⃣ **`len(c)` → `3`**
   - `c = [[10, 20], 30, 40]`
   - The elements are:
     - `[10, 20]` (counts as **one element**, not two)
     - `30`
     - `40`
   - Total **3 elements**.

---

### **Final Output:**
```
4
0
3
```

---

### **Key Takeaways**
✅ `len()` counts **top-level elements** in a list.  
✅ Nested lists count as **one element**, regardless of their contents.  
✅ `len([]) = 0` for an empty list.
--------------------------------------------------------------------------------------------------------------------------------------------------
### **Step-by-Step Execution & Output Analysis of `sum()` Function**

#### **Code:**
```python
a = [25, 10.8, True]
print(sum(a))  # Output: 36.8

b = [3 + 4j, 5 + 6j]
print(sum(b))  # Output: (8+10j)

c = [25, 10.8, True, 3 + 4j, False]
print(sum(c))  # Output: (39.8+4j)

d = [10, 20, 15, 18]
print(sum(d))  # Output: 63

e = [25, 10.8, 'Hyd', True]
print(sum(e))  # TypeError: unsupported operand type(s) for +: 'float' and 'str'
```

---

### **Understanding the `sum()` Function**
- **`sum(list)`** returns the **sum of numeric elements** in the list.
- The elements must be **integers, floats, complex numbers, or booleans**.
- `True` is treated as `1`, and `False` is treated as `0`.
- If the list contains **strings**, it raises a `TypeError`.

---

### **Breakdown of Each Case**
1️⃣ **`sum(a)` → `36.8`**
   - `a = [25, 10.8, True]`
   - `True` is `1`, so:  
     `25 + 10.8 + 1 = 36.8`

2️⃣ **`sum(b)` → `(8+10j)`**
   - `b = [3 + 4j, 5 + 6j]`
   - Complex number addition:  
     `(3+4j) + (5+6j) = (8+10j)`

3️⃣ **`sum(c)` → `(39.8+4j)`**
   - `c = [25, 10.8, True, 3 + 4j, False]`
   - `True` is `1`, `False` is `0`
   - `25 + 10.8 + 1 + (3+4j) + 0 = (39.8+4j)`

4️⃣ **`sum(d)` → `63`**
   - `d = [10, 20, 15, 18]`
   - `10 + 20 + 15 + 18 = 63`

5️⃣ **`sum(e)` → `TypeError`**
   - `e = [25, 10.8, 'Hyd', True]`
   - `'Hyd'` is a **string**, which **cannot** be summed with numbers.
   - Raises:  
     ```
     TypeError: unsupported operand type(s) for +: 'float' and 'str'
     ```

---

### **Final Output:**
```
36.8
(8+10j)
(39.8+4j)
63
TypeError
```

---

### **Key Takeaways**
✅ `sum()` works with **integers, floats, complex numbers, and booleans**.  
✅ `True = 1`, `False = 0` in arithmetic operations.  
✅ **Mixing strings with numbers in `sum()` results in `TypeError`.**  
✅ Complex numbers **can be summed** normally.
---------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding the `sum()` Function on a Nested List**
```python
a = [[10, 20, 15, 18]]
print(sum(a))  
```
#### **What Happens Here?**
- `sum(a)` tries to add the elements of `a`, but `a` is **a list containing another list**.
- `sum()` does **not** automatically sum inner list elements.
- **Error Occurs:**
  ```
  TypeError: unsupported operand type(s) for +: 'int' and 'list'
  ```
  **Reason:** `sum()` expects numbers, but it encounters a **list inside a list**.

---

### **How to Determine the Sum of Inner List Elements?**
#### ✅ **Method 1: Accessing the Inner List Directly**
```python
print(sum(a[0]))  # Output: 63
```
**Explanation:**
- `a[0]` extracts `[10, 20, 15, 18]` (the inner list).
- `sum(a[0])` correctly sums the elements:  
  `10 + 20 + 15 + 18 = 63`

---

### **Another Way to Determine the Sum of Inner List Elements**
#### ✅ **Method 2: Using List Comprehension + `sum()`**
```python
print(sum(sum(inner_list) for inner_list in a))  # Output: 63
```
**Explanation:**
- This is useful when `a` contains **multiple inner lists**.
- It **iterates over** each inner list (`inner_list`) and sums its elements.
- Since `a` has **only one** inner list, it produces the same result.

---

### **Final Corrected Code**
```python
a = [[10, 20, 15, 18]]

# Incorrect usage
# print(sum(a))  # ❌ TypeError

# Correct approaches
print(sum(a[0]))  # ✅ Output: 63
print(sum(sum(inner_list) for inner_list in a))  # ✅ Output: 63
```

---

### **Key Takeaways**
✅ **Directly sum the inner list using `sum(a[0])`.**  
✅ **For multiple inner lists, use `sum(sum(inner_list) for inner_list in a)`.**  
✅ **`sum()` does not automatically sum elements inside nested lists.**
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `max()` and `min()` Functions on Lists**

The `max()` and `min()` functions return the **largest** and **smallest** elements in a list.

---

### **Analyzing the Given Code**
```python
a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))  # ✅ Output: 30
print(min(a))  # ✅ Output: 5
```
✅ Works because `a` contains only **numeric values**.

---

### **Using `max()` and `min()` on Strings**
```python
b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))  # ✅ Output: 'Vamsi'  (Based on **lexicographic order**)
print(min(b))  # ✅ Output: 'Amar'   (Smallest in **alphabetical order**)
```
✅ **Works with strings** using **dictionary order** (A-Z).

---

### **Error Cases**
#### ❌ **List with Mixed Data Types**
```python
c = [25, 10.8, 3 + 4j, True]
print(max(c))  
```
🔴 **Error:**
```
TypeError: '>' not supported between instances of 'complex' and 'float'
```
**Reason:**  
- `max()` and `min()` **cannot compare complex numbers** with real numbers.

---

#### ❌ **List with Incompatible Data Types**
```python
d = [25, '35']
print(max(d))
```
🔴 **Error:**
```
TypeError: '>' not supported between instances of 'str' and 'int'
```
**Reason:**  
- `'35'` (string) **cannot be compared** with `25` (integer).

---

#### ❌ **Empty List**
```python
print(max([]))
print(min([]))
```
🔴 **Error:**
```
ValueError: max() arg is an empty sequence
ValueError: min() arg is an empty sequence
```
**Reason:**  
- `max()` and `min()` **cannot work on an empty list**.

---

### **Final Corrected Code**
```python
a = [10, 20, 15, 18, 30, 5, 12]
print(max(a))  # ✅ 30
print(min(a))  # ✅ 5

b = ['Rama', 'Sita', 'Rajesh', 'Kiran', 'Amar', 'Vamsi', 'Manohar']
print(max(b))  # ✅ 'Vamsi'
print(min(b))  # ✅ 'Amar'

# Handling complex numbers separately
c = [25, 10.8, 3 + 4j, True]
real_numbers = [x for x in c if isinstance(x, (int, float))]
print(max(real_numbers))  # ✅ 25

# Handling mixed types safely
d = [25, '35']
d_strings = [str(x) for x in d]  # Convert all to strings
print(max(d_strings))  # ✅ '35' (lexicographically larger)

# Handling empty list safely
empty_list = []
print(max(empty_list) if empty_list else "List is empty")  # ✅ Avoids error
print(min(empty_list) if empty_list else "List is empty")  # ✅ Avoids error
```

---

### **Key Takeaways**
✅ `max()` and `min()` **work on numbers and strings separately**.  
✅ **String comparison follows alphabetical order** (A-Z).  
✅ **Cannot compare complex numbers with real numbers**.  
✅ **Mixed data types (int & str) cause TypeErrors**.  
✅ **Empty lists cause ValueErrors** unless handled properly.
-------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `list()` Function**

The `list()` function is used to **convert an iterable (e.g., tuple, string, etc.) into a list**.

---

### **Code Analysis**
```python
a = (10, 20, 15, 18)  # Tuple
b = list(a)           # Converts tuple to list

print(b)         # ✅ Output: [10, 20, 15, 18]  (List representation of tuple)
print(type(b))   # ✅ Output: <class 'list'>   (Confirms it's a list)
print(a is b)    # ✅ Output: False  (Different memory locations)
print(a == b)    # ✅ Output: True   (Same values)
```

---

### **Key Points**
✅ `list(a)` **creates a new list from the tuple**.  
✅ `is` **compares memory locations**, so `a is b` is **False** because they are different objects.  
✅ `==` **compares values**, so `a == b` is **True** since both have the same elements.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `list()` Function with Different Inputs**
The `list()` function is used to convert a **sequence** (iterable) into a list. If no arguments are given, it returns an empty list. If a **non-sequence** is passed, it raises an error.

---

### **Code Execution & Expected Outputs**
```python
a = range(4, 10, 2)  
b = list(a)   
print(b)          # ✅ Output: [4, 6, 8]   (range converted to list)
print(type(b))    # ✅ Output: <class 'list'>

a = list('Vamsi')  
print(a)          # ✅ Output: ['V', 'a', 'm', 's', 'i']  (String converted to list of characters)

a = list()  
print(a)          # ✅ Output: []  (Empty list)

print(list(25))   # ❌ TypeError: 'int' object is not iterable
print(list(10.8)) # ❌ TypeError: 'float' object is not iterable
print(list(True)) # ❌ TypeError: 'bool' object is not iterable
print(list(None)) # ❌ TypeError: 'NoneType' object is not iterable
```

---

### **Key Takeaways**
✅ `list(sequence)` → Converts a sequence (like `range`, `str`, `tuple`) into a list.  
✅ `list()` → Returns an **empty list**.  
❌ `list(non-sequence)` → Raises a **TypeError** because numbers, booleans, and `None` are not iterable.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `list()` with Different Data Types**
The `list()` function converts an **iterable** (tuples, sets, lists, etc.) into a list.  
Let's analyze the given code and expected outputs.

---

### **Code Execution & Expected Outputs**
```python
# Case 1: Converting a tuple of tuples into a list
a = ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(list(a))  
# ✅ Output: [(10, 20), (30, 40, 50), (60, 70, 80, 90)]
# Explanation: Each inner tuple remains unchanged; only the outer tuple is converted to a list.

# Case 2: Converting a set of tuples into a list
b = {(10, 20), (30, 40, 50), (60, 70, 80, 90)}
print(list(b))  
# ✅ Output: [(10, 20), (30, 40, 50), (60, 70, 80, 90)] (Order may vary)
# Explanation: Sets are **unordered**, so the output order may not match the input.

# Case 3: Converting a tuple containing a list, tuple, and set into a list
c = ([10, 20], (30, 40), {50, 60})
print(list(c))  
# ✅ Output: [[10, 20], (30, 40), {50, 60}]
# Explanation: The inner elements (list, tuple, set) remain unchanged, and only the outer tuple is converted into a list.
```

---

### **Key Takeaways**
✅ `list(tuple_of_tuples)` → Converts the outer tuple to a list, keeping inner tuples intact.  
✅ `list(set_of_tuples)` → Converts the set to a list, but **order is not guaranteed**.  
✅ `list(tuple_with_mixed_types)` → Converts the outer tuple into a list while keeping inner elements unchanged.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `sorted()` with Lists of Strings**
The `sorted()` function returns a **new sorted list** while keeping the original list unchanged. It sorts strings in **lexicographical (alphabetical) order** by default.

---

### **Code Execution & Expected Outputs**
```python
a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']

# Sorting in ascending order (alphabetical)
b = sorted(a)
print(b)  
# ✅ Output: ['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
# Explanation: Strings are sorted alphabetically, with spaces being treated as smaller than letters.

# Sorting in descending order (reverse alphabetical)
c = sorted(a, reverse=True)
print(c)  
# ✅ Output: ['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
# Explanation: The order is reversed from the previous sorting.

# Original list remains unchanged
print(a)  
# ✅ Output: ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
# Explanation: `sorted()` does **not** modify `a`, it only returns a new sorted list.
```

---

### **Key Takeaways**
✅ `sorted(a)` → Returns a **new list** sorted in ascending order.  
✅ `sorted(a, reverse=True)` → Returns a **new list** sorted in descending order.  
✅ `a` (original list) remains **unchanged**.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding `all()` Function in Python**
The `all()` function returns:
- `True` **if all elements** in the list are **truthy**.
- `False` **if at least one** element is **falsy**.
- `True` **for an empty list** (since there are no false values).

---

### **Code Execution & Expected Outputs**
```python
# List of Boolean expressions
a = [12 > 10 , 5 < 20 , 30 == 30]  
print(all(a))  
# ✅ Output: True
# Explanation: All conditions evaluate to True.

b = [9 >= 6 , 12 <= 9 , 6 == 6]  
print(all(b))  
# ✅ Output: False
# Explanation: `12 <= 9` is False, so `all()` returns False.

# List containing an empty string (Falsy)
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']  
print(all(c))  
# ✅ Output: False
# Explanation: The empty string `''` is Falsy.

# List containing `0` (Falsy)
d = [10 , 0 , 20]  
print(all(d))  
# ✅ Output: False
# Explanation: `0` is Falsy.

# Empty list
e = []  
print(all(e))  
# ✅ Output: True
# Explanation: `all([])` returns True because there are no False values.
```

---

### **Key Takeaways**### **Understanding `any()` Function in Python**
The `any()` function returns:
- `True` **if at least one element** in the list is **truthy**.
- `False` **if all elements** in the list are **falsy**.
- `False` **for an empty list** (since there are no true values).

---

### **Code Execution & Expected Outputs**
```python
# List of Boolean expressions
a = [12 > 18 , 5 < 20 , 35 == 30]  
print(any(a))  
# ✅ Output: True
# Explanation: `5 < 20` is True, so `any()` returns True.

b = [12 > 18 , 25 < 20 , 35 == 30]  
print(any(b))  
# ✅ Output: False
# Explanation: All conditions evaluate to False.

# List containing at least one truthy value (25)
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]  
print(any(c))  
# ✅ Output: True
# Explanation: `25` is Truthy.

# List containing only falsy values
d = [0 , 0.0 , '' , 0 + 0j , False]  
print(any(d))  
# ✅ Output: False
# Explanation: Every element is Falsy.

# Empty list
e = []  
print(any(e))  
# ✅ Output: False
# Explanation: `any([])` returns False because there are no True values.
```

---

### **Key Takeaways**
✅ `any()` checks if **at least one element** in the list is **truthy**.  
✅ **Falsy values** include `0`, `False`, `None`, `''`, and empty structures (`[]`, `{}`, `set()`).  
✅ An **empty list** returns `False`.  

---

### **Practical Use Case**
Instead of:
```python
if cond1 or cond2 or cond3 or cond4:
```
You can write:
```python
if any([cond1, cond2, cond3, cond4]):
```
This makes the code **cleaner** and **more readable**! ✅
✅ `all()` checks if **all elements** in the list are **truthy**.  
✅ **Falsy values** include `0`, `False`, `None`, `''`, and empty structures (`[]`, `{}`, `set()`).  
✅ An **empty list** returns `True`.  

---

### **Practical Use Case**
Instead of:
```python
if cond1 and cond2 and cond3 and cond4:
```
You can write:
```python
if all([cond1, cond2, cond3, cond4]):
```
--------------------------------------------------------------------------------------------------------------------------------------------------------
