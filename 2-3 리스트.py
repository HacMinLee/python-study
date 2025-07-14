odd=[1,3,5,7,9]            #대괄호와 콤마로 만든다 리스트는.
print(type(odd))
print(odd)


e=[1,2,'life','is','3']    #리스트안에 다른 자료형도 가능. 파이썬특임
print(e)
print(type(e))
print(e[3])                #리스트안에선 is가 통으로3번째. 알파벳 하나하나마다 x
print(e[0]+e[1])            #3나온다. 숫자형자료형
print(e[2]+e[3])            #'life is'
                            #'3'은 문자형취급으로 1,2와 연산불가. 이건str이다.



a=[1,2,3,['a','b','c']]     #리스트속 리스트!
print(a[3])
print(a[3][1]) 
print(a[3]*3+a[3])         #print(a[3]*3+a[3][2])는 안된다, 리스트간에만 연산이 가능하고, str과 리스트는 불가능


#리스트 안의 거 바꾸기  str은 이렇게불가던데
f=[1,2,3]
f[2]=4
print(f)

del f[0:2]                 #리스트안에꺼 날려보리기
print(f)
f.append(3)                #리스트에 추가하기 append--insert로 통일이 편할듯
print(f)
f.sort()
print(f) 
f.reverse()
print(f)

f.insert(1,5)              #1번째인덱스에 5값넣어라.
print(f)

f.remove(4)
print(f)

print(f.pop()   )
                           #pop은 그냥 뒤에서 하나를 뿅!뽑는다.튀어나와서 남아있음3이 ㅋ
print(f)

f.insert(0,3)              #아,인서트는 자리를 꼭 지정해줘야되네. append는 지정안해도 들어감
print(f)
 