# Taking input
s = input("Enter a string: ")

# Forward direction (using positive indices)
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

print()  # To separate forward and reverse outputs

# Reverse direction (using negative indices)
for i in range(-1, -len(s)-1, -1):
    print(f"Character at index {i} : {s[i]}")
#"'output "
# Enter a string: kingkong
# Character at index 0 : k
# Character at index 1 : i
# Character at index 2 : n
# Character at index 3 : g
# Character at index 4 : k
# Character at index 5 : o
# Character at index 6 : n
# Character at index 7 : g

# Character at index -1 : g
# Character at index -2 : n
# Character at index -3 : o
# Character at index -4 : k
# Character at index -5 : g
# Character at index -6 : n
# Character at index -7 : i
# Character at index -8 : k