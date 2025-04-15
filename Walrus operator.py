print(a := 25)  # Correct: Assigns 25 to 'a' and prints 25
print(a = 25)  # ERROR: '=' is not allowed inside print()
print(a)  # Will work if previous line didn't have an error
print(a := 6 + 7)  #  Correct: Assigns 13 to 'a' and prints 13
print(a)  #  Will print 13
print((a := 6) + 7)  #  Assigns 6 to 'a', then adds 7, prints 13
print(a)  #  Will print 6
print((a = 6) + 7)  # ERROR: '=' cannot be used inside an expression
