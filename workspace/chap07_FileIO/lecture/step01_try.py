'''
예외) 프로그램 실행 상태에서 예기치 않은 상황(오류)
try:
    예외 발생 코드
except:
    예외 처리 코드
finally:
    항상 처리 코드
'''

# 1. 간단한 예외 처리
try:
    print('프로그램 시작')
    x = [10, 20, 35.5, 15, 'num', 14.5]
    for i in x:
        print(i)
        y = i ** 2
        print(f'y = {y}')
    print('프로그램 종료')
except:
    try:
        print(f'예외발생(숫자 아님) : {i}')
    except:
        print('except의 except였던거임')

# 2. 유형별 예외 처리
try:
    div1 = 1000 / 2.5  # 정상

    # div2 = 1000 / 0  # 1차 : 산술적 예외

    # f = open("C:/text.txt")  # 파일 열기

    num = int(input('숫자 입력 : '))
    print(f'num = {num}')

except ZeroDivisionError as e:  # e : class as object
    print(f'예외 발생 : {e}')

except FileNotFoundError as e:
    print(f'예외 발생 : {e}')

except Exception as e:
    print(f'기타 예외 발생 : {e}')

finally:
    print('프로그램 종료')
