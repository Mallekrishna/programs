s = 'ENGINEERING'
res = ""  # Initialize the result variable

for i in s:
    if s.count(i) == 1:  # If the character appears only once in the string
        print(i)
        res += i  # Add the character to the result string

  # Print the accumulated result
