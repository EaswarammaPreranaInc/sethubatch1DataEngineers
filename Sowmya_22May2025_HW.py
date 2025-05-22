
import re
string = input('Enter any string: ')
pattern = input('Enter pattern: ')
m = re.search(pattern, string, re.IGNORECASE)
print(type(m))
if m:
    print(f'{m.group()} is found between indexes {m.start()} and {m.end() - 1}')
else:
    print(pattern, 'is not found')
```

---

## 🔹 **Case 1:**

### Inputs:

* `string` = `'Hyd is green city'`
* `pattern` = `'Green'`

> The `re.IGNORECASE` flag allows case-insensitive matching.

### Matching:

* `'Green'` matches `'green'` in the string.
* Start index of `'green'` in the string = `7`
* End index = `12` → But since we subtract 1, it becomes `11`

### Output:

```
<class 're.Match'>
green is found between indexes 7 and 11
```

---

## 🔹 **Case 2:**

### Inputs:

* `string` = `'Hyd is green city'`
* `pattern` = `'red'`

> `'red'` is not present in `'Hyd is green city'`.

### Output:

```
<class 'NoneType'>
red is not found
```

---

### ✅ Summary of Outputs:

#### **Case 1 Output:**

```
<class 're.Match'>
green is found between indexes 7 and 11Let's break down your Python code and explain **what it does and what the output will be**.

---

### **Code:**

```python
import re

m = re.search('^learn', 'Learning Python is simple', re.IGNORECASE)
if m:
    print('String starts with', m.group())
else:
    print('String does not start with learn')

m = re.search('Simple$', 'Learning Python is simple', re.IGNORECASE)
if m:
    print('String ends with', m.group())
else:
    print('String does not end with Simple')
```

---

### ✅ **Explanation:**

#### 🔹 `^learn`

This pattern checks if the **string starts with 'learn'**, case-insensitively.

* String: `'Learning Python is simple'`
* Does it **start with 'learn'**?
  ✅ **Yes**, it starts with `'Learning'`, and `'learn'` is a prefix of it.

> The pattern `^learn` will match the start of the string **only if it begins with 'learn' exactly**, not just a word **starting with** `'learn'`.

👉 But **`^learn` does NOT match `'Learning'`**, because `'Learning' ≠ 'learn'`.

So, this part **does not match**.

#### 🔹 `Simple$`

This pattern checks if the **string ends with 'Simple'**, case-insensitively.

* String: `'Learning Python is simple'`
* Does it **end with 'simple'**?
  ✅ Yes — and with `re.IGNORECASE`, `'Simple'` matches `'simple'`.

👉 So this **matches** successfully.

---

### 🟢 **Final Output:**

```
String does not start with learn
String ends with simple
```

---

If you want to match words that **start with** a prefix like `'learn'`, even if it's `'Learning'`, then you'd need to use a different regex like:

```python
re.search(r'\blearn\w*', text, re.IGNORECASE)
```
------------------------------------------------------------------------------------------------------------------------------
Let's walk through the code and inputs you've given:

---

### ✅ **Code Overview:**

```python
import re
string  =  input('Enter any string: ')
pattern = input('Enter pattern to be searched: ')
itr = re.finditer(pattern, string, re.IGNORECASE)
ctr = 0
while True:
    try:
        m = next(itr)
        print(f'{m.group()} is found between indexes {m.start()} and {m.end() - 1}')
        ctr += 1
    except StopIteration:
        break
print('Found', ctr, 'times')
```

---

### 🔹 Inputs:

**1st Input (string):**
`Hyd is green city. Hyd IS hitec city. Hyd Is hiS city`

**2nd Input (pattern):**
`is`

The pattern `is` is matched **case-insensitively** due to `re.IGNORECASE`.

---

### 🧠 Let’s Find All Matches:

The string:

```
Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
```

Let's locate each **case-insensitive** match of `"is"`:

| Match | Word Containing It                | Start Index | End Index |
| ----- | --------------------------------- | ----------- | --------- |
| `is`  | "is"                              | 4           | 6         |
| `IS`  | "IS"                              | 21          | 23        |
| `Is`  | "Is"                              | 37          | 39        |
| `hiS` | "hiS" (matches `is` inside "hiS") | 44          | 46        |

> In the last one, `"hiS"` contains `"is"` as `"iS"` (which still matches due to `IGNORECASE`).

---

### 🔸 Total Matches: 4

---

### ✅ **Output:**

```
is is found between indexes 4 and 5
IS is found between indexes 21 and 22
Is is found between indexes 37 and 38
hiS is found between indexes 44 and 45
Found 4 times
```

(Note: Even though the match is inside the word `"hiS"`, it still matches `"is"` inside `"hiS"` due to substring matching.)

