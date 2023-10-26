import re

# 정규 표현식 패턴 (이메일 주소 검사)
#r(raw string notation)
pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$'

# 예시 이메일 주소
sample_emails = [
    "user@example.com",
    "john.doe1234@gmail.com",
    "info@company.co.uk",
    "invalid-email",
    "user@.com",
    "user@company.",
    "@example.com",
    "user@-website.com",
    "user@company.c",
    "user@company.123"
]

for email in sample_emails:
    if re.search(pattern, email):
        print(f"{email} 는 유효한 이메일 주소입니다.")
    else:
        print(f"{email} 는 유효하지 않은 이메일 주소입니다.")
