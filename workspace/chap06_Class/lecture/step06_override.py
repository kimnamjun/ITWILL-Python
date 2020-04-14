'''
1. 메소드 재정의(method override)
- 부모의 원형 메소드 -> 자식에 원형 메소드를 다시 작성하는 문법
- 상속관계에서만 나오는 용어
- 인수, 내용 -> tnwjd eotkd

2. 다형성
- 상속 관계에서만 나오는 용어
- 한 가지 기능 -> 2개 이상 결과 생성(+ -> 덧셈, 결합)
- 부모 객체 -> (지식1, 지식2) 멤버 호출
'''


# 1. 메소드 재정의
class Super:
    def super_func(self):
        pass


class Sub1(Super):
    def super_func(self, data):  # 수정 -> override
        self.data = data
        print(f'data1 = {data}')


class Sub2(Super):
    def super_func(self, data):
        self.data = data
        print(f'data2 = {data ** 2}')


subclass1 = Sub1()
subclass1.super_func('20200414')

subclass2 = Sub2()
subclass2.super_func(100)


# 2. 다형성
superclass = Super()
subclassA = Sub1()
subclassB = Sub2()

superclass = subclassA
superclass.super_func(100)
superclass = subclassB
superclass.super_func(100)