# func1.py
#함수 정의
def setValue(newValue) :
    #지역변수 초기화
    x = newValue
    print(x)
# 흰색 줄로 함수가 어디까지인지 확인할 수 있음.    
    
#함수 호출
setValue(5)

#값을 리턴하는 함수
def swap(x,y) :
    return y,x

#함수 호출
result = swap(5,6)
print(result)
