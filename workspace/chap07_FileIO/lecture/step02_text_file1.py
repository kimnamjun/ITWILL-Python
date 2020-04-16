'''
텍스트 파일 입출력
형식) open(file, mode)  / mode 'r'(default) 'w' 'a'
'''

import os

try:
    print(f'현재 경로 : {os.getcwd()}')  # 현재 경로 : C:\ITWILL\3_Python-I\workspace\chap07_FileIO\lecture

    # 1. 파일 읽기
    file1 = open(os.getcwd() + '/../data/ftest.txt', mode='r')  # 절대 경로
    print(file1.read())
    file1.close()

    file2 = open('../data/ftest.txt', mode='r')  # 상대 경로
    print(file2.read())
    file2.close()

    # 2. 파일 쓰기
    file3 = open('../data/ftest2.txt', 'w')
    file3.write('my first text~~')
    file3.close()

    # 3. 파일 덮어쓰기
    file4 = open('../data/ftest2.txt', 'a')
    file4.write('\nmy second text~~')
    file4.close()

    # 4. read
    '''
    file.read() : 전체 문서 한 번에 읽기
    file.readline() : 전체 문서에서 한 줄 읽기
    file.readlines() : 전체 문서를 줄 단위 읽기
    '''

    file5 = open('../data/ftest2.txt', 'r')
    print('A: ' + '-' * 50)
    print(file5.read())
    print('B: ' + '-' * 50)
    file5.close()

    file5 = open('../data/ftest2.txt', 'r')
    print(file5.readline())
    print('C: ' + '-' * 50)
    file5.close()

    file5 = open('../data/ftest2.txt', 'r')
    rows = file5.readlines()
    print(rows)
    print('D: ' + '-' * 50)
    file5.close()

    # 5. strip
    # string.strip() : 문장 끝 불용어(공백, /n, /t 기타) 제거
    print('strip 함수')
    for i in rows:
        print(i.strip())

    str_text = 'qwer1234\n \t\r'
    print(str_text.strip())

    # 6. with
    with open(file='../data/ftest3.txt', mode='w', encoding='utf-8') as file6:
        file6.write('파이썬 파일 작성 연습1\n')
        file6.write('파이썬 파일 작성 연습2\n')
    with open(file='../data/ftest3.txt', mode='r', encoding='utf-8') as file7:
        print(file7.read())


except FileNotFoundError as e:
    print(f'Error : {e}')
finally:
    pass
