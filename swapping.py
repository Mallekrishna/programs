#method 1
print('')
print('METHOD 1')
l =[1,2,3,4,5]
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)

print('')
print('METHOD 2')
# method 2
a=5
b=10
temp=a
a=b
b=temp
print('a',a)
print('b',b)

print('')
print('METHOD 3')
#method 3
a= 5
b=10
a,b =b,a
print('a:',a)
print('b:',b)

#method 4

print('')
print('METHOD 4')

a=5
b=10
a= a+b
b=a-b
a=a-b
print('a:',a)
print('b:',b)