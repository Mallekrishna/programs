#highest value

l = [78,58,68,98,34,55,18,19]
h=l[0]
for i in l:
    if i > h:
        h=i
print(h)


# 2nd higest value

l = [78,58,68,98,34,55,18,19]
h=[0]
sh=[0]
for i in l:
    if i>h[0]:
        sh[0]=h[0]
        h[0]=i
    elif i!=h[0] and i>sh[0]:
        sh[0]=i
print(sh[0])


#3rd highest value

l = [78,58,68,98,34,55,18,19]
h=[0]
sh=[0]
for i in l:
    if i>h[0]:

        h[0]=i
    elif i!=h[0] and i>sh[0]:
        sh[0]=i
print(sh[0])


#lowest value
l = [78,58,68,98,34,55,18,19]
h=l[0]
for i in l:
    if i < h:
        h=i
print(h)
