t1 = (1,2,3,'life',(5,6,7))
print(t1)
print(type(t1))
print(t1[2])

t2=1,2,3,'life'              #소괄호없이 쉼표만 넣어도 튜플이 된다.
print(t2)
#del t2[0]                    튜플은 삭제,추가,변경 불가

t3=t1+t2
print(t3)
#t1.sort()                    이것도 안된다. 이건 변형이다.
                              #insert remove pop sort 불가능






print('='*50)






dic={'name':'이학민','전화번호':'010-9100-9554','생일':'0416'}
print(type(dic))
print(dic)
dic[3]=[1,2,3]               #딕셔녀리에 추가 dic[key]=value들 리스트에선 이게 3번째자리를 바꾸는거였는데 딕셔너리에선 추가임.
print(dic)

del dic['name'],dic['생일']   #삭제는 key를 지운다.
print(dic)
print(dic['전화번호'])        #key를 지정해서 value를 프린트
print(dic.keys())
print(dic.values())
print(dic.items())

print(dic.get('전화번호','값이없습니다'))
print(dic.get('hi','값없어임마'))

dic.clear()
print(dic)

#리스트 a=[1,2,3]
#딕셔너리 a={0:1,1:2,2:3}
#print(a[0])