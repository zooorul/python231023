#web1.py
#웹크롤링
from bs4 import BeautifulSoup

#페이지 로딩
#함수 Chain = Open 후 바로 Read(연속해서 작성)
page = open("c:\\work\\test01.html","rt",encoding ="utf-8").read() 
#검색이 용이한 객체 생성
#html, image, javascript 섞여 있음 "html.parser" 부분이 상수임
#XML(데이터 저장, 교환) -> 엑셀 문서 쓸 때 사용
soup = BeautifulSoup(page, "html.parser")
#전체 보기
# print(soup.prettify())
#<p>태그 전체를 검색
# print(soup.find_all("p"))
# print(soup.find("p"))
#<p class ="outer-text">형태만 검색
#print(soup.find_all("p",class_="outer-text"))
#attrs를 사용(Attributes)
#print( soup.find_all("p",attrs={"class":"outer-text"}) )
#특정 태그만 지정할 경우 id 속성
#print(soup.find_all(id="first"))
#태그 내부의 컨텐츠를 가져오기: .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)

