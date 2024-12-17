s1='listen'
s2='silent'
if sorted(s1)==sorted(s2):
    print('Anagram')
else:
    print('Not anagram')


s1 = 'mother-in-law'
s2 = 'hitler women'

s1 = s1.replace(' ', '').upper()
s2 = s2.replace(' ', '').upper()

if len(s1) != len(s2):
    print('anagram')
else:
    for i in s1:
        if s1.count(i) != s2.count(i):
            print('anagram')
            break
    else:
        print('not anagram')