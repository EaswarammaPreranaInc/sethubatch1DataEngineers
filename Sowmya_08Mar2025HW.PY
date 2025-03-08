### **1. Merge Two Strings Alternately**
```
def merge_strings(s1, s2):
    c = ''
    i = 0
    while i < len(s1) and i < len(s2):
        c += s1[i] + s2[i]
        i += 1
    c += s1[i:] + s2[i:]
    return c

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = merge_strings(s1, s2)
print("Result:", result)
```
**Example Input & Output:**
```
Enter first string: HYD
Enter second string: VAMSI
Result: HVYADMSI
```

---

### **2. Remove Duplicate Characters from a String**
```
def remove_duplicates(s):
    out = ''
    for char in s:
        if char not in out:
            out += char
    return out

s = input("Enter any string: ")
print("String without duplicates:", remove_duplicates(s))
```
**Example Input & Output:**
```
Enter any string: MISSISIPI
String without duplicates: MISP
```

---

### **3. Demonstration of `len()` Function**
```
print(len('Hyd'))  
print(len('Rama Rao')) 
print(len('9247'))
print(len('+-$')) 
print(len('')) 
print(len(' ')) 
print(len('A2#')) 

# This will raise a TypeError because `len()` is not applicable to integers
# print(len(3456))  
```

---

### **4. Demonstration of `chr()` Function**
```
print(chr(65))  # A
print(chr(90))  # Z
print(chr(97))  # a
print(chr(122)) # z
print(chr(48))  # 0
print(chr(57))  # 9
print(chr(36))  # $
print(chr(32))  # (space)
```

---

### **5. Demonstration of `ord()` Function**
```
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('0'))  # 48
print(ord('9'))  # 57
print(ord('$'))  # 36
print(ord(' '))  # 32
```

---

### **6. Transform a String with Alternate Character and Digit**
```
def transform_string(s):
    if not all(s[i].isalpha() and s[i+1].isdigit() for i in range(0, len(s)-1, 2)):
        return "Please enter a string with alternating characters and digits"

    out = ''
    for i in range(0, len(s), 2):
        char = s[i]
        num = int(s[i+1])
        out += char + chr(ord(char) + num)
    
    return out

s = input("Enter any string with alternate character and digit: ")
print("Result:", transform_string(s))
```
**Example Input & Output:**
```
Enter any string with alternate character and digit: M3K2$5z2
Result: MPKM$)z|
```

If the input is incorrect:
```
Enter any string with alternate character and digit: hyd
Please enter a string with alternating characters and digits
```
