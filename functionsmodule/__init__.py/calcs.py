import __pycache__.mathemat 

result = __pycache__.mathemat.add(2,3)
print(result)

result2 = __pycache__.mathemat.subs(5,7)
print(result2)

Stu_Det = __pycache__.mathemat.Details['Age']
print(Stu_Det)


import __pycache__.mathemat as pm
result = pm.add(2,3)
print(result)

result2 = pm.subs(5,7)
print(result2)

Stu_Det = pm.Details['Age']
print(Stu_Det)


from __pycache__.mathemat import add
result2 = add(2,10)
print(result2)


def add(a,b):
    return a*b
number = add(2,100)
print(number)




