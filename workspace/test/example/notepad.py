class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.num = 1
        return cls.instance
        # if 안에 return이 있으면 두 번째 객체부터는 안 만들어짐
        # 밖에 있으면 두 번째 객체가 첫 번째 객체와 같은 것을 가리킴

    def show(self):
        print(f'Hello, World! {self.num}')


s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)

s1.show()
s2.show()