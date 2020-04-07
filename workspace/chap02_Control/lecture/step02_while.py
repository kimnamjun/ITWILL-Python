# 반복문 while

# 카운터, 누적 변수
cnt = tot = 0
while cnt < 5:
    cnt += 1
    tot += cnt
    print(cnt, tot)

# 문1) 1~100 합 + 짝수 출력
cnt = tot = 0
data = list()
while cnt < 100:
    cnt += 1
    tot += cnt
    if cnt % 2 == 0:
        data.append(cnt)
print(tot)
print(data)

# 문2) 1~100에서 5의 배수이면서 3의 배수가 아닌 값만 append
cnt = 0
data = []
while cnt < 100:
    cnt += 1
    if not cnt % 5 and cnt % 3:
        data.append(cnt)
print(data)


# 무한 loop -> 종료 조건(0)
while True:
    num = int(input("숫자 입력 : "))
    if num == 0:
        print("프로그램 종료")
        break
    print(f"num = {num}")

# 난수 생성
import random
r = random.random()  # 0~1 사이의 난수
print(f'r = {r}')

r = random.randint(0, 5) # 0, 1, 2, 3, 4, 5 / 끝 값 포함
print(f'r = {r}')

r = random.choice(['가','나','다'])
print(f'r = {r}')

# 문3) 난수가 0.01 미만이면 종료, 아니면 난수 개수 출력
cnt = 0
while True:
    r = random.random()
    if r < 0.01:
        break
    else:
        cnt += 1
print(cnt)

print('>>> 숫자 맞히기 게임 <<<')
'''
숫자 범위 : 1 ~ 10
myInput == computer : 성공(exit) -> 종료조건
myInput > computer : '더 작은 수 입력'
myInput < computer : '더 큰 수 입력'
'''
r = random.randint(1, 10)
while True:
    n = int(input('숫자 입력 : '))
    if n > r:
        print('더 작은 수 입력')
    elif n < r:
        print('더 큰 수 입력')
    else:
        print(f'정답! ({r})')
        break

'''
continue vs break
- 반복문에서 사용되는 명령어
- continue : 반복을 지속, 다음 문장 skip
- break : 반복 멈춤
'''

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end=' ')