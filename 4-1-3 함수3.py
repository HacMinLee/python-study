def kwargs(**kwargs):     #  **kwargs는 딕셔너리형태로 받는다.
    return (kwargs)

print(kwargs(a=1))
print(kwargs(name='foo', age=3))


def add_and_mul(a,b):
    return a+b, a*b       #이건 리턴값이 하나인 것.
print(add_and_mul(2,3))

j,k=add_and_mul(2,3)
print(j)
print(k)


#def add_and_mul(a,b)
#    return a+b
#    return a*b
#print(add_and_mul(2,3))  이거안된다. 리턴값이 2줄은 안됌. 리턴값은 무쟈건 한줄