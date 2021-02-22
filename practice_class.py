class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# super를 다중 상속시 사용하는 경우
# 맨 처음 상속받는 클래스에 대하여 오버라이딩함
# 다중 상속의 경우 별도 명시를 해주는 것이 좋음
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

        


dropship = FlyableUnit()