---------------------------------------------------------------------------------------------------------
Let's analyze your Python regex code and determine the output step-by-step.

---

### ✅ **Code:**

```python
import re
itr = re.finditer('[A-Za-z0-9]', 'm$9 K,d%5@E&')
while True:
    try:
        m = next(itr)
        print(m.group(), ' is at index : ', m.start())
    except:
        break
```

---

### 🔍 **Pattern: `[A-Za-z0-9]`**

This pattern matches any **single alphanumeric character**:

* Uppercase letters: A–Z
* Lowercase letters: a–z
* Digits: 0–9

It will **ignore special characters** like `$`, `,`, `%`, `@`, `&`, and whitespace.

---

### 🔹 **Input String:**

`'m$9 K,d%5@E&'`

Let’s look at the indexes and matchable characters:

| Index | Character | Match? | Reason           |
| ----- | --------- | ------ | ---------------- |
| 0     | `m`       | ✅      | letter           |
| 1     | `$`       | ❌      | special char     |
| 2     | `9`       | ✅      | digit            |
| 3     | (space)   | ❌      | not alphanumeric |
| 4     | `K`       | ✅      | letter           |
| 5     | `,`       | ❌      | special char     |
| 6     | `d`       | ✅      | letter           |
| 7     | `%`       | ❌      | special char     |
| 8     | `5`       | ✅      | digit            |
| 9     | `@`       | ❌      | special char     |
| 10    | `E`       | ✅      | letter           |
| 11    | `&`       | ❌      | special char     |

---

### ✅ **Matched Characters and Their Indexes:**

| Character | Index |
| --------- | ----- |
| m         | 0     |
| 9         | 2     |
| K         | 4     |
| d         | 6     |
| 5         | 8     |
| E         | 10    |

---

### ✅ **Output:**

```
m  is at index :  0
9  is at index :  2
K  is at index :  4
d  is at index :  6
5  is at index :  8
E  is at index :  10
```
----------------------------------------------------------------------------------------------------------
Let's go through your code line by line and determine the outputs step by step for each regular expression.

---

### ✅ **Given String:**

```python
string = 'z7.Q-$2 b[9.a%6$G&k.%'
```

Let's number the characters in the string:

