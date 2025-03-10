Here's the Python program to print distinct vowels of the string *without using set*:
def distinct_vowels(s):
    vowels = "AEIOUaeiou"  # Vowel characters (both uppercase and lowercase)
    found_vowels = ""  # String to store distinct vowels
    
    for char in s:
        upper_char = char.upper()  # Convert to uppercase for uniformity
        if upper_char in vowels and upper_char not in found_vowels:
            found_vowels += upper_char  # Append if not already in the result
    
    return found_vowels

# Example usage
input_str = "RaMA rAo"
output = distinct_vowels(input_str)
print(output)  # Expected Output: AO


### Explanation:
1. Convert each character to uppercase (upper()) to handle case insensitivity.
2. Check if the character is a vowel.
3. If the vowel is not already in found_vowels, append it.
4. Print the result.

### Output for "RaMA rAo": AO
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Here's the modified program using the *walrus operator (:=)*:

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1  # Initialize index

while (index := a.find('is', index + 1)) != -1:  
    print(index)

print('End')


### Explanation:
1. The walrus operator (:=) allows assigning and checking index in the same expression.
2. index := a.find('is', index + 1):
   - Finds the next occurrence of 'is' starting from index + 1.
   - Updates index in the same step.
3. The loop continues until find() returns -1 (no more occurrences).

### Output:

4
22
40
End
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)
Syntax  is  same  as   find()  method
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Here’s the modified program using the *rfind()* method:

### *Modified Code using rfind()*:
python
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = len(a)  # Start from the end of the string

while (index := a.rfind('is', 0, index)) != -1:  
    print(index)

print('End')


---

### *Explanation:*
1. *rfind('is', 0, index)*:
   - Starts searching from the right (index-1) towards the left (0).
   - Finds the last occurrence first, then moves left.
   
2. *Loop until rfind() returns -1*:
   - Keeps updating index to find occurrences from right to left.

---

### *Output:*

40
22
4
End


This correctly finds the occurrences of "is" from *right to left, unlike find(), which searches **left to right*.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Here’s the modified program using the *rindex()* method with try-except:  

### *Modified Code using rindex()*:
python
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = len(a)  # Start from the end of the string

try:
    while True:
        index = a.rindex('is', 0, index)  # Find 'is' from right to left
        print(index)
except ValueError:  # Raised when 'is' is not found
    print('End')


---

### *Explanation:*
1. *rindex('is', 0, index)*:
   - Similar to rfind(), but *raises ValueError if not found* instead of returning -1.
   - Searches from index-1 back to 0 (right to left).
   
2. *try-except*:
   - *Keeps finding occurrences* of "is" from right to left.
   - *When no more occurrences exist*, rindex() raises a ValueError, which stops the loop.

---

### *Output:*

40
22
4
End


This is functionally the same as rfind(), except it *throws an error instead of returning -1* when the substring is missing.
--------------------------------------------------------------------------------------------------------------------------------------------------
program  demonstrates the usage of the `count()` method in Python. 
```
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a.count('is'))        # Counts occurrences of 'is' in the entire string
print(a.count('is', 19, 48)) # Counts occurrences of 'is' from index 19 to 47
print(a.count('was'))       # Counts occurrences of 'was' (which is not present, so returns 0)
```

### Explanation:
1. `a.count('is')`  
   - Counts how many times `"is"` appears in the whole string.  
   - Output: `3`
   
2. `a.count('is', 19, 48)`  
   - Counts `"is"` only within the substring `a[19:48]`.  
   - Output: `2`

3. `a.count('was')`  
   - `"was"` is not in the string, so it returns `0`.  
   - Output: `0`

