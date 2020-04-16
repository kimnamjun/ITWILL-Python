#문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 

'''
문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문단 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

try:
    with open("../data/ftest.txt", mode = 'r') as file:
        lines = file.readlines()
        print('문단 내용')
        print(lines)
        print(f'문단 수 : {len(lines)}')

        file.seek(0)

        words = file.read().split()
        print('단어 내용')
        print(words)
        print(f'단어 수 : {len(words)}')

except Exception as e:
    print(f'예외 발생 : {e}')
finally:
    print('프로그램 종료')