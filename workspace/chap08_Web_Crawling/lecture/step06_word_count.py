'''
1. pickle file load
2. 텍스트 전처리
3. word count
'''
import pickle
from re import sub

# 1. pickle file load
with open('../data/news_crawling.pickle', mode='rb') as file:
    news_crawling = pickle.load(file)

# 2. 텍스트 전처리
clean_news = [' '.join(sub(r'[.,;:?!@#$%^&*()\'\"]+', '', x).lower().split()) for x in news_crawling]

# 3. word_count
word_count = dict()
for texts in clean_news:
    for word in texts.split():
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)

word_count2 = word_count.copy()  # 객체 복제

# 4. 2음절 이상 단어 선택
for word in word_count.keys():
    if len(word) < 2:
        del word_count2[word]

del(word_count2['[바로잡습니다]'])
print(word_count2)

# 5. top10, top5
'''
pip install collections-extended
'''
from collections import Counter

count = Counter(word_count2)

top5 = count.most_common(5)
print(top5)

top10 = count.most_common(10)
print(top10)

# 6. data frame
import pandas as pd
top10_df = pd.DataFrame(top10, columns=['word','count'])
print(top10_df)

# 7. 시각화
'''
pip install matplotlib
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 선 그래프
plt.plot(top10_df['word'], top10_df['count'])
plt.title('top10 word count')
plt.show()

# 막대 그래프
plt.bar(top10_df['word'], top10_df['count'])  # 세로 막대 차트
# plt.barh : 가로 막대 차트
plt.title('top10 word count')
plt.show()
