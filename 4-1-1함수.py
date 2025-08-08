def 함수(a,b):            #함수정의하기
    return a+b

print(함수(4,7))          #출력시키기


def add_many(*args): 
    result = 0
    for i in args: 
        result = result + i   # *args에 입력받은 모든 값을 더한다.
    return result 

print(add_many(1,2,3,4,5,6,7,8,9))