### Output:
3
2
0
----------------------------------------------------------------------------------------------------------------------------------------------------
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a.count(' '))   # Counts occurrences of space (' ')
print(a.count('\t'))  # Counts occurrences of tab ('\t')
print(a.count('\n'))  # Counts occurrences of newline ('\n')
```

### Breakdown:
The given string is:
```
'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
```
It contains:
- Spaces (`' '`) → 3 occurrences (`between words like "Hyd is", "Hyd is", and "Hyd is"`)
- Tabs (`'\t'`) → 3 occurrences (`before "green", "hitec", and "his"`)
- Newlines (`'\n'`) → 3 occurrences (`before "city.Hyd", "city.Hyd", and "city"`)

### Output:
3
3
3
example:
Here's a Python program to replace all occurrences of the second character in a string (except the first occurrence) with `'*'`:  

# Get user input
s = input("Enter any string: ")

# Check if the string has at least two characters
if len(s) > 1:
    first_char = s[0]
    second_char = s[1]
    
    # Replace all occurrences of second character (except the first one)
    modified_string = first_char + second_char + s[2:].replace(second_char, '*')
    
    print("Result:", modified_string)
else:
    print("String is too short to process.")
```

### **Explanation:**  
For the input `"babble"`,  
- The second character is `'a'`.  
- Replace all occurrences of `'a'` in the rest of the string with `'*'`.  

### **Output:**  
```
Enter any string: babble
Result: ba**le
                   (or)

# Get user input
s = input("Enter any string: ")

# Check if the string is not empty
if len(s) > 0:
    first_char = s[0]  # Get the first character
    
    # Replace every occurrence of the first character (except the first one) with '*'
    modified_string = first_char + s[1:].replace(first_char, '*')
    
    print("Result:", modified_string)
else:
    print("String is empty.")
```

### **Explanation:**  
For input `"babble"`:  
- The first character is `'b'`.  
- Replace every `'b'` after the first occurrence with `'*'`.  
- `"babble"` → `"ba**le"`  
### **Expected Output:**  
Enter any string: babble
Result: ba**le
------------------------------------------------------------------------------------------------------------------------------------------------------
a = '15:36:48'
print(a.split(':'))  # Splits the string at each occurrence of ':'
print(a)  # Prints the original string
### **Explanation:**
1. **`a.split(':')`**
   - The `split(':')` method splits the string `a` wherever `':'` appears.
   - The result is a list of substrings.
   - `'15:36:48'` → `['15', '36', '48']`

2. **`print(a)`**
   - Since `split()` does not modify the original string, printing `a` will still output `'15:36:48'`.

### **Expected Output:**
['15', '36', '48']
15:36:48
------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 'Hyd\nis green\tcity'

print(a.split(' '))     # Splits the string at each space (' ')
print(a.split())        # Splits at any whitespace (spaces, tabs, newlines)
print(a.split('green')) # Splits the string at 'green'
print(a.split(''))      # This will cause an error

### **Explanation & Output:**

1. **`a.split(' ')`**  
   - Splits the string at **each space (`' '`)**, keeping other whitespace (like `\n` and `\t`) as part of the split elements.
   - `'Hyd\nis green\tcity'` → `['Hyd\nis', 'green\tcity']`  
   - **Output:**  
     ```
     ['Hyd\nis', 'green\tcity']
     ```

2. **`a.split()`**  
   - When `.split()` is used **without arguments**, it splits at **any whitespace** (spaces, tabs `\t`, newlines `\n`).
   - `'Hyd\nis green\tcity'` → `['Hyd', 'is', 'green', 'city']`
   - **Output:**  
     ```
     ['Hyd', 'is', 'green', 'city']
     ```

3. **`a.split('green')`**  
   - Splits the string at `'green'`, removing it and creating two substrings.
   - `'Hyd\nis green\tcity'` → `['Hyd\nis ', '\tcity']`
   - **Output:**  
     ```
     ['Hyd\nis ', '\tcity']
     ```

4. **`a.split('')`**  
   - This **raises an error** (`ValueError: empty separator`) because the `split()` method **does not accept an empty string** as a separator.
   - **Output:**  
     ```
     ValueError: empty separator
     ```