| Index | Char    |
| ----- | ------- |
| 0     | z       |
| 1     | 7       |
| 2     | .       |
| 3     | Q       |
| 4     | -       |
| 5     | \$      |
| 6     | 2       |
| 7     | (space) |
| 8     | b       |
| 9     | \[      |
| 10    | 9       |
| 11    | .       |
| 12    | a       |
| 13    | %       |
| 14    | 6       |
| 15    | \$      |
| 16    | G       |
| 17    | &       |
| 18    | k       |
| 19    | .       |
| 20    | %       |

---

### 🔹 `print(re.findall('[a-z]', string))`

Find all **lowercase letters**.

✅ Matches: `'z', 'b', 'a', 'k'`
**Output:**

```python
['z', 'b', 'a', 'k']
```

---

### 🔹 `print(re.findall('[0-9]', string))`

Find all **digits**.

✅ Matches: `'7', '2', '9', '6'`
**Output:**

```python
['7', '2', '9', '6']
```

---

### 🔹 `print(re.findall('[^A-Za-z0-9]', string))`

Find all characters **that are NOT alphanumeric**.

✅ Matches: `'.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%'`
**Output:**

```python
['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
```

---

### 🔹 `print(re.findall('.', string))`

The dot `.` matches **every character except newline**.

✅ Matches all characters in the string, in order.
**Output:**

```python
['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
```

---

### 🔹 `print(re.findall('[.]', string))`

Find all literal dots `.`.

✅ Matches: `'.', '.', '.'`
**Output:**

```python
['.', '.', '.']
```

---

### 🔹 `print(re.findall('[$]', string))`

Find all literal dollar signs `$`.

✅ Matches: `'$', '$'`
**Output:**

```python
['$', '$']
```

---

### 🔹 `print(re.findall('[%]', string))`

Find all literal percent signs `%`.

✅ Matches: `'%', '%'`
**Output:**

```python
['%', '%']
```

---

### 🔹 `print(re.findall('[az-]', string))`

This is a bit tricky due to the placement of the hyphen (`-`).

* In `[az-]`, the hyphen is **not between two characters**, so it's interpreted literally.
* So this matches: `'a'`, `'z'`, and `'-'`

✅ Matches: `'z', '-', 'a'`
**Output:**

```python
['z', '-', 'a']
```

---

### ✅ **Final Combined Output:**

```python
['z', 'b', 'a', 'k']

['7', '2', '9', '6']

['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']

['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']

['.', '.', '.']

['$', '$']

['%', '%']

['z', '-', 'a']
```
--------------------------------------------------------------------------------------------------------
Let's analyze both cases using the provided code:

---

### ✅ **Code Explanation:**

```python
import re
string  =  input('Enter any string: ')
pattern = input('Enter any pattern: ')
m = re.match(pattern, string, re.IGNORECASE)
if m:
    print(string, 'starts with', m.group())
else:
    print(string, 'does not start with', pattern)
```

* `re.match()` checks **only at the beginning** of the string.
* It's **case-insensitive** due to `re.IGNORECASE`.

---

## 🔹 **Case 1:**

### Input:

* `string = 'Sankar dayal sarma'`
* `pattern = 'san'`

### Matching:

* The string starts with `'Sankar'`.
* `'san'` (lowercase) matches `'San'` (from `'Sankar'`) — ✅ match.

### Output:

```
Sankar dayal sarma starts with San
```

(Note: `m.group()` returns exactly the part of the string that matched — in this case, `'San'`.)

---

## 🔹 **Case 2:**

### Input:

* `string = 'Hyderabad'`
* `pattern = 'Sec'`

### Matching:

* The string starts with `'Hyd...'`
* `'Sec'` does **not** match the beginning of `'Hyderabad'`.

### Output:

```
Hyderabad does not start with Sec
```

---

### ✅ **Final Answers:**

#### Case 1 Output:

```
Sankar dayal sarma starts with San
```

#### Case 2 Output:

```
Hyderabad does not start with Sec
```
------------------------------------------------------------------------------------------------------------
Yes, there is a **syntax error** in your code. Let's identify it clearly.

---

### ❌ **Error Line:**

```python
m = re.match(^pattern, string, re.IGNORECASE)
```

---

### ❗ What's Wrong:

* `^pattern` is **not valid syntax** in Python.
* The caret `^` is a **regex symbol** used **inside a string pattern**, **not outside**.

You're trying to use the caret to check if the pattern occurs at the start of the string, which is already the default behavior of `re.match()`.

---

### ✅ **Correct Line:**

```python
m = re.match(pattern, string, re.IGNORECASE)
```

Or, if you want to **explicitly** include the caret to anchor the pattern to the start:

```python
m = re.match(f'^{pattern}', string, re.IGNORECASE)
```

But again — `re.match()` already matches only from the **start**, so the caret is not needed unless you use `re.search()`.

---

### ✅ **Final Correct Code:**

```python
import re
string = input('Enter any string : ')
pattern = input('Enter any pattern : ')
m = re.match(pattern, string, re.IGNORECASE)
if m:
    print(string, 'starts with', m.group())
else:
    print(string, 'does not start with', pattern)
```
-----------------------------------------------------------------------------------------------------------------

---

### ✅ **Code Explanation:**

```python
import re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m = re.fullmatch(s1, s2, re.IGNORECASE)
if m:
    print('Same  strings  after  ignoring  the  case')
else:
    print('Different  strings')
```

* `re.fullmatch(pattern, string, re.IGNORECASE)` checks if **the entire `string` matches the `pattern`**, **ignoring case**.

---

## 🔹 Case 1:

**Inputs:**

* `s1 = 'HYD'`
* `s2 = 'hyd'`

**Behavior:**

* `re.fullmatch('HYD', 'hyd', re.IGNORECASE)` → ✅ Match

**Output:**

```
Same  strings  after  ignoring  the  case
```

---

## 🔹 Case 2:

**Inputs:**

* `s1 = 'HYD'`
* `s2 = 'SEC'`

**Behavior:**

* `re.fullmatch('HYD', 'SEC', re.IGNORECASE)` → ❌ No match

**Output:**

```
Different  strings
```

---

### ✅ Final Answers:

1. If inputs are `'HYD'` and `'hyd'` →
   **Output:** `Same  strings  after  ignoring  the  case`

2. If inputs are `'HYD'` and `'SEC'` →
   **Output:** `Different  strings`

---------------------------------------------------------------------------------------------------
Sure! Here's a complete Python program that validates a 10-digit mobile number based on your rules using the regular expression and `re.fullmatch()` function:

```python
import re

# Regular expression pattern
pattern = r'(0|\+91)?[6-9][0-9]{9}'

# Take input from user
mobile_number = input("Enter mobile number: ")

# Validate using fullmatch
if re.fullmatch(pattern, mobile_number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
```

---

### How it works:

* It checks if the input starts optionally with `0` or `+91`
* Then verifies the first digit is between 6 and 9
* Followed by exactly 9 digits (making total 10 digits excluding prefix)
* Uses `fullmatch()` to ensure the entire input matches the pattern exactly
