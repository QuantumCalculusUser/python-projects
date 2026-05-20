# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python
def divisors(n):
    a=1
    for i in range(1,n):
        if n%i==0:
            a+=1
    return a