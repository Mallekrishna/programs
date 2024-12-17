#1
def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i  # Corrected the syntax
    return fact

print(fact(5))  # Outputs 120

#using recursion

def fun(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
num=5
print(fact(5))



#