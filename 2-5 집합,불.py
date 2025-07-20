s1=set([1,2,3])
print(s1)
print(type(s1))

s2={1,2,3}           #dict는 key:value지만 집합은 걍 중괄호치고 쓰면 set임.
print(s2)

s3=set('hellow')
print(s3)            #집합엔 순서없이 랜덤이다.(섞여있다)

s4={1,2,3,4,5,6}
s5={4,5,6,7,8,9}
print(s4&s5)         #교집합
print(s4|s5)         #합집합
print(s4-s5)         #차집합

s1.add(4)
print(s1)
s1.update([4,4,5,6])
print(s1)
s1.remove(2)
print(s1)


a=True
b=False
print(type(a))      #?대충 이런게있다. 불.