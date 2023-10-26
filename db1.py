# Database(DB or RDB)

# 데이터베이스와 파이썬의 관계는, 파이썬이 데이터를 끌어올리는 느낌. 파이썬에서 작성된 쿼리를 DB로 떨구고, 해당하는 데이터를 파이썬으로 그대로 올림.
# 만약 DB 관련 경험이 없다면 , 오픈소스인 SQLite 공부해보는 것도 나쁘지 않다. 

#SQL 관련 언어설명
# - DDL (data definition language) : 데이터베이스의 객체를 생성,수정,삭제하는 언어 → Create, alter, drop .. 
# - DML (data manipulation language) : 데이터를 다루는 언어 → select update insert delete ... (=.CRUD)

# 목적은 파이썬에서 DB를 체계적으로 관리하는 것이므로, 파이썬에서 관련 SQL구문을 쓰고 / DB 를 다뤄보는 것이다. 실제 DB SW에 연동해서 하는 것

# sqlite 모듈 : DB 등 전역함수가 정의되어 있음. 
# 전역함수 : sqlite3.connect / sqlite3.complete_statement / sqlite3.register_adapter / sqlite3.register_converter....
# connection 클래스 : cursor / rollback / commit / close / execute...

# ? Java JDBC / ODBC → 1. connection class(연결 맺고끊는 작업) 2. Command class(실제 SQL 실행) 3. ResultSet class(결과 집합)
# ? C#/VB : 1. connection class(연결 맺고끊는 작업) 2. command class(실제 SQL 실행) 3. Dataset Class(결과 집합)
# ? Python : 1. Connection class(연결 맺고 끊는 작업) 2. Cursor Class (command + result class 통합의 역할) → 두 클래스만 배우면되니 훨씬 Simple 함.

# db1.py 
import sqlite3

#연결객체(일단은 메모리에 저장) 
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor()
#테이블 구조 생성
cur.execute("""create table if not exists PhoneBook  
    (id integer primary key autoincrement, name text, phoneNum text);
    """)

#1건입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('전우치','010-222');")

#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook (name, phoneNum) values (?,?);",
            (name,phoneNumber))

#다중으로 행을 입력 
#Tuple이 여러개 들어가면 행렬 개념으로 생각하면 된다.
datalist = (("박문수","010-333"),("김길동","010-567"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?,?);",
            datalist)

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---") # 하나씩 가져와서 루프로 보여줘도 됌
print(cur.fetchone())
print("---fetchmany(2)---") # 10개씩 덩어리로 끊어서 보여줄 수도 있음
print(cur.fetchmany(2))
print("---fetchall()---") # Data가 100, 1000건으로 적으면 fetchall로 다 가져옴
cur.execute("select * from PhoneBook;") #버퍼를 채워주는 것
print(cur.fetchall()) 
# 임시 메모리(휘발성) -> 데이터 가져오면 Buffer는 사라짐 -> DB에 저장해야함
    