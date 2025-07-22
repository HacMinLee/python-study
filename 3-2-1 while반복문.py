treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print('나무를 %s번 찍었습니다.' % treeHit)
    if treeHit==10:
        print('나무가 넘어갑니다.')          #디버깅해서 순서를 봐봐라.







prompt= '''
1. ADD
2. DEL
3. LIST
4. QUIT
Enter number: '''

number=0
#while number != 4:
 #   print(prompt)
  #  number=int(input())












coffee=10
money=300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee=coffee-1
    print('남은 커피의 양은 %s 입니다.' %coffee)
    if coffee==0:
        print('커피가 다 떨어졌습니다. 판매종료')
        break