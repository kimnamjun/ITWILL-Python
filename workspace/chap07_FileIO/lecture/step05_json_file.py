'''
JSON 파일
- 네트워크에서 표준으로 사용되는 파일 형식
- 파일 형식 : {key:value, key:value}, {key:value, key:value}
               1행                     2행
- 활용 예 : 서로 다른 플랫폼(java, python)에서 파일 공유

- json 모듈
1. encoding : file save : python object(list, dict) -> json file
2. decoding : file read : json file -> python object(list, dict)
'''
import json

# 1. encoding
'''
python object -> json 문자열 -> file save
형식) json.dumps(object)
'''
user = {'id': 1234, 'name': '홍길동'}
print(type(user))

json_str = json.dumps(user, ensure_ascii=False)  # unicode -> ascii 인코딩 안함
print(json_str)        # 모양은 dict 비슷하나
print(type(json_str))  # 타입은 str임


# 2. decoding : 문자열 -> object
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''
py_obj = json.loads(json_str)
print(py_obj)
print(type(py_obj))


# 3. json file read/write

# 1) json file read : decoding
import os
print(os.getcwd())

with open('../data/usagov_bitly.txt', encoding='UTF-8') as file:
    data = file.readlines()

rows = [json.loads(row) for row in data]  # row = {key:value, key:value}
print(len(rows))

for row in rows[:10]:
    print(row)

# json object -> data frame
import pandas as pd
rows_df = pd.DataFrame(rows)
print(rows_df.info())
print(rows_df.head())
print(rows_df.tail())

# 2) json file wirte : encoding
with open('../data/json_text.txt', mode='w', encoding='UTF-8') as file:
    for row in rows[:100]:
        json_str = json.dumps(row)
        file.write(json_str + '\n')
print('~~ 파일 저장 완료 ~~')