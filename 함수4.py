                                         # default1.py
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself('이학민',27)                   #기본값이 man은 True이기 때문에 안써도 기본값인 man=True가 들어간다.
