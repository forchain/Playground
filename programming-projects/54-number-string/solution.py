def expanded_form(number: int) -> str:
    digits = str(number)
    terms = [digit + '0' * (len(digits) - index - 1)
             for index, digit in enumerate(digits) if digit != '0']
    return ' + '.join(terms) if terms else '0'
