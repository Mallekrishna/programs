def is_vowel(char):
    vowels = 'aeiouAEIOU'  # Define a string containing all vowels (both lowercase and uppercase)
    return char in vowels  # Check if the character is in the vowels string

# Test the function with some characters
chars = ['a', 'b', 'E', 'z', 'I', 'o']

for char in chars:
    if is_vowel(char):
        print(f'{char} is a vowel')
    else:
        print(f'{char} is not a vowel')


# 2
s= 'unpro fessional student'
res= ''
for i in s:
    if i in 'aeiou':
        res+=i
print(res)


#not vowels

s= 'unpro fessional student'
res= ''
for i in s:
    if i not in 'aeiou':
        res+=i
print(res)