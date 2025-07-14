c = ' 삶은짧으니 \' 파이썬이 필요하다 '

print(c)
print(type(c))


d='I\'m hungry'

print(d)

b=2
e='''life is too short
u need python'''             #줄바꿔서도 문장형으로 인식되게
print(e)
head='python is'
tail= ' very fun'
print(head+tail)
print(head*b+tail*4+head+' b')
print("="*50)
print('my program')
print('='*50)
print(len(e)) 


print(c[3])
print(c[9],c[3])
print(d[0])            # 파이썬 문자열은 0칸부터 시작한다. 0123이렇게 간다
print(e[0:4])          # [ : ] 을 통해 문자열에서 표현되는 칸의 범위를 정할 수 있다 0~3까지가 아니라 0,1,2칸이 표시된다, 마지막놈은 미만의 의미이다.0이상4미만. life출력희망시 [0:4]를 해줘야한다.
print(e[2:])           # 2번칸부터 끝까지 
print(e[ : :3])        # c처음부터 끝까지 3칸간격으로 print
print(e[: :-2])        # 처음부터끝까지, 역순으로 2칸간격으로 


k="20250713rainday"
date=k[0:8] 
weather=k[8:]
print(date)
print(weather)
print(date,weather)




#문자열 포메팅.방법1: %s를 하면된다.

a= 'I eat %s apples a day.' %10      
print(a)

f= 'I eat %s apples a day.' %'five'   
print(f)

number=3
g= 'I eat %s apples a day.' %number
print(g)

i='today is %s,so i wanna eat %s apples.' %(weather,'five')
print(i)
#OR
h='today is {1} , so i want to eat {0} apples'  .format (weather,10)
print(h)       

 
t=3.23232233232323              #걍 소수점이렇게한대 제껴                
n='{0:0.4f}' .format(t)
print(n)


#포메팅 가장 최신-사실 이것만 알면된다.

name='이학민'
age=27
name2='노영대'
y=f'나의 이름은 {name}입니다. 제 나이는{age}입니다. 반가워요{name2}.'
print(y)
p=f'나는 내년이면{age+1}'
print(p)

print(e.count('o'))     #e안에 o몇개인지 세기
print(e.find("short"))  #e안에서 short찾아주세요--12번째네요~
print(e.index('o'))     #find와 동일

print(e.replace('life','your leg'))  #바꿔치기
print(e.split())

#그 외 여러가지 스킬들이 있지만 일단 대충보고 넘어가자. 