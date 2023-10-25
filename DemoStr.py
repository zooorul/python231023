# DemoStr.py
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.count("p"))
print(strB.count("p",7))
print(strB.startswith("python"))
print(strB.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())
#앞뒤에 공백문자 제거 -> 나중에 데이터 처리 시 앞/뒤 공백 제거하는 전처리 작업 진행함(데이터 多)
data = "<<< spam and ham >>>"
result = data.strip("<> ") # <> 앞뒤에 오는 <, > 제거할 수 있음
print(data)
print(result)
result2 = result.replace("spam","spam egg")
print(result2)
#화이트 스페이스(공백문자)
lst = "spam::egg::ham"
lst = result2.split("::")
print("리스트:",lst)

print("---다시 합치기---")
print(":)".join(lst))

