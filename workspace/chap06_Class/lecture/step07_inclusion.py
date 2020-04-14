'''
1. private 변수 : 클래스 내의 은닉 변수
- object.member : 객체 -> 은닉 변수 (X)
- getter() / setter() -> 은닉 변수 (O)
2. class 포함 관계 (inclusion)
- 특정 객체가 다른 객체를 포함하는 클래스 설계 기법
- 두 객체 간의 통신 지원
- ex) class A(a) -> class B(b)
'''


# 1. private 변수
class Login:
    def __init__(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd

    def getIdPwd(self):
        return self.__dbId, self.__dbPwd

    def setIdPwd(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd


# object
login = Login('hong', '1234')
# object.member
print(login._Login__dbId)

login.setIdPwd('lee', '2345')

uid, pwd = login.getIdPwd()
print(uid, pwd, sep=', ')


# Server <-> Login
class Server:
    def send(self, obj):
        self.obj = obj

    def cert(self, uid, upwd):
        dbId, dbPwd = self.obj.getIdPwd()
        if dbId == uid and dbPwd == upwd:
            print('로그인 성공 ㅎㅎ')
        else:
            print('로그인 실패 ㅠㅠ')
