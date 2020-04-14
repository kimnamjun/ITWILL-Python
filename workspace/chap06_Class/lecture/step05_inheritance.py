'''
클래스 상속(Inheritance)
- 기존 클래스를 이용하여 새로운 클래스 생성 문법
- 부모 클래스 정의 -> 자식 클래스 생성
- 상속 대상 : 멤버(O) 생성자(X)
    -> 생성자는 상속 대상이 아님
형식)
class 자식(부모):
    멤버
    생성자
'''


class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'이름 : {self.name}, 나이 : {self.age}')


class Sub(Super):
    def __init__(self, name, age, gender):
        # python 3.8 기준 세 개 다 됨
        super().__init__(name, age)             # 이거를 사용하는 쪽이 좋아보임
        # super(Sub, self).__init__(name, age)  # Pycharm 자동 생성 코드 / 구조 변경 시 코드가 바꿔야하는 번거로움?
        # Super.__init__(self, name, age)       # 다중 상속시에 유용해보임
        self.gender = gender

    def display(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}')


super_man = Super('부모', 55)
super_man.display()

sub_man = Sub('자식', 22, '남자')
sub_man.display()


class Parent:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def display(self):
        print(f'이름 : {self.name}, 직업 : {self.job}')


class Children(Parent):
    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender

    def display(self):
        print(f'이름 : {self.name}, 직업 : {self.job}, 성별 : {self.gender}')


