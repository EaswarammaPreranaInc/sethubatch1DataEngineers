Of course, Sowmya! Here's the same OTP program with **step-by-step comments** so you understand everything clearly:

---

### ✅ Python Program to Generate 6-Digit OTP (with comments):

```python
# Import the random module to generate random numbers
import random

# Generate a random number between 0 and 999999
otp = random.randint(0, 999999)

# Format the number to make sure it is always 6 digits (adds leading zeros if needed)
# For example, if otp = 156, this becomes "000156"
formatted_otp = f"{otp:06d}"

# Display the formatted OTP
print("Your OTP is:", formatted_otp)
```

---

### 🧠 Explanation:

| Line | What It Does |
|------|---------------|
| `import random` | Brings in Python's random number functions |
| `random.randint(0, 999999)` | Generates a number between 000000 and 999999 |
| `f"{otp:06d}"` | Formats the number to 6 digits with leading zeros |
| `print(...)` | Displays the OTP to the user |

---

### 🖥 Sample Output:

```
Your OTP is: 004567
```
------------------------------------------------------------------------------------------------------
  
