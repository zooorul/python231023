# DemoDict.py(딕셔너리)

phone = {"kim":"1111","lee":"2222","park":"3333"}
print(phone)
print(len(phone))
print(phone["kim"])
#include의 약자(멤버십)
print("park" in phone)
print("kang" not in phone)

#항상 객체의 참조가 전달된다.
# p = phone은 값을 복사시키는 것이 아니라 같은 곳을 참조하도록 하는 것임!!!!
p = phone 
p["kang"] ="1234"
print(p)
print(phone)
print( id(phone),id(p)) # 같은 ID를 보고 있음을 확인할 수 있음

#장비 관리
device = {"아이폰" : 5,"아이패드":20}
print(device["아이폰"])
#입력
device["맥북"] = 15
#수정
device["아이폰"] = 6
print(device)
#삭제
del device["아이폰"]
print(device)

for item in device.items() :
    print(item)
for item in device.keys() :
    print(item)
for item in device.values() :
    print(item)    

print(bool(0))
print(bool(3))
print(bool(""))
print(bool("test"))
print(bool({}))
print(bool({1,2,3}))
print("---논리식---")
print(1<2)
print(1 != 2)
print(1==2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
print( 5 / 2 )
print( 5 // 2 )
print( 5 % 2 )