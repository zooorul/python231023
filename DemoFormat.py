# DemoFormat.py

for x in range(1,6) :
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6) :
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0을 출력---")
for x in range(1,6) :
    print(x,"*",x,"=",str(x*x).zfill(5))
    
for i in range(1,11) :     
    url = "http://www.multicampus.com/?page=" + str(i)
    print(url)

print("---서식 지정---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

#파일 쓰기
f = open("demo.txt","wt", encoding = "utf-8") 
#encoding은 지정 안해도 됨. 다만 영문, 독일  윈도우 사용하는 경우가 있어서 
#utf-8이라고 습관적으로 지정해주기(utf-8 = uni-code라는 뜻)
f.write("첫번째\n두번째\n세번째\n") 
f.close()

#파일 읽기
f = open("demo.txt", "rt", encoding = "utf-8")
result=f.read()
print(result)

#처음으로 리셋
f.seek(0)
print(f.readline(),end="")
print(f.readline(),end="")

f.seek(0)
lst = f.readlines()
for item in lst:
    print(item,end="")
#print 함수는 끝에 \n이 고정적으로 들어가 있음.
#따라서 end=""을 추가해줘서 \n이 고정 값으로 들어가지 않도록 함.
    
f.close() # close 안하면 다른 여러 사용자가 사용할 때 문제가 생길 수 있음.

