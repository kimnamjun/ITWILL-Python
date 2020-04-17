'''
json 파일 2가지 형식
1. 중괄호 : {key: value, ...}, {key: value, ...}
    -> json.loads(row)
2. 대괄호 : [ {key: value, ...}, {key: value, ...} ]
    -> json.load(row)  # 함수가 다름
'''
import json
import pandas as pd

# 1번 형식 : {key: value, ...}, {key: value, ...} : step05 참고 / 이하 생략

# 2번 형식 : [ {key: value, ...}, {key: value, ...} ]
with open('../data/labels.json', encoding='UTF-8') as file:
    # print(file.read())
    rows = json.load(file)

print(len(rows))
print(rows)

for row in rows[:5]:
    print(row)
    print(type(row))

# list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
print(rows_df.head())


# pickle
'''
python object(list, dict) -> file(binary) -> python object(list, dict)
'''
import pickle
'''
pickle은 list, dict 뿐 아니라 모든 object에 대해 바이너리 데이터로 변환 가능
save : pickle.dump(data, file)
load : pickle.load(file)
'''
with open('../data/row_data.pik', mode='wb') as file1:  # mode='wb' : write binary
    pickle.dump(rows, file1)  # list -> binary
    print('pickle file saved')

with open('../data/row_data.pik', mode='rb') as file2:
    rows_data = pickle.load(file2)
    print(rows_data)
    print(type(rows_data))