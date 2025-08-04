#반복되는 변수&함수를 미리 정해놓은 틀(설계도)
# calculator3.py
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()
cal4 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print('='*50)
print(cal2.add(3))
print(cal2.add(7))
print('='*50)
print(cal3.add(1))
print(cal3.add(3))
print('='*50)
print(cal4.add(2))
print(cal4.add(5))



class Cookie:              #클래스는 대문자로 시작해야한다.
    pass

초코쿠키= Cookie()          #초코,아몬드쿠키를 인스턴스,객체라고 부른다
아몬드쿠키 = Cookie()


