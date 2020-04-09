from re import sub
# from package module import class or function
# from module import class or function

# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

# 1. 소문자 변경
text_result1 = [text.lower() for text in texts]
print(' 소문자로 변경 :', text_result1)

# 2. 숫자 제거
text_result2 = [sub(r'\d', '', text) for text in text_result1]
print('     숫자 제거 :', text_result2)

# 3. 문장 부호 제거
punc_str = '[.,;:?!]'
text_result3 = [sub(punc_str, '', text) for text in text_result2]
print('문장 부호 제거 :', text_result3)

# 4. 특수 문자 제거
spec_str = '[!@#$%^&*()]'
text_result4 = [sub(spec_str, '', text) for text in text_result3]
print('특수 문자 제거 :', text_result4)

# 5. 공백 제거 : 'abtta a' -> ''.join('abtta', 'a')
text_result5 = [''.join(text.split()) for text in text_result4]
print('     공백 제거 :', text_result5)


# 텍스트 전처리2
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
