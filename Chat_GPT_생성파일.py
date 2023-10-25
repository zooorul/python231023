class Person:
    def __init__(self, name, id_number, phone_number):
        self.name = name  # 이름
        self.id_number = id_number  # 신분증 번호
        self.phone_number = phone_number  # 전화 번호

    def printinfo(self):
        print(f"name: {self.name}")
        print(f"id_number: {self.id_number}")
        print(f"phone_number: {self.phone_number}")

class Manager(Person):
    def __init__(self, name, id_number, phone_number, skill):
        super().__init__(name, id_number, phone_number)
        self.skill = skill  # 기술

    def printinfo(self):
        super().printinfo()
        print(f"skill: {self.skill}")

class Employee(Manager):
    def __init__(self, name, id_number, phone_number, skill, title):
        super().__init__(name, id_number, phone_number, skill)
        self.title = title  # 직급

    def printinfo(self):
        super().printinfo()
        print(f"title: {self.title}")

# 이 클래스들을 생성하고 사용하는 샘플 코드:
if __name__ == "__main__":
    person = Person("홍길동", "12345", "555-123-4567")
    person.printinfo()

    manager = Manager("이영희", "67890", "555-987-6543", "프로젝트 관리")
    manager.printinfo()

    employee = Employee("김철수", "13579", "555-555-5555", "코딩", "소프트웨어 엔지니어")
    employee.printinfo()