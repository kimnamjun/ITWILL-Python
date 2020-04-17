'''
csv, excel file read/write
- 컬럼 단위로 작성된 파일 유형

cmd 에서 외부 라이브러리 설치
pip install [패키지명]
'''

from re import sub
import os
import pandas as pd

print(os.getcwd())

# 1. csv file read
spam_data = pd.read_csv('../data/spam_data.csv', header=None, encoding='MS949')
print(spam_data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5 non-null      object
 1   1       5 non-null      object
dtypes: object(2)
memory usage: 208.0+ bytes
None
'''
print(spam_data)


# 2. x, y 변수 선택
target = spam_data[0]  # DF[컬럼명]
text = spam_data[1]

print(target)
print(text)


# 3. target -> dummy
target = [1 if x == 'spam' else 0 for x in target]
print(target)


# 4. 텍스트 전처리
clean_texts = [' '.join(sub(r'[a-zA-Z\d.,;:?!@#$%^&*()]+', '', t).split()) for t in text]
print('텍스트 전처리 후')
print(clean_texts)


########################
## bmi.csv
########################

# 1. csv file read
bmi = pd.read_csv('../data/bmi.csv', encoding='UTF-8')
print(bmi.info())
print(bmi.head())
print(bmi.tail())

height = bmi['height']
weight = bmi['weight']
label = bmi.label  # 이런 것도 가능 / 컬럼명 지을 때 기존 멤버와 겹치지 않게 조심해야 할 듯

print(len(height))
print(len(label))

print(f'키 평균 : {height.mean()}')
print(f'몸무게 평균 : {weight.mean()}')

max_h = max(height)
max_w = max(weight)
print(f'max_h = {max_h}, min_w = {max_w}')

height_norm = height / max_h
weight_norm = weight / max_w

# 범주형 변수 : label
lab_cnt = label.value_counts()  # 빈도수 (범주형)
print(lab_cnt)


# 2. excel file read
'''
pip install xlrd
'''
excel = pd.ExcelFile('../data/sam_kospi.xlsx')  # xlrd 필요
print(excel)  # object info
kospi = excel.parse('sam_kospi')  # sheet
print(kospi)


# 3. csv file save
kospi['Diff'] = kospi.High - kospi.Low  # 파생 변수
print(kospi.info())

# csv 파일 저장
kospi.to_csv('../data/kospi_df.csv', index=None, encoding='UTF-8')

kospi_df = pd.read_csv('../data/kospi_df.csv', encoding='UTF-8')
print(kospi_df.head())