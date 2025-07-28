for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ")  # end는 출력되는 줄 유지
    print('')                # 줄바꾸기

print('='*50)
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)



result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)