---

### **Final Expected Output:**
```
['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']
ValueError: empty separator
```
----------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 'Hyd\tis\tgreen\tcity'  # There is a tab (\t) between words

print(a.split('\t'))  # Splits at each tab character
print(a.split())      # Splits at any whitespace (spaces, tabs, newlines)
print(a.split(' '))   # Splits at spaces (but there are no spaces in 'a')

### **Explanation & Expected Output:**

1. **`a.split('\t')`**  
   - This splits the string at each **tab (`\t`)** character.
   - The string `'Hyd\tis\tgreen\tcity'` gets split into `['Hyd', 'is', 'green', 'city']`.  
   - **Output:**  
     ```
     ['Hyd', 'is', 'green', 'city']
     ```

2. **`a.split()`**  
   - When `.split()` is used **without arguments**, it splits at **any whitespace**, including spaces and tabs.
   - The string contains **tabs (`\t`)**, so it splits at those.
   - Output is the same as `split('\t')` in this case.
   - **Output:**  
     ```
     ['Hyd', 'is', 'green', 'city']
     ```

3. **`a.split(' ')`**  
   - This attempts to split the string at spaces (`' '`), **but there are no spaces** in `a`, only tabs (`\t`).
   - Since there are **no spaces to split on**, the entire string remains unchanged inside a single-element list.
   - **Output:**  
     ```
     ['Hyd\tis\tgreen\tcity']
     ```

---

### **Final Expected Output:**
```
['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']
```
---------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 'Hyd   is   green   city'  # There are 3 spaces between words

print(a.split())      # Splits at any whitespace (spaces, tabs, newlines)
print(a.split(' '))   # Splits at each space (' ')

### **Explanation & Expected Output:**

1. **`a.split()`**  
   - When `.split()` is used **without arguments**, it automatically removes **extra** spaces and splits at **any whitespace sequence** (including multiple spaces, tabs, and newlines).
   - `'Hyd   is   green   city'` → `['Hyd', 'is', 'green', 'city']`
   - **Output:**  
     ```
     ['Hyd', 'is', 'green', 'city']
     ```

2. **`a.split(' ')`**  
   - This explicitly splits **at each space (`' '`)**, meaning it **does not remove extra spaces**.
   - Multiple spaces between words create **empty string elements (`''`)** in the list.
   - `'Hyd   is   green   city'` → `['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']`
   - **Output:**  
     ```
     ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
     ```
### **Final Expected Output:**
```
['Hyd', 'is', 'green', 'city']
['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 'www.gmail.com'
print(a.split('.'))  # Splitting at '.'

### **Explanation & Expected Output:**
- The `.split('.')` method splits the string at each occurrence of `'.'`.
- The given string is `'www.gmail.com'`, so it will be split into parts:
  - `'www'`
  - `'gmail'`
  - `'com'`

- **Output:**
  ```
  ['www', 'gmail', 'com']
  ```
---

### **Final Expected Output:**
```
['www', 'gmail', 'com']
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get user input
expr = input("Enter an expression containing only '+' symbols: ")

# Split the input string at '+' and convert each part to an integer
numbers = expr.split('+')
sum_result = sum(map(int, numbers))  # Convert to int and sum

# Print the result
print("Result:", sum_result)

### **Explanation:**  
1. The `input()` function takes an arithmetic expression as a string (e.g., `"3+2+4+5+6"`).  
2. The `.split('+')` method splits the string into a list of numbers as strings (e.g., `['3', '2', '4', '5', '6']`).  
3. `map(int, numbers)` converts each string in the list into an integer.  
4. `sum()` adds all the numbers together.  
5. The final sum is printed.

### **Example Run:**  
```
Enter an expression containing only '+' symbols: 3+2+4+5+6+21+4+5+8+12
Result: 70
```
Enter the expression: 23+456+7
Sum:  486
Yes! If the input is:  
```
Enter the expression: 23+456+7
```
Then the program will split the string `"23+456+7"` at the `'+'` symbol, convert each part to an integer, and sum them up:  

