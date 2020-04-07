import time
import random


class Card:
    def __init__(self, _num):
        self.num = _num
        self.rand = random.random()
        self.opened = False

    def show(self):
        if self.num // 13 == 0:
            print('♣', end ='')
        elif self.num // 13 == 1:
            print('♥', end='')
        elif self.num // 13 == 2:
            print('◆', end='')
        elif self.num // 13 == 3:
            print('♠', end='')

        if self.num % 13 == 0:
            print('A', end=' ')
        elif self.num % 13 == 10:
            print('J', end=' ')
        elif self.num % 13 == 11:
            print('Q', end=' ')
        elif self.num % 13 == 12:
            print('K', end=' ')
        else:
            print(self.num % 13 + 1, end=' ')


class User:
    def __init__(self, _name, _money):
        self.name = _name
        self.money = _money
        self.cards = list()


def show(_users):
    print('테이블 현황입니다.')
    for i in _users:
        print(f'{i.name}')
        for j in i.cards:
            if j.opened:
                j.show()
            else:
                print('??', end=' ')
        print()


if __name__ == '__main__':
    users = list()

    user_name = input('사용자 이름을 입력하세요. ')
    users.append(User(user_name, 2000))
    users.append(User('User1', 2000))
    users.append(User('User2', 2000))
    users.append(User('User3', 2000))

    user_num = len(users)

    while users[0].money > 100:
        print('게임을 시작합니다.')
        print('기본 베팅을 진행합니다.')
        print('-100원')

        for i in range(user_num):
            users[i].cards = list()
            users[i].money -= 100

        # 카드 셔플
        deck = list()
        for i in range(52):
            deck.append(Card(i))
            time.sleep(0.001)
        deck = sorted(deck, key=lambda x: x.rand)

        # 패 돌리기
        for i in range(user_num):
            for j in range(4):
                users[i].cards.append(deck.pop())

        # 멀리건
        select = ''
        while not(select == '1' or select == '2' or select == '3' or select == '4'):
            print('버릴 카드를 입력하세요. (1-4)')
            for i in users[0].cards:
                i.show()
            select = input()
        users[0].cards.pop(int(select) - 1)

        select = ''
        while not(select == '1' or select == '2' or select == '3'):
            print('공개할 카드를 입력하세요. (1-4)')
            for i in users[0].cards:
                i.show()
            select = input()
        temp_card = users[0].cards.pop(int(select) - 1)

        # 게임 시작
        users[0].cards.append(temp_card)
        users[0].cards.append(deck.pop())
        users[0].cards.append(deck.pop())
        for i in users[0].cards:
            i.opened = True

        for i in range(1, user_num):
            users[i].cards.pop()
            users[i].cards.append(deck.pop())
            users[i].cards.append(deck.pop())
            for j in range(2, 5):
                users[i].cards[j].opened = True

        users[0].cards = sorted(users[0].cards, key=lambda x: x.opened)

        show(users)

        # 족보?