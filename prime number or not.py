
num = 7  # The number to check
count = 0  # Counter to count the number of divisors

# Loop through all numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:  # Check if i is a divisor of num
        count += 1  # Increment the counter for each divisor

# A number is prime if it has exactly 2 divisors (1 and itself)
if count == 2:
    print('Prime number')
else:
    print('Not a prime number')


# using while loop

num = 7  # The number to check
count = 0  # Counter for divisors
i = 1  # Start checking divisors from 1

# Use a while loop to count the number of divisors
while i <= num:
    if num % i == 0:  # Check if i is a divisor of num
        count += 1  # Increment divisor count
    i += 1  # Move to the next number

# Check if the number is prime
if count == 2:  # A prime number has exactly 2 divisors
    print("Prime number")
else:
    print("Not a prime number")






#using def keyword

def prime(n):
    # Loop through numbers from 2 to n
    for i in range(2, n+1):
        is_prime = True  # Assume the number is prime
        # Check divisors from 2 to the square root of the number
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:  # If divisible, it's not a prime
                is_prime = False
                break
        if is_prime:
            print(i)  # Print the prime number

# Call the function to find primes up to 50
prime(50)






# using recursion
def is_prime(num, div=2):
    # Base case: if divisor equals the number, it's prime
    if div * div > num:  # Optimized to check divisors only up to the square root
        return True
    if num % div == 0:  # If divisible, it's not prime
        return False
    return is_prime(num, div + 1)  # Check the next divisor

def print_prime(n):
    for num in range(2, n + 1):  # Iterate through all numbers from 2 to n
        if is_prime(num):  # Check if the number is prime
            print(num)  # Print the prime number

# Call the function to print prime numbers up to 50
print_prime(50)