```
23 + 456 + 7 = 486
```

### **Final Output:**
```
Sum: 486
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

a = ['15', '36', '48']
print(':'.join(a))  
```
- `join()` concatenates the elements of the list using `':'` as a separator.
- **Output:**  
  ```
  15:36:48
  ```

---

b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))
```
- `join()` works on tuples just like lists.
- **Output:**  
  ```
  Hyd is green city
  ```

---

```
c = {'10', '20', '15', '25', '52'}
print(','.join(c))
```
- `join()` works on sets as well, but **sets are unordered**, so the output order may vary.
- Possible **Output:**  
  ```
  10,20,15,25,52
  ```  
  (Order might change due to the nature of sets.)

---

```
d = ['www', 'gmail', 'com']
print('.'.join(d))
```
- `join()` concatenates the elements using `'.'`.
- **Output:**  
  ```
  www.gmail.com
  ```

---

```
e = [15, 36, 48]
print(':'.join(e))
```
- **Error!**  
  - `join()` only works with strings, but the list contains **integers**.
  - **Output:**  
    ```
    TypeError: sequence item 0: expected str instance, int found
    ```
  - To fix this, convert integers to strings:
    ```python
    print(':'.join(map(str, e)))
    ```
    - Output:  
      ```
      15:36:48
      ```

---

```
f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))
```
- `join()` with an empty separator (`''`) simply concatenates the strings.
- **Output:**  
  ```
  SankarDayalSarma
  ```

---

```
g = range(5)
print('-'.join(g))
```
- **Error!**  
  - `join()` requires **strings**, but `range(5)` produces **integers** (`0, 1, 2, 3, 4`).
  - **Output:**  
    ```
    TypeError: sequence item 0: expected str instance, int found
    ```
  - To fix this, convert numbers to strings:
    ```python
    print('-'.join(map(str, g)))
    ```
    - Output:  
      ```
      0-1-2-3-4
      ```

---

### **Final Expected Output:**
```
15:36:48
Hyd is green city
10,20,15,25,52  (order may vary)
www.gmail.com
TypeError: sequence item 0: expected str instance, int found
SankarDayalSarma
TypeError: sequence item 0: expected str instance, int found
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------
a = 'Hyd is green city'

print(a.endswith('city'))      # Checks if the string ends with 'city'
print(a.endswith('town'))      # Checks if the string ends with 'town'
print(a.endswith('green', 3, 12))  # Checks if substring from index 3 to 12 ends with 'green'
print(a.endswith('green', 3, 13))  # Checks if substring from index 3 to 13 ends with 'green'
print(a.endswith(' ', 3, 13))      # Checks if substring from index 3 to 13 ends with ' '
```

---

### **Explanation & Expected Output:**

1. **`a.endswith('city')`**
   - The string is **`'Hyd is green city'`**, which **ends with** `'city'`.
   - **Output:**
     ```
     True
     ```

2. **`a.endswith('town')`**
   - The string **does not** end with `'town'`.
   - **Output:**
     ```
     False
     ```

3. **`a.endswith('green', 3, 12)`**
   - `a[3:12]` → `' is gree'`
   - `' is gree'` **does not** end with `'green'`.
   - **Output:**
     ```
     False
     ```

4. **`a.endswith('green', 3, 13)`**
   - `a[3:13]` → `' is green'`
   - `' is green'` **ends with** `'green'`.
   - **Output:**
     ```
     True
     ```

5. **`a.endswith(' ', 3, 13)`**
   - `a[3:13]` → `' is green'`
   - `' is green'` **ends with a space (`' '`)**.
   - **Output:**
     ```
     True
     ```

---

### **Final Expected Output:**
```
True
False
False
True
True
```
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get user input
word = input("Enter a word: ")

# Check the conditions
if len(word) < 3:
    result = word  # Leave unchanged if length is less than 3
elif word.endswith("ing"):
    result = word + "ly"  # Append 'ly' if word ends with 'ing'
else:
    result = word + "ing"  # Append 'ing' otherwise

# Print the result
print("Output:", result)
```

