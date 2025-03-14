Here's the demo program for the clear() method in Python:
# Creating a list
my_list = [10, 20, 15, 18]

# Printing original list
print("my_list:", my_list)

# Using clear() method to remove all elements
my_list.clear()

# Printing the list after clearing
print("List after clear():", my_list)

Expected Output:
Original list: [10, 20, 15, 18]
List after clear(): []


### **Key Differences Between `clear()`, `remove()`, and `pop()`**
1. **`clear()` method**  
   - Removes **all** elements from the list, making it empty.  
   - Example:
     my_list = [1, 2, 3]
     my_list.clear()
     print(my_list)  # Output: []
     ```

2. **`remove(value)` method**  
   - Removes **the first occurrence** of a specific value.  
   - Example:
     my_list = [1, 2, 3, 2]
     my_list.remove(2)
     print(my_list)  # Output: [1, 3, 2]
     ```

3. **`pop(index)` method**  
   - Removes an element **at a specific index** and returns it.  
   - If no index is provided, it removes the **last** element.  
   - Example:
     my_list = [1, 2, 3]
     removed = my_list.pop(1)
     print(removed)  # Output: 2
     print(my_list)  # Output: [1, 3]
-----------------------------------------------------------------------------------------------------------------------------------
Here's the **demo program** for the `reverse()` method in Python:
# Creating a list
a = [10, 20, 15, 18]

# Printing the original list
print("list:", a)

# Using the reverse() method to reverse the list
a.reverse()

# Printing the list after using reverse()
print("List after reverse():", a)
```

### **Expected Output:**
```
Original list: [10, 20, 15, 18]
List after reverse(): [18, 15, 20, 10]
```

---

### **Key Points About `reverse()` Method**
1. **What does `reverse()` do?**  
   - It **reverses the elements** of the list **in place** (modifies the original list).  

2. **Where are the results stored?**  
   - The results are stored **in the same list** (lists are mutable in Python).  

---

### **Alternative Method: Using Slicing**
If you want to **reverse a list without modifying the original**, use slicing:
```python
a = [10, 20, 15, 18]
reversed_list = a[::-1]  # Creates a new reversed list
print(reversed_list)  # Output: [18, 15, 20, 10]
```
-------------------------------------------------------------------------------------------------------------------------------
Here’s the **demo program** for the `sort()` method in Python:
# Creating a list
my_list = [10, 20, 15, 18, 5]

# Printing the original list
print("list:", my_list)

# Sorting the list in ascending order
my_list.sort()
print("List after sort():", my_list)

# Sorting the list in descending order
my_list.sort(reverse=True)
print("List after sort(reverse=True):", my_list)
```

### **Expected Output:**
```
Original list: [10, 20, 15, 18, 5]
List after sort(): [5, 10, 15, 18, 20]
List after sort(reverse=True): [20, 18, 15, 10, 5]
```

---

### **Key Points About `sort()` Method**
1. **What does `sort()` do?**  
   - Sorts the list **in ascending order** by default.
   - Modifies the list **in place** (does not return a new list).

2. **What does `sort(reverse=True)` do?**  
   - Sorts the list **in descending order**.

---

### **Alternative Method: Using `sorted()`**
If you want to **sort without modifying the original list**, use `sorted()`:
```python
my_list = [10, 20, 15, 18, 5]

# Ascending order without modifying the original list
ascending_list = sorted(my_list)
print("Ascending:", ascending_list)  # Output: [5, 10, 15, 18, 20]

# Descending order without modifying the original list
descending_list = sorted(my_list, reverse=True)
print("Descending:", descending_list)  # Output: [20, 18, 15, 10, 5]
```
------------------------------------------------------------------------------------------------------------------------------------------------
### **Understanding the `sort()` Method on a List of Strings**  

