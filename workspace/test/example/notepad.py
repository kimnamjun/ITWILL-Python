# 욱성이 형 코드

a = [[1,500],[3,300],[6,200],[10,50],[15,30],[21,10]]
b = [[1,512],[3,256],[7,128],[15,64],[31,32]]

a = sorted(a,key = lambda a:a[0],reverse=True)
b = sorted(b,key = lambda a:a[0],reverse=True)

num = int(input())

answer_list = list()
for i in range(num):
    tmp1 , tmp2 = map(int,input().split())
    t1 = 0
    t2 = 0
    answer = 0

    for j in range(6):
        if a[j][0] >= tmp1:
            t1=j

    for j in range(5):
        if b[j][0] >= tmp2:
            t2=j

    if tmp1 != 0:
        answer += a[t1][1]

    if tmp2 != 0:
        answer += b[t2][1]

    answer = answer * 10000
    answer_list.append(answer)

for i in answer_list:
    print(i)