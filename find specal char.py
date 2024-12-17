s= 'abc@123#57$'
count=0
for i in s:
    if i in '@#$':
        count+=1
print(count)