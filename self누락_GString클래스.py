#전역변수

str = "Not Class Member"
class GString:
    def __init__(self):
        #멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #self누락 클래스 변수가 아닌 글로벌 변수로 불러옴
        print(self.str) 

g = GString()
g.set("First Message")
g.print()
