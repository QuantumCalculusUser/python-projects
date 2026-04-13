# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python
# https://github.com/QuantumCalculusUser/python-projects
def last_digit(lst):
    if not lst:
        return 1

    exponent = 1

    for value in reversed(lst[1:]):
        power = exponent if exponent < 4 else exponent % 4 + 4
        exponent = pow(value, power)
        if exponent > 4:
            exponent = exponent % 4 + 4

    return pow(lst[0] % 10, exponent, 10)
