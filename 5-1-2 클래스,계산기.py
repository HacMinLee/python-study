#class=설계도
class FourCal:
    def __init__(self, first, second):   #생성자. setdata를 입력하는것을 강제한다. 입력값을 강제해서 오류가 안나게하는존재.
        self.first = first
        self.second = second

    def setdata(self,first,second):      #self부분엔 a라는 놈이 박힌다고한다.
        self.first=first
        self.second=second
    def add(self):
        result=self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#계산기찍어내기

a=FourCal(4,2)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


#b=FourCal()
#b.setdata(10,5)
#print(b.add())
#print(b.mul())
#print(b.sub())
#print(b.div())


class MoreFourCal(FourCal):         #클래스의 상속
    def pow(self):
        result = self.first ** self.second
        return result


c=MoreFourCal(2,3)
print(c.add())
print(c.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:                # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
d=SafeFourCal(5,0)
print(d.div())                              #혹여나 d를 FourCal과 SafeFourCal에 동시에 만들어서 해도 자식이 이긴다, 자식이기는부모없다