# 이메일주소체크.py

import re

# 정규 표현식 패턴
#r(raw string notation)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# 이메일 주소를 검사할 텍스트
text = """
이메일 주소 목록:
1. abc@example.com
2. john.doe@my-company.net
3. user@subdomain.domain.co.uk
4. invalid_email.com
5. no@tld.
6. @startwithat.com
7. spaces in@username.com
8. special_characters!$%@domain.com
9. missing_domain@example.
10. 이것은 한국어 주소 test@한글주소.com
"""

# 정규 표현식을 사용하여 이메일 주소 검색
emails = re.findall(email_pattern, text)

# 검색된 이메일 주소 출력
for i, email in enumerate(emails, start=1):
    print(f"{i}. {email}")
