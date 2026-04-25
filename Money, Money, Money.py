#https://www.codewars.com/kata/563f037412e5ada593000114/train/python
def calculate_years(principal, interest, tax, desired):
    def calculate_amount(principal, interest, tax):
        return principal + (principal * interest) - (principal * interest * tax)
    years = 0
    while principal < desired:
        principal = calculate_amount(principal, interest, tax)
        years += 1
    return years
