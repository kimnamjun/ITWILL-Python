# 변수(Variable)
# - 형식) 변수명 = 값 or 수식 or 변수명
#  - 자료를 저장하는 메모리 이름
# - type 선언 없음(R 동일)

# 1. 변수와 자료
var1 = 'Hello Python'
var2 = 'Hello Python'
print(var1)
print(var2)
print(type(var1), type(var2))

var1 = 100
print(var1, type(var1))

var3 = 150.25
print(var3, type(var3))

var4 = True
print(var4, type(var4))

# 2. 변수명 작성규칙(p11 참조)
_num10 = 10
_NUM10 = 20
print(id(_num10), id(_NUM10))

# 키워드 확인
import keyword
py_keyword = keyword.kwlist
print(py_keyword)
print(len(py_keyword))

# camel case
korScore = 90
matScore = 85
engScore = 75
tot = korScore + matScore + engScore
print(tot)

# 3. 참조변수 : 메모리 객체(value)를 참조하는 주소 저장 변수
x = 150 # 객체의 주소
y = 45.23
y2 = y # 변수 복제 (주소 복제)
x2 = 150 # 기존 객체 있으면, 주소 반환

print(x, y, y2, x2)
print(id(x), id(y), id(y2), id(x2))