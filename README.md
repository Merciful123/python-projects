# module1
creating a module using python
def add(*x):
    return sum(x)

def sub(*x):
    result=x[0]
    for i in x[1:]:
        result=result-i
    return result
def multiply(*x):
    result=1
    for i in x:
        result=result*i
    return result

def divide(*x):
    result=1
    for i in x:
       result=result/i
    return result


import calc


print(calc.add(10,20,30,40,50))
print(calc.sub(10,20,30))
print(calc.multiply(1,2,3,4,5,7,8,9))
print(calc.divide(1,2,5,5,5,5))
