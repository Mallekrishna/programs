num=153
num_str = str(num)
count = len(num_str)
total= 0
for i in num_str:
    total += int(i)**count
if total == num:
    print(f"{num} ARMSTRONG")
else:
    print(f"{num}Not ARMSTRONG ")


# using while loop


num = 153
copy = num  # Save the original number for comparison
count = len(str(num))  # Count the digits in the number
add = 0

while num != 0:
    rem = num % 10  # Get the last digit of the number
    add += rem ** count  # Add the power of the digit to `add`
    num = num // 10  # Remove the last digit by performing integer division

if copy == add:
    print(f"{num} ARMSTRONG")
else:
    print(f"{num} not  ARMSTRONG")
