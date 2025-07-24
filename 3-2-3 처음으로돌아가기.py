a = 0
while a < 20:
    a = a + 1
    if a % 2 == 0: 
        continue   #2로 나눈 나머지가 ==0 이면 다시 처음으로 돌아가라.
    else:
        print(a)
print('프로그램 다 끝')