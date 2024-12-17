def pangram(sentence):
    # Convert the sentence to lowercase to make it case-insensitive
    sentence = sentence.lower()

    # Create a set of all English alphabet letters
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    # Create a set of all unique letters in the sentence
    sentence = set(sentence)

    # Check if all alphabet letters are in the sentence
    return alphabet.issubset(sentence)


# Test the function
sentence = "The quick brown fox jumps over the lazy dog"
if pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")




#2

s = "The quick brown fox jumps over the lazy dog"
s = s.upper()  # Convert the string to uppercase

# Check for each character from A to Z
for i in range(ord('A'), ord('Z') + 1):
    if chr(i) not in s:  # Check if the character is not in the string
        print('Not a pangram')
        break
else:
    print('Pangram')