---

### **Explanation & Expected Outputs:**

| **Input**      | **Condition Check**                 | **Output**         |
|---------------|----------------------------------|------------------|
| `"interest"`  | Does not end with `"ing"`, append `"ing"` | `"interesting"` |
| `"interesting"` | Ends with `"ing"`, append `"ly"` | `"interestingly"` |
| `"Hi"`        | Length is `< 3`, unchanged       | `"Hi"` |

---

### **Example Runs:**
#### **Case 1:**
```
Enter a word: interest
Output: interesting
```

#### **Case 2:**
```
Enter a word: interesting
Output: interestingly
```

#### **Case 3:**
```
Enter a word: Hi
Output: Hi
```

This program correctly implements the required logic using the `endswith()` method. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
print('Hyd'.isalpha())       # True
print('Rama Rao'.isalpha())  # False (contains space)
print('Hyd4'.isalpha())      # False (contains digit '4')
print('Hyd$'.isalpha())      # False (contains special character '$')
print('9247'.isalpha())      # False (only digits, no alphabets)
print('+-$'.isalpha())       # False (only special characters, no alphabets)
print('A2#'.isalpha())       # False (contains digit '2' and special character '#')
print(''.isalpha())          # False (empty string)
print(' '.isalpha())         # False (only space, no alphabets)
```

---

### **Explanation & Expected Output:**

| **String**    | **Contains only alphabets?** | **Output**  |
|--------------|------------------------------|------------|
| `'Hyd'`       | ✅ Yes                        | `True`     |
| `'Rama Rao'`  | ❌ No (contains space)        | `False`    |
| `'Hyd4'`      | ❌ No (contains digit `4`)    | `False`    |
| `'Hyd$'`      | ❌ No (contains `$`)          | `False`    |
| `'9247'`      | ❌ No (only digits)           | `False`    |
| `'+-$'`       | ❌ No (only special chars)    | `False`    |
| `'A2#'`       | ❌ No (contains `2` and `#`) | `False`    |
| `''` (empty)  | ❌ No characters at all       | `False`    |
| `' '` (space) | ❌ No alphabets               | `False`    |

---

### **Final Expected Output:**
```
True
False
False
False
False
False
False
False
False
```

---

### **Key Takeaways:**
- `.isalpha()` returns **`True`** only if **all** characters in the string are alphabets (A-Z, a-z).
- It returns **`False`** if the string contains:
  - Spaces
  - Digits
  - Special characters
  - Is empty (`''`)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# isdigit()  method  demo  program  
