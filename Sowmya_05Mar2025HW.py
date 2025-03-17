Here are the Python programs for each :

### 1️⃣ Search for an element in a list without using `in` operator
```python
numbers = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
search_element = 15
indices = []
count = 0

for index in range(len(numbers)):
    if numbers[index] == search_element:
        print(f"{search_element} is found at index {index}")
        indices.append(index)
        count += 1

print(f"{search_element} is found {count} times")
```

---

### 2️⃣ Modify the given program using the **walrus operator** (`:=`)
```
try:
    sum = ctr = 0
    while (x := eval(input('Enter input (-1 to stop): '))) != -1:
        sum += x
        ctr += 1
    print('Average:', sum / ctr)
except ZeroDivisionError:
    print('Enter at least one input')
except (NameError, TypeError):
    print('Input cannot be a string')
```

---

### 3️⃣ Determine the largest command-line input
```
import sys

if len(sys.argv) < 2:
    print("Pls send inputs")
else:
    try:
        a = [eval(x) for x in sys.argv[1:]]
        print(f"argv: {sys.argv}")
        print(f"List 'a': {a}")
        print(f"Largest number: {max(a)}")
    except:
        print("Pls send valid numeric inputs")
```

---

### 4️⃣ Check if the command-line input is even or odd
```
import sys

if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(sys.argv[1])
        print("Even number" if num % 2 == 0 else "Odd number")
    except ValueError:
        print("Pls send an integer input")
```

---

### 5️⃣ Determine the average of command-line inputs
```
import sys

try:
    a = [eval(x) for x in sys.argv[1:] if isinstance(eval(x), (int, float))]
    if len(a) == 0:
        print("Pls send number inputs")
    else:
        print("Average:", sum(a) / len(a))
except:
    print("Pls send number inputs")
```

---

### 6️⃣ Sort command-line inputs in ascending and descending order
```
import sys

try:
    a = [eval(x) for x in sys.argv[1:] if isinstance(eval(x), (int, float))]
    if len(a) == 0:
        print("Pls send numeric inputs")
    else:
        a.sort()
        print("Ascending order:", a)
        a.sort(reverse=True)
        print("Descending order:", a)
except:
    print("Pls don't send number and string inputs together")
```
