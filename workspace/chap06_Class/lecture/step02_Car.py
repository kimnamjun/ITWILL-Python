'''
동적 멤버 변수 생성
- 필요한 경우 특정 함수에서 멤버 변수 생성
- self : 클래스의 멤버를 호출하는 역할
- self.멤버변수
- self.멤버메서드()
'''


class Car:
    # 멤버변수
    door = cc = 0
    name = None

    # 생성자 : 객체 + 초기화
    def __init__(self, door, cc, name):
        self.door = door
        self.cc = cc
        self.name = name

    # 멤버 메소드 : 자료 처리
    def info(self):
        self.kind = ''
        if self.cc >= 3000:
            self.kind = '대형'
        else:
            self.kind = '소형'
        self.display()

    def display(self):
        print(f"{self.name}{'은' if (ord(self.name[-1]) - 44032) % 28 else '는'} {self.cc}cc이고, 문짝은 {self.door}개이다.")


# 객체 생성 : 생성자() -> object
car1 = Car(4, 2000, '소나타')
print(f'자동차 이름 : {car1.name}')
car1.info()

car2 = Car(4, 3000, '그랜저')
print(f'자동차 이름 : {car2.name}')
car2.info()