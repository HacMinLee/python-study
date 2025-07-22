enoughmoney=True
if enoughmoney:
    print('택시를 타고 가라')     #들여쓰기 =tap
else:
    print('걸어 가라')

x=3
y=2
print(x>y)
print(x>=y)                     #크거나같나요? 
print(x==y)                     #같나요?
print(x!=y)                     #같지않죠?

money=2000
card=True

if money>=3000 or card:    
    print('택시타')
else:
    print('거지쉑 걸어')


print(1 in [1,2,3])
print(1 not in [1,2,3])


pocket=['종이','휴대폰','돈']
if '돈' in pocket:
    print('택시타고가라')
else:
    print('걸어가라잉')



print('='*50)



pocket=['종이','휴대폰','돈']
if '돈' in pocket:
    pass
else:
    print('걸어가라잉')



print('='*50)



if '돈' in pocket:
    print('택시타')
else:
    if card:
         print('택시타')
    else:
        print('걸어가라')

if '돈' in pocket:            #같은표현이다, else하고 또 조건문올때 elif로 줄인다.
    print('택시타')
elif card:
    print('택시타')
else:
    print('걸어가')

if money in pocket: print('택시타용') #안띄워도 되긴한데,,, 걍 띄어서 써라 ;;
else: print('ㅗ')

