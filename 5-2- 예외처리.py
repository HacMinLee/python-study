# try_else_loop_v2.py
while True:
    try:
        age = int(input('나이를 입력하세요. (종료는 -1 입력): '))
    except:
        print('입력이 정확하지 않습니다.')
    else:
        if age == -1:
            print('프로그램을 종료합니다.')
            break
        elif age < 0 or age >= 99:       #-1이 더 위에 적혀있어서 -1 입력시 그냥 break 여기칸에 적용x
            print('구라치지마세요.')
        elif age < 18:
            print('미성년자는 출입금지입니다.')
        else:
            print('환영합니다.')
            break
    finally:
        print("🌀영양제의정석에 오신 것을 환영합니다.")


#이러면 사용자입력값이 오류나도 어떻게든 지나간다.