a = ['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
print(a)

a.sort()  # Sorting in ascending order
print(a)

a.sort(reverse=True)  # Sorting in descending order
print(a)

---

### **Step-by-Step Execution and Expected Outputs:**

#### **Step 1: Print Original List**
```
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
```
✅ **No changes yet, just printing the original list.**

---

#### **Step 2: `a.sort()` → Sorting in Ascending Order**
- Strings are sorted **alphabetically (lexicographically)**.
- Sorting follows **ASCII values**, meaning **uppercase letters come before lowercase**.
- **Sorting order:** `'Amar'`, `'Kiran'`, `'Rajesh'`, `'Rama'`, `'Rama Rao'`, `'Sita'`, `'Vamsi'`.

**Output after sorting:**
```
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
```

---

#### **Step 3: `a.sort(reverse=True)` → Sorting in Descending Order**
- Reverse the sorted order.

**Output after sorting in reverse order:**
```
['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
```

---

### **Final Expected Output:**
```
['Rama', 'Rajesh', 'Amar', 'Sita', 'Vamsi', 'Kiran', 'Rama Rao']
['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama Rao', 'Sita', 'Vamsi']
['Vamsi', 'Sita', 'Rama Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
```

✅ **Key Takeaways:**
1. **Sorting is case-sensitive** (capital letters come before lowercase in ASCII).
2. **Ascending order sorts alphabetically**.
3. **Descending order reverses the sorted list**.
--------------------------------------------------------------------------------------------------------------------------------------------------------
### **Error Analysis:**
#### **Given Code:**
```python
a = [25, 10.8, 'Hyd', True]
a.sort()
```

#### **What Happens?**
- The `sort()` method tries to sort the elements of `a`.
- However, `a` contains **different data types**:  
  - `int` (`25`)
  - `float` (`10.8`)
  - `str` (`'Hyd'`)
  - `bool` (`True`)

- Python **cannot compare different data types directly** (e.g., `int` vs. `str`), leading to a **TypeError**.

---

### **Error Message:**
```
TypeError: '<' not supported between instances of 'str' and 'int'
```

---

### **Solution:**
To avoid this error, ensure that all elements in the list are of the **same type**.  

#### ✅ **Fix 1: Use a List with Only Comparable Data Types**
```python
a = [25, 10.8, 100, 5]  # All numbers
a.sort()
print(a)  # Output: [5, 10.8, 25, 100]
```

#### ✅ **Fix 2: Sort Strings Only**
```python
a = ['Hyd', 'Delhi', 'Mumbai']
a.sort()
print(a)  # Output: ['Delhi', 'Hyd', 'Mumbai']
```

#### ✅ **Fix 3: Sort Using a Custom Key (Convert All to Strings)**
```python
a = [25, 10.8, 'Hyd', True]
a.sort(key=str)
print(a)  # Output: [10.8, 25, True, 'Hyd'] (Sorted as strings)
```
-----------------------------------------------------------------------------------------------------------------------------------------
Here’s the **demo program** for the `count()` method in Python:
# Creating a list
a = [10, 20, 15, 18, 15, 12, 14, 15, 19]

# Counting occurrences of 15
print(a.count(15))  # Output: 3 (since 15 appears 3 times in the list)

# Counting occurrences of 25 (which is not in the list)
print(a.count(25))  # Output: 0 (since 25 is not in the list)

# Printing the total number of elements in the list
print(len(a))  # Output: 9 (total elements in the list)
```

---

### **Expected Output:**
```
3
0
9
```

---

### **Key Points About `count()` Method**
1. **What does `list.count(x)` do?**  
   - It **returns the number of times** `x` appears in the list.
   - If `x` is **not in the list**, it returns `0`.

2. **How does it compare to `len()`?**  
   - `count(x)` → Counts occurrences of a specific element.  
   - `len(list)` → Returns the **total number of elements** in the list.

---

### **Example with Strings:**
```python
b = ['apple', 'banana', 'cherry', 'apple', 'apple']
print(b.count('apple'))  # Output: 3
print(b.count('orange'))  # Output: 0
```
---------------------------------------------------------------------------------------------------------------------------------------------------
Here’s the **Python program** to remove all duplicate elements from the list, ensuring that even single occurrences are removed:
def remove_duplicates(lst):
    list = []  # List to store elements that appear only once
    for item in lst:
        if lst.count(item) == 1:  # If an element appears only once, keep it
            list.append(item)
    return list

# Example input
a = [10, 20, 15, 10, 14, 10, 18, 20, 19]

# Removing duplicate elements
result = remove_duplicates(a)

# Printing the output
print(result)  # Expected Output: [15, 14, 18, 19]

# Example input
a = [10, 20, 15, 10, 14, 10, 18, 20, 19]

# Removing duplicate elements
result = remove_duplicates(a)

# Printing the output
print(result)  # Expected Output: [15, 14, 18, 19]
```

---

### **Explanation:**
1. We **iterate through the list** and check the count of each element using `count()`.
2. If an element appears **exactly once**, we add it to `unique_list`.
3. We return and print `unique_list`, which contains only non-repeating elements.

---

### **Expected Output:**
```
[15, 14, 18, 19]
```
------------------------------------------------------------------------------------------------------------------------------------------
Your index() method demo program is well-structured! Here's a slightly improved version with proper exception handling:

a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
#     0    1    2    3    4    5    6    7    8    9    10

try:
    i = a.index(15)  # Get the first occurrence of 15
    while True:
        print(i)  # Print the index
        i = a.index(15, i + 1)  # Find the next occurrence of 15
except ValueError:  # Handle when index() can't find 15
    print(f'15 is found {a.count(15)} times')

---

### **Expected Output:**
```
2
5
8
15 is found 3 times
```

---

### **Key Learnings About `index()` Method:**
1. **`list.index(x)`** → Returns the index of the **first occurrence** of `x`.  
   - If `x` is **not found**, it raises a **ValueError**.
   
2. **`list.index(x, i)`** → Searches for `x` **starting from index `i`**.

3. **What happens when an element is not found?**  
   - It throws an exception, which is caught using `except ValueError`.

### **Additional Notes:**
1. **Four search methods in `str` class**:
   - `find()`
   - `rfind()`
   - `index()`
   - `rindex()`

2. **Single search method in `list` class**:
   - `index()`
   
-------------------------------------------------------------------------------------------------------------------------------
Here is a Python program to check if the first list is a sublist of the second list:
def is_sublist(first, second):
    try:
        start = 0
        for item in first:
            start = second.index(item, start) + 1  # Find index of item and move to next
        return True
    except ValueError:
        return False

# Test cases
print(is_sublist([2, 3, 4], [2, 2, 3, 4, 5]))  # True
print(is_sublist([2, 4, 4], [2, 2, 3, 4, 5]))  # False
print(is_sublist([2, 4, 3], [2, 2, 3, 4, 5]))  # False
print(is_sublist([2, 2, 5], [2, 2, 3, 4, 5]))  # True

### **Explanation:**
1. **Loop through each element in `first` list** and try to find it in `second` list **starting from the previous found index**.
2. **If an element is not found**, `index()` raises a `ValueError`, and we return `False`.
3. If all elements are found in order, return `True`.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
The `copy()` method creates a shallow copy of a list. Here's an explanation of the given program:

---

### **Expected Output:**
```python
[10, 20, 15, 18]  # b (copy of a)
False             # a is b (Different objects in memory)
True              # a == b (Same values)

[10, 20, 15, 18]  # c (copy using slicing)
False             # a is c (Different objects in memory)
True              # a == c (Same values)

[10, 20, 15, 18]  # d (reference to a)
True              # a is d (Same object in memory)
True              # a == d (Same values)
```

---

### **Explanation:**
1. `copy()` method creates a **new list** with the same elements, but a different memory location.
2. `[:]` (slicing) also creates a **new list** (same effect as `copy()`).
3. Assigning `d = a` does **not create a new list**, but instead, `d` just becomes another reference to `a`.

---

### **Alternative Ways to Copy a List:**
```python
b = a.copy()  # Using copy() method
c = a[:]      # Using slicing
d = list(a)   # Using list() constructor
e = a * 1     # Using multiplication
import copy
f = copy.deepcopy(a)  # Using deepcopy() for nested lists
```
-------------------------------------------------------------------------------------------------------------------------------
Here's a Python program to check whether all elements in a list are identical or not:  

```python
def check_identical(lst):
    if len(lst) == lst.count(lst[0]):  # Check if all elements are the same as the first element
        print("All the elements are identical")
    else:
        print("All the elements are not identical")

    print(f"Number of elements in the list: {len(lst)}")
    print(f"First element ({lst[0]}) is repeated {lst.count(lst[0])} times")

# Example Inputs
list1 = [25, 25, 25, 25]  
check_identical(list1)

print()

list2 = [10, 10, 20, 10]  
check_identical(list2)
```

### **Expected Output:**
```
All the elements are identical
Number of elements in the list: 4
First element (25) is repeated 4 times

All the elements are not identical
Number of elements in the list: 4
First element (10) is repeated 3 times
```

### **Explanation:**
1. **`len(lst) == lst.count(lst[0])`**
   - `lst.count(lst[0])` counts how many times the **first element** appears.
   - If this count is **equal to the length** of the list, all elements are identical.
   - Otherwise, the list contains different values.
------------------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to delete **all occurrences** of a given element from a list using the `remove()` method:  

```python
def remove_all_occurrences(lst, x):
    while x in lst:  # Keep removing until x is no longer in the list
        lst.remove(x)
    return lst

# Example Input
lst = [10, 20, 15, 18, 19, 15, 17, 20, 15, 14]
x = 15

# Function call
result = remove_all_occurrences(lst, x)

# Output the modified list
print(result)
```

### **Expected Output:**
```
[10, 20, 18, 19, 17, 20, 14]
```

### **Explanation:**
1. The `remove()` method **only removes the first occurrence** of the specified value.
2. Using a `while` loop, we keep calling `remove(x)` **until x is completely gone** from the list.
3. Finally, we return and print the updated list.
------------------------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to determine the **mode** of a list and delete all occurrences of a given element:

```python
from collections import Counter

# Function to find mode (most frequently occurring element)
def find_mode(lst):
    freq = Counter(lst)  # Count occurrences of each element
    mode = max(freq, key=freq.get)  # Find the element with max count
    return mode

# Function to remove all occurrences of a given element
def remove_all_occurrences(lst, x):
    return [item for item in lst if item != x]

# Example 1: Finding mode
lst1 = [10, 20, 15, 18, 10, 20, 15, 10, 20, 19, 10]
mode = find_mode(lst1)
print(f"Mode: {mode}")  # Expected Output: 10

# Example 2: Removing all occurrences of an element
lst2 = [15, 15, 15]
element_to_remove = 15
new_lst = remove_all_occurrences(lst2, element_to_remove)
print(f"List without {element_to_remove}'s: {new_lst}")  # Expected Output: []
```

### **Explanation:**
1. **Finding Mode:**
   - The `Counter` class is used to count occurrences of elements.
   - The mode is the element with the highest frequency.
  
2. **Removing All Occurrences:**
   - A **list comprehension** filters out occurrences of the given element.
   -------------------------------------------------------------------------------------------------------------------------------
   Here’s a Python program demonstrating **nested lists** and how to access elements within them:

```python
# Defining a nested list
a = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]

# Printing the entire list
print("Nested List:", a)

# Length of the outer list
print("Length of outer list:", len(a))  # Output: 3 (because there are 3 inner lists)

# Accessing inner lists
print("1st inner list:", a[0])
print("2nd inner list:", a[1])
print("3rd inner list:", a[2])

# Accessing specific elements
print("30:", a[0][2])  # 1st list, index 2
print("80:", a[1][3])  # 2nd list, index 3
print("100:", a[2][1]) # 3rd list, index 1
```

### **Explanation:**
1. **Nested List Definition**: The list `a` contains three inner lists.
2. **Accessing Inner Lists**:
   - `a[0]` gives the first list `[10, 20, 30, 40]`
   - `a[1]` gives the second list `[50, 60, 70, 80]`
   - `a[2]` gives the third list `[90, 100, 110, 120]`
3. **Accessing Specific Elements**:
   - `a[0][2]` → 30 (1st list, 3rd element)
   - `a[1][3]` → 80 (2nd list, 4th element)
   - `a[2][1]` → 100 (3rd list, 2nd element)
-------------------------------------------------------------------------------------------------------------------------------------------
Here’s how you can access and print the required values from the nested list:

```python
# Defining the nested list
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

# Printing the inner lists
print("1st inner list:", a[0])  
print("2nd inner list:", a[1])  
print("3rd inner list:", a[2])  

# Printing the number of elements in each inner list
print("Number of elements in 1st inner list:", len(a[0]))  
print("Number of elements in 2nd inner list:", len(a[1]))  
print("Number of elements in 3rd inner list:", len(a[2]))  
```

### **Expected Output:**
```
1st inner list: [10, 20]
2nd inner list: [30, 40, 50]
3rd inner list: [60, 70, 80, 90]
Number of elements in 1st inner list: 2
Number of elements in 2nd inner list: 3
Number of elements in 3rd inner list: 4
```

### **Explanation:**
- `a[0]` → First inner list `[10, 20]`
- `a[1]` → Second inner list `[30, 40, 50]`
- `a[2]` → Third inner list `[60, 70, 80, 90]`
- `len(a[0])` → 2 elements in the first inner list
- `len(a[1])` → 3 elements in the second inner list
- `len(a[2])` → 4 elements in the third inner list.
-------------------------------------------------------------------------------------------------------------------------------------------------
Here’s how you can print the nested list in different ways:  

```python
# Defining the nested list
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

# Printing the entire nested list
print('Nested list with print function:')
print(a)

# Printing each inner list without using indexes
print('Each inner list of outer list without indexes:')
for sublist in a:
    print(sublist)

# Printing elements in matrix style without using indexes
print('Elements in the form of matrix without using indexes:')
for sublist in a:
    for item in sublist:
        print(item, end=' ')
    print()

# Printing elements in matrix style using indexes
print('Elements in the form of matrix using indexes:')
for i in range(len(a)):  # Iterating through outer list
    for j in range(len(a[i])):  # Iterating through inner list
        print(a[i][j], end=' ')
    print()
```

### **Expected Output:**
```
Nested list with print function:
[[10, 20], [30, 40, 50], [60, 70, 80, 90]]

Each inner list of outer list without indexes:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]

Elements in the form of matrix without using indexes:
10 20 
30 40 50 
60 70 80 90 

Elements in the form of matrix using indexes:
10 20 
30 40 50 
60 70 80 90 
```

### **Explanation:**
- `print(a)` prints the entire nested list.
- Using a `for` loop, we print each inner list separately.
- Using a nested loop, we print the elements in a matrix format without using indexes.
- Using indexes (`a[i][j]`), we print elements in matrix form explicitly.
-----------------------------------------------------------------------------------------------------------------------------------------------------
Let's analyze the output of your code step by step.

### **Given Nested List:**
```python
a = [[10, 20], [30, 40], [50, 60], [70, 80]]

for x in a:
    print(x)  # Prints each inner list as it is

print()

for x, y in a:
    print(x, y, sep='...')  # Unpacks each inner list and prints values with '...' separator
```

### **Step-by-Step Execution:**

#### **First loop:**
```python
for x in a:
    print(x)
```
- Iterates through the nested list, printing each inner list as a whole.

#### **Second loop:**
```python
for x, y in a:
    print(x, y, sep='...')
```
- Since each inner list contains exactly **two elements**, Python unpacks them into `x` and `y`, then prints them separated by `'...'`.

---

### **Expected Output:**
```
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
```

---

### **Explanation:**
1. The first `for` loop prints each sublist as is.
2. The second `for` loop unpacks each inner list and prints the numbers with `'...'` as a separator.
------------------------------------------------------------------------------------------------------------------------------------------------------
Let's analyze the expected output step by step.

### **Given Nested List:**
```python
a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

for x in a:
    print(x)  # Prints each inner list as it is

print()

for x, y, z in a:
    print(x, y, z, sep='...')
```

---

### **Step-by-Step Execution:**

#### **First loop:**
```python
for x in a:
    print(x)
```
- Iterates through the nested list, printing each inner list as a whole.

#### **Second loop:**
```python
for x, y, z in a:
    print(x, y, z, sep='...')
```
- Since each inner list contains exactly **three elements**, Python unpacks them into `x`, `y`, and `z`, then prints them separated by `'...'`.

---

### **Expected Output:**
```
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
```

---

### **Explanation:**
1. The first `for` loop prints each sublist as is.
2. The second `for` loop unpacks each inner list into three variables and prints them with `'...'` as a separator.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Let's analyze the expected output step by step.

---

### **Given Nested List:**
```python
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

for x in a:
    print(x)  # Prints each inner list as it is

for x, y in a:
    print(x, y, sep='...')
```

---

### **Step-by-Step Execution:**

#### **First loop:**
```python
for x in a:
    print(x)
```
- Iterates through the nested list and prints each inner list as a whole.

##### **Output of first loop:**
```
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
```

---

#### **Second loop:**
```python
for x, y in a:
    print(x, y, sep='...')
```
- This loop **expects** each sublist to have exactly **two elements** because it tries to unpack each sublist into `x` and `y`.
- **Error occurs** when trying to unpack `[30, 40, 50]`, which has **three elements**, and `[60, 70, 80, 90]`, which has **four elements**.

---

### **Expected Output:**
```
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
```
**Followed by an error:**
```
ValueError: too many values to unpack (expected 2)
```

---

### **Why does the error occur?**
- `[10, 20]` → ✅ Unpacks correctly as `x = 10`, `y = 20`
- `[30, 40, 50]` → ❌ **Error** (Too many values, expected only 2)
- `[60, 70, 80, 90]` → ❌ **Error** (Too many values)

---

### **How to Fix the Error?**
If you want to avoid the error, you can either:
1. **Ensure all sublists have exactly 2 elements** OR
2. **Use slicing or a different loop to handle lists of varying lengths**.

---
------------------------------------------------------------------------------------------------------------------------------------------------
Let's analyze the expected outputs.

---

### **Given Nested List:**
```python
a = [[]]
```
Here, `a` is a nested list with **one inner empty list**.

---

### **Printing the Inner List**
#### **Method 1: Direct Indexing**
```python
print(a[0])
```
- `a[0]` refers to the first (and only) inner list inside `a`.
- Since the inner list is empty, it prints:
```
[]
```

#### **Method 2: Using a Loop**
```python
for inner in a:
    print(inner)
```
- This loop iterates over `a`, which contains **one empty list**.
- It prints:
```
[]
```

---

### **Expected Output**
```
[]
[]
```
(Since both methods print the same empty inner list.)

---
-----------------------------------------------------------------------------------------------------------------------
Let's analyze the expected outputs for the given program.

---

### **Given Nested List:**
```python
a = [[10, 'Rama', 1000.0], 
     [20, 'Sita', 2000.0], 
     [15, 'Rajesh', 3500.0], 
     [18, 'Kiran', 2800.0], 
     [5, 'Amar', 5000.0]]
```
Each inner list contains:
1. A number (probably an ID or age)
2. A string (name)
3. A float (salary or some numerical value)

---

### **Understanding `sorted(a)`**
- **Sorting is done based on the first element of each inner list (numeric values).**
- The default behavior of `sorted()` arranges elements in **ascending order**.

#### **Sorted List:**
```
[
    [5, 'Amar', 5000.0],  
    [10, 'Rama', 1000.0],  
    [15, 'Rajesh', 3500.0],  
    [18, 'Kiran', 2800.0],  
    [20, 'Sita', 2000.0]
]
```

---

### **Understanding `sorted(a, reverse=True)`**
- This sorts in **descending order** based on the first element.

#### **Reverse Sorted List:**
```
[
    [20, 'Sita', 2000.0],  
    [18, 'Kiran', 2800.0],  
    [15, 'Rajesh', 3500.0],  
    [10, 'Rama', 1000.0],  
    [5, 'Amar', 5000.0]
]
```

---

### **Understanding `print(a)`**
- The `sorted()` function returns a **new sorted list** but **does not modify `a`**.
- So, when printing `a`, it remains **unchanged**:
```
[
    [10, 'Rama', 1000.0],  
    [20, 'Sita', 2000.0],  
    [15, 'Rajesh', 3500.0],  
    [18, 'Kiran', 2800.0],  
    [5, 'Amar', 5000.0]
]
```

---

### **Final Output**
```
[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]

[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]

[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
```

---

### **Key Takeaways**
- `sorted(a)` sorts by the **first element** of each sublist.
- `sorted(a, reverse=True)` sorts in **descending order**.
- `a` remains **unchanged** after using `sorted()`.
------------------------------------------------------------------------------------------------------------------------------------
You can use **list comprehension** to generate a list of cubes of the numbers **2, 4, 6, 8, and 10** as follows:

### **Python Program:**
```python
cubes = [x**3 for x in [2, 4, 6, 8, 10]]
print(cubes)
```

### **Output:**
```
[8, 64, 216, 512, 1000]
```

### **Explanation:**
- The list comprehension `[x**3 for x in [2, 4, 6, 8, 10]]` calculates the **cube** of each element in the given list.
- `x**3` raises each number to the power of 3.

This is a short and efficient way to generate the required list!
----------------------------------------------------------------------------------------------------------------------------------------
### **Python Program (Without List Comprehension)**
```python
cities = ['hyd', 'pune', 'chennai', 'vijayawada']
first_chars = []

for city in cities:
    first_chars.append(city[0].upper())

print(first_chars)
```

### **Output:**
```
['H', 'P', 'C', 'V']
```

### **Explanation:**
1. We initialize an empty list `first_chars`.
2. We iterate through each city name in the `cities` list.
3. For each city, we extract the first character (`city[0]`) and convert it to uppercase using `upper()`.
4. We append the capitalized character to `first_chars`.
5. Finally, we print the result.

Let me know if you need a list comprehension version too! 
---------------------------------------------------------------------------------------------------------------------
### **Python Program (With List Comprehension)**
```python
cities = ['hyd', 'pune', 'chennai', 'vijayawada']
first_chars = [city[0].upper() for city in cities]

print(first_chars)
```

### **Output:**
```
['H', 'P', 'C', 'V']
```

### **Explanation:**
- This program uses **list comprehension** to extract the first character of each string in the `cities` list and convert it to uppercase in a single line.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
### **Python Program (Without List Comprehension)**
```python
sentence = "hyd is green city"
words = sentence.split()  # Splitting the sentence into words
result = []  # Empty list to store word and its length

for word in words:
    result.append([word.upper(), len(word)])  # Append word in uppercase and its length

print(result)
```

### **Output:**
```
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
```

### **Explanation:**
1. **`split()`** → Splits the sentence into words: `['hyd', 'is', 'green', 'city']`
2. **Loop through words** and:
   - Convert each word to uppercase using **`upper()`**.
   - Get its length using **`len()`**.
   - Append as a list `[word, length]` to `result`.
--------------------------------------------------------------------------------------------------------------------------------------------------
### **Python Program (With List Comprehension)**
```python
sentence = "hyd is green city"
result = [[word.upper(), len(word)] for word in sentence.split()]
print(result)
```

### **Output:**
```
[['HYD', 3], ['IS', 2], ['GREEN', 5], ['CITY', 4]]
```

### **Explanation:**
- **`sentence.split()`** → Splits the sentence into words.
- **List comprehension** iterates over each word:
  - Converts it to **uppercase** using `upper()`.
  - Finds its **length** using `len()`.
  - Stores them in a **nested list**.

This method is more concise than the previous one. 
-------------------------------------------------------------------------------------------------------------------------------------------------------
### **Python Program to Add Two Lists of Unequal Length (Without Comprehension)**
```python
list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [100, 200, 300, 400]

result = []
min_length = min(len(list1), len(list2))

for i in range(min_length):
    result.append(list1[i] + list2[i])

print(result)
```

### **Output:**
```
[110, 220, 330, 440]
```

### **Explanation:**
- The program finds the **minimum length** between the two lists.
- It iterates only up to that length and adds corresponding elements.
- The extra elements in the longer list are **ignored** (not included in the result).
-----------------------------------------------------------------------------------------------------------------------------------------------
### **Python Program to Initialize a Nested List with Zeroes (Without Comprehension)**  
```python
# Inputs: Number of rows and columns
rows = 3
cols = 4

# Initializing the nested list with zeroes using the repetition operator
nested_list = []
for _ in range(rows):
    nested_list.append([0] * cols)

print(nested_list)
```

### **Output:**  
```
[[0, 0, 0, 0],  
 [0, 0, 0, 0],  
 [0, 0, 0, 0]]
----------------------------------------------------------------------------------------------------------------------------------
Here's the Python program using list comprehension to initialize a nested list with zeroes:  

```python
# Taking user input for the number of lists and elements in each list
rows = int(input("How many lists? : "))
cols = int(input("How many elements in each list? : "))

# Using list comprehension to create the nested list
nested_list = [[0] * cols for _ in range(rows)]

# Printing the result
print(nested_list)
```

### **Example Run:**
```
How many lists? : 3
How many elements in each list? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
```
--------------------------------------------------------------------------------------------------------------------------------
Here's the Python program to extract elements from the first list that are not in the second list, without using list comprehension:

```python
# Given lists
list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

# Creating an empty list to store the result
result = []

# Iterating through elements of list1
for item in list1:
    if item not in list2:  # Checking if the element is not in list2
        result.append(item)

# Printing the result
print(result)
```

### **Expected Output:**
```
[20, 18, 32]
```
-------------------------------------------------------------------------------------------------------------------------------
Here's the program using list comprehension:  

```python
# Given lists
list1 = [10, 20, 15, 18, 25, 32]
list2 = [30, 40, 10, 25, 15]

# List comprehension to filter elements of list1 not in list2
result = [item for item in list1 if item not in list2]

# Printing the result
print(result)
```

### **Expected Output:**
```
[20, 18, 32]
```
------------------------------------------------------------------------------------------------------------------------------
Here's the Python program using list comprehension to print even numbers between 1 and 20:  

```python
# List comprehension to generate even numbers between 1 and 20
even_numbers = [num for num in range(1, 21) if num % 2 == 0]

# Printing the result
print("Even numbers between 1 and 20:", even_numbers)
```

### **Expected Output:**
```
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
------------------------------------------------------------------------------------------------------------------------------------------------------
You can generate even numbers between 1 and 20 using list comprehension without an `if` condition by modifying the `range()` function to step by 2:  

```python
# List comprehension without using if
even_numbers = [num for num in range(2, 21, 2)]

# Printing the result
print("Even numbers between 1 and 20:", even_numbers)
```

### **Expected Output:**
```
Even numbers between 1 and 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
------------------------------------------------------------------------------------------------------------------------------------------------------------
You can generate squares of numbers from 1 to 20 that are divisible by 2 using list comprehension like this:

```python
# List comprehension to generate squares divisible by 2
squares = [num**2 for num in range(1, 21) if (num**2) % 2 == 0]

# Printing the result
print("Squares divisible by 2:", squares)
```

### **Expected Output:**
```
Squares divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```
--------------------------------------------------------------------------------------------------------------------------------
You can generate the required squares **without using `if`** by only squaring even numbers from the range:

```python
# List comprehension without using if
squares = [num**2 for num in range(2, 21, 2)]

# Printing the result
print("Squares divisible by 2:", squares)
```

### **Expected Output:**
```
Squares divisible by 2: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

This avoids the `if` condition by directly iterating over even numbers. 
----------------------------------------------------------------------------------------------------------------------------------
Here’s the Python program using **nested for loops** to add each element of the first list with all elements of the second list **without using list comprehension**:

### **Python Program:**
```python
# Given lists
list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

# Empty list to store results
result = []

# Nested loops to add each element of list1 with each element of list2
for x in list1:
    for y in list2:
        result.append(x + y)

# Printing the result
print("Result:", result)
```

### **Expected Output:**
```
Result: [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
```

Each element of `list1` is added to every element of `list2`, and the sum is stored in `result`. 
----------------------------------------------------------------------------------------------------------------
Here’s the Python program using **list comprehension** to achieve the same result:  

### **Python Program:**
```python
# Given lists
list1 = [10, 20, 15]
list2 = [30, 40, 35, 32]

# List comprehension to add each element of list1 with all elements of list2
result = [x + y for x in list1 for y in list2]

# Printing the result
print("Result:", result)
```

### **Expected Output:**
```
Result: [40, 50, 45, 42, 50, 60, 55, 52, 45, 55, 50, 47]
```

This is the **comprehension version** of the previous program, making it more compact and efficient. 
--------------------------------------------------------------------------------------------------------------------
Here's the Python program using **list comprehension** to concatenate each character of the first string with every character of the second string:

### **Python Program:**
```python
# Given strings
str1 = "HYD"
str2 = "PUNE"

# List comprehension to concatenate each character of str1 with every character of str2
result = [x + y for x in str1 for y in str2]

# Printing the result
print("Result:", result)
```

### **Expected Output:**
```
Result: ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
```

This program efficiently combines characters using a **nested loop inside list comprehension** to create all possible pairs. 
----------------------------------------------------------------------------------------------------------------------------------------
Here's a Python program to convert a **nested list** into a **flat list** without using list comprehension:

### **Python Program:**
```python
# Given nested list
nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

# Flattening the list using a for loop
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

# Printing the result
print("Flattened List:", flat_list)
```

### **Expected Output:**
```
Flattened List: [10, 20, 30, 40, 50, 60, 70, 80, 90]
```

### **Explanation:**
- The **outer loop** iterates through each inner list.
- The **inner loop** iterates through elements of the inner list and adds them to `flat_list`.

This approach **does not use list comprehension** and effectively flattens the nested list! 
----------------------------------------------------------------------------------------------------------
Here's a Python program to **flatten a nested list using list comprehension**:

### **Python Program:**
```python
# Given nested list
nested_list = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

# Flattening the list using list comprehension
flat_list = [item for sublist in nested_list for item in sublist]

# Printing the result
print("Flattened List:", flat_list)
```

### **Expected Output:**
```
Flattened List: [10, 20, 30, 40, 50, 60, 70, 80, 90]
```

### **Explanation:**
- The **outer loop** (`for sublist in nested_list`) iterates through each inner list.
- The **inner loop** (`for item in sublist`) extracts elements and adds them directly to `flat_list`.

This **one-liner list comprehension** replaces the **nested for loops** and achieves the same result efficiently! 
------------------------------------------------------------------------------------------------------------------------
Let's analyze the given list comprehension:

```python
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
b = [x for x in a for y in x]
print(b)
```

### **Step-by-Step Execution:**
1. The outer loop: `for x in a` → iterates through each sublist.
   - `x = [10, 20]`
   - `x = [30, 40, 50]`
   - `x = [60, 70, 80, 90]`
   
2. The inner loop: `for y in x` → iterates through each element of `x`, but **does nothing with `y`**, meaning `x` itself gets added to `b` multiple times.

### **How It Expands:**
This list comprehension is equivalent to:

```python
b = []
for x in a:
    for y in x:  # This loop runs but does nothing specific
        b.append(x)  # The entire sublist 'x' is appended multiple times
```

### **Final Output:**
Since each sublist `x` is appended as many times as its number of elements:

- `[10, 20]` → appended **2 times**
- `[30, 40, 50]` → appended **3 times**
- `[60, 70, 80, 90]` → appended **4 times**

#### **So, the final list `b` will be:**
```python
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], 
 [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
```

### **Key Takeaway:**
- This comprehension doesn't **flatten** the list but **repeats the inner lists** based on their number of elements.
- If the goal is to flatten the list, the correct approach should be:
  ```python
  b = [y for x in a for y in x]
  ```
  **Output:**
  ```
  [10, 20, 30, 40, 50, 60, 70, 80, 90]
  ```
-------------------------------------------------------------------------------------------------------------------------------
Let's analyze the nested list comprehension:

```python
a = [[j for j in range(i)] for i in range(5)]
print(a)
```

### **Step-by-Step Execution:**

#### **Outer Loop:** `for i in range(5)`
- `i` takes values: `0, 1, 2, 3, 4`

#### **Inner Loop:** `for j in range(i)`
- Generates a list of numbers from `0` to `i-1` for each `i`

### **How It Expands:**

| `i`  | `range(i)`  | Inner List (`[j for j in range(i)]`) |
|------|------------|--------------------------------------|
| `0`  | `range(0)` → `[]`  | `[]` |
| `1`  | `range(1)` → `[0]` | `[0]` |
| `2`  | `range(2)` → `[0,1]` | `[0, 1]` |
| `3`  | `range(3)` → `[0,1,2]` | `[0, 1, 2]` |
| `4`  | `range(4)` → `[0,1,2,3]` | `[0, 1, 2, 3]` |

### **Final Output:**
```python
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
```

### **Key Takeaways:**
- This creates a **nested list**, where each inner list contains numbers from `0` to `i-1`.
- The first inner list (`i=0`) is empty because `range(0)` produces no numbers.
- This pattern generates a **triangular** structure of numbers.
-----------------------------------------------------------------------------------------------------------------------------
Here’s a Python program to merge two sorted lists into another sorted list.

### **Approach:**
- Use two pointers to traverse both lists.
- Compare elements at both pointers and append the smaller one to the result list.
- If any elements remain in either list, append them at the end.

### **Python Code:**
```python
def merge_sorted_lists(a, b):
    i, j = 0, 0
    c = []
    
    # Traverse both lists
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    # Append remaining elements from a (if any)
    while i < len(a):
        c.append(a[i])
        i += 1
    
    # Append remaining elements from b (if any)
    while j < len(b):
        c.append(b[j])
        j += 1

    return c

# Example input
a = [10, 20, 30, 40, 50]
b = [5, 12, 20, 37]

# Merging the lists
c = merge_sorted_lists(a, b)
print("Merged Sorted List:", c)
```

### **Output:**
```
Merged Sorted List: [5, 10, 12, 20, 20, 30, 37, 40, 50]
```

#### **Alternative Approach:**
If you don't want to use a manual merging approach, you can simply use:
```python
c = sorted(a + b)
```
This works but is **less efficient** than the two-pointer method.
