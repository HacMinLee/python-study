# vartest.py
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)            #2가 아닌1이 나온다. a는 지역변수에서 2가된거고 마지막 print(a)는 글로벌a변수에 대해서 출력.



#def vartest1(b):
#    b=b+1

#vartest1(3)
#print(b)             이거오류뜬다. why? b가 글로벌변수로 지정되지않고 지역변수에서만 지정된상태.


