'''
기본(default) 생성자
- 생성자를 생략하면 기본 생성자가 만들어진다.
- 묵시적 생성자
'''


class DefaultCost:
    # 생성자 생략
    # def __init__(self):
    #     pass

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y


obj1 = DefaultCost()
obj1.data(10, 20)
print(obj1.mul())

'----------------------------------------------------------'


# TV 클래스 정의
class TV:
    channel = volume = 0
    power = False
    color = None

    def __init__(self):
        pass

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        self.channel -= 1

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

    def change_power(self):
        self.power = not(self.power)

    def data(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    def display(self):
        print(f"전원 : {self.power}, 채널 : {self.channel}, 볼륨 : {self.volume}, 색상 : {self.color}")


tv1 = TV()
tv1.data(5, 10, 'Black')
tv1.display()

tv1.change_power()
tv1.channel_up()
tv1.volume_up()

'''
문) tv2 객체를 다음과 같이 생성하시오.
단계1 : 전원 : False, 채널: 1,  볼륨 : 1,  색상 : 파랑색
단계2 : 전원 : True,  채널: 10, 볼륨 : 15
'''
tv2 = TV()
tv2.data(1, 1, 'Blue')

tv2.change_power()
tv2.channel = 10
tv2.volume = 15

tv2.display()