def validate_coupon(code: str) -> str:
    valid = 10 <= len(code) <= 12
    valid = valid and code[:3].isalpha() and code[:3].isupper() and len(set(code[:3])) == 3
    valid = valid and code[3:7].isdigit() and 1900 <= int(code[3:7]) <= 2019
    valid = valid and code[-1].isalpha() and code[-1].isupper()
    valid = valid and code[7:-1] in {'10','20','50','100','200','500','1000'}
    return code[0] if valid else code[-1]