print('9247'.isdigit())   # True
print('92a47'.isdigit())  # False (contains 'a')
print('92$47'.isdigit())  # False (contains '$')
print('Hyd'.isdigit())    # False (only alphabets)
print('+-$'.isdigit())    # False (only special characters)
print('A2#'.isdigit())    # False (contains 'A' and '#')
print(''.isdigit())       # False (empty string)
print(' '.isdigit())      # False (contains only space)
print(9247.isdigit())     # ❌ Error! Integers don't have isdigit() method
```

---

### **Explanation & Expected Output:**

| **String**   | **Contains only digits?** | **Output**  |
|-------------|--------------------------|------------|
| `'9247'`     | ✅ Yes                    | `True`     |
| `'92a47'`    | ❌ No (`a` is not a digit) | `False`    |
| `'92$47'`    | ❌ No (`$` is not a digit) | `False`    |
| `'Hyd'`      | ❌ No (only alphabets)     | `False`    |
| `'+-$'`      | ❌ No (only special chars) | `False`    |
| `'A2#'`      | ❌ No (contains `A` and `#`) | `False` |
| `''` (empty) | ❌ No characters           | `False`    |
| `' '` (space)| ❌ No digits, only space   | `False`    |
| `9247.isdigit()` | ❌ **Error** (integers don't have `.isdigit()`) | `AttributeError` |

---

### **Final Expected Output:**
```
True
False
False
False
False
False
False
False
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
AttributeError: 'int' object has no attribute 'isdigit'
```

---

### **Fix for the Last Line:**
- The error happens because `.isdigit()` **only works on strings**.
- To fix it, convert the number to a string first:
  ```python
  print(str(9247).isdigit())  # Output: True
  ```

---

### **Key Takeaways:**
- `.isdigit()` returns **`True`** only if **all** characters in the string are digits (0-9).
- It returns **`False`** if the string contains:
  - Alphabets
  - Special characters
  - Spaces
  - Is empty (`''`)
- **Numbers (integers) don’t have `.isdigit()`**—it must be called on a string.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
# isupper()  method  demo  program
print('HYd'.isupper())      # False (contains lowercase 'd')
print('HYD'.isupper())      # True (all uppercase)
print('9247'.isupper())     # False (only digits, no alphabets)
print('RAMA RAO'.isupper()) # True (all uppercase, space doesn't affect)
print('+-$'.isupper())      # False (only special characters, no alphabets)
print('HYD123'.isupper())   # True (has uppercase letters & no lowercase)
print('HYD+-$'.isupper())   # True (has uppercase letters & no lowercase)
print(''.isupper())         # False (empty string)
print('A2#'.isupper())      # True (has uppercase 'A' & no lowercase)
```

---

### **Explanation & Expected Output:**

| **String**   | **Contains Uppercase?** | **Contains Lowercase?** | **Output**  |
|-------------|-------------------------|-------------------------|------------|
| `'HYd'`     | ✅ Yes                    | ✅ Yes (`d`)             | `False`    |
| `'HYD'`     | ✅ Yes                    | ❌ No                    | `True`     |
| `'9247'`    | ❌ No (only digits)       | ❌ No                    | `False`    |
| `'RAMA RAO'`| ✅ Yes                    | ❌ No                    | `True`     |
| `'+-$'`     | ❌ No (only symbols)      | ❌ No                    | `False`    |
| `'HYD123'`  | ✅ Yes                    | ❌ No                    | `True`     |
| `'HYD+-$'`  | ✅ Yes                    | ❌ No                    | `True`     |
| `''` (empty)| ❌ No characters          | ❌ No                    | `False`    |
| `'A2#'`     | ✅ Yes                    | ❌ No                    | `True`     |

---

### **Final Expected Output:**
```
False
True
False
True
False
True
True
False
True
```

---

### **Key Takeaways:**
- `.isupper()` returns **`True`** if:
  - There is **at least one uppercase letter**.
  - There are **no lowercase letters**.
- It returns **`False`** if:
  - There are **no uppercase letters** at all.
  - There is **at least one lowercase letter**.
  - The string is **empty (`''`)**.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
# islower()  method  demo  program
print('hyD'.islower())      # False (contains uppercase 'D')
print('hyd'.islower())      # True (all lowercase)
print('9247'.islower())     # False (only digits, no alphabets)
print('rama rao'.islower()) # True (all lowercase, space doesn't affect)
print('+-$'.islower())      # False (only special characters, no alphabets)
print('hyd+-$'.islower())   # True (has lowercase letters & no uppercase)
print('abc123'.islower())   # True (has lowercase letters & no uppercase)
print(''.islower())         # False (empty string)
print('a2#'.islower())      # True (has lowercase 'a' & no uppercase)
```

---

### **Explanation & Expected Output:**

| **String**   | **Contains Lowercase?** | **Contains Uppercase?** | **Output**  |
|-------------|-------------------------|-------------------------|------------|
| `'hyD'`     | ✅ Yes                    | ✅ Yes (`D`)             | `False`    |
| `'hyd'`     | ✅ Yes                    | ❌ No                    | `True`     |
| `'9247'`    | ❌ No (only digits)       | ❌ No                    | `False`    |
| `'rama rao'`| ✅ Yes                    | ❌ No                    | `True`     |
| `'+-$'`     | ❌ No (only symbols)      | ❌ No                    | `False`    |
| `'hyd+-$'`  | ✅ Yes                    | ❌ No                    | `True`     |
| `'abc123'`  | ✅ Yes                    | ❌ No                    | `True`     |
| `''` (empty)| ❌ No characters          | ❌ No                    | `False`    |
| `'a2#'`     | ✅ Yes                    | ❌ No                    | `True`     |

---

### **Final Expected Output:**
```
False
True
False
True
False
True
True
False
True
```

---

### **Key Takeaways:**
- `.islower()` returns **`True`** if:
  - There is **at least one lowercase letter**.
  - There are **no uppercase letters**.
- It returns **`False`** if:
  - There are **no lowercase letters** at all.
  - There is **at least one uppercase letter**.
  - The string is **empty (`''`)**.

---

### **Additional Notes:**
- **What are `.upper()` and `.lower()` called?**
  - They are **conversion methods** (they change case).
- **What are `.isupper()` and `.islower()` called?**
  - They are **conditional methods** (they return `True` or `False`).

-------------------------------------------------------------------------------------------------------------------------------------------
# isalnum()  method  demo  program
print('A7$g'.isalnum())    # False (contains special character '$')
print('HYD'.isalnum())     # True (only alphabets)
print('+-$'.isalnum())     # False (only special characters)
print('hyd'.isalnum())     # True (only alphabets)
print('hYd'.isalnum())     # True (only alphabets)
print('9247'.isalnum())    # True (only digits)
print(''.isalnum())        # False (empty string)
print('A7g9'.isalnum())    # True (contains only alphabets and digits)
```

---

### **Explanation & Expected Output:**

| **String**   | **Contains Alphabets?** | **Contains Digits?** | **Contains Special Characters?** | **Output**  |
|-------------|-------------------------|----------------------|----------------------------------|------------|
| `'A7$g'`    | ✅ Yes                    | ✅ Yes               | ✅ Yes (`$`)                    | `False`    |
| `'HYD'`     | ✅ Yes                    | ❌ No                | ❌ No                           | `True`     |
| `'+-$'`     | ❌ No                     | ❌ No                | ✅ Yes (`+`, `-`, `$`)          | `False`    |
| `'hyd'`     | ✅ Yes                    | ❌ No                | ❌ No                           | `True`     |
| `'hYd'`     | ✅ Yes                    | ❌ No                | ❌ No                           | `True`     |
| `'9247'`    | ❌ No                     | ✅ Yes               | ❌ No                           | `True`     |
| `''` (empty)| ❌ No characters          | ❌ No                | ❌ No                           | `False`    |
| `'A7g9'`    | ✅ Yes                    | ✅ Yes               | ❌ No                           | `True`     |

---

### **Final Expected Output:**
```
False
True
False
True
True
True
False
True
```

---

### **Key Takeaways:**
- `.isalnum()` returns **`True`** if:
  - The string **only contains alphabets and/or digits**.
  - **No special characters** are present.
- It returns **`False`** if:
  - There is **at least one special character** (`$`, `+`, `-`, etc.).
  - The string is **empty (`''`)**.

---

### **Additional Notes:**
- **What is `isalnum()`?**
  - It is a combination of **`isalpha()`** (checks if a string contains only letters) **and** **`isdigit()`** (checks if a string contains only digits).
  - Essentially:  
    ```python
    isalnum() == isalpha() or isdigit()
    ```
- **Example:**
  ```python
  print('abc123'.isalnum())  # True (letters + digits)
  print('abc!123'.isalnum()) # False (contains '!')
  ```
