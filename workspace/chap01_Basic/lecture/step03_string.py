# 문자열 처리
# - 문자열(string) : 문자들의 순서(index) 집합
# - indexing slicing 가능
# - 문자열 = 상수 : 수정이 불가능

# 1. 문자열 처리

# 1) 문자열 유형
line_str = "this is one line string"  # 한 줄 문자열
print(line_str)

multi_str = '''this
is multi line
string'''
print(multi_str)

multi_str2 = 'this\nis multi line\nstring'
print(multi_str2)

# sql문 : 부서번호
deptno = int(input('부서번호 입력 : '))
query = f"""SELECT *
FROM emp
WHERE deptno = {deptno}
ORDER BY sel DESC"""
print(query)

# 2) 문자열 연산(+, *)
print('python ' + 'program')
print('python ' + str(37))
print('-' * 30)

'''
object.member or object.member()
int.member
str.member
'''

# 3) 문자열 처리 함수
print(line_str, type(line_str)) # 내용, 자료형 출력
# this is one line string <class 'str'>
print('문자열 길이 :', len(line_str))
print('t의 글자수 :', line_str.count('t'))

# 접두어 : 시작 문자열
print(line_str.startswith('this'))  # True
print(line_str.startswith('that'))  # False
words = line_str.split(sep=' ')
print(words)
print('단어 길이 :', len(words))

# 문단 -> 문장
sentence = multi_str.split(sep='\n')
print(sentence)
print('문장 길이 :', len(sentence))
print(multi_str.upper())

# 4) indexing / slicing
print(line_str)
print(line_str[0])
print(line_str[-1])
print(line_str[0:4])
print(line_str[0:-6])