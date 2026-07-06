#https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
def gimme(input_array):
    a=sorted(input_array)
    for i in range(len(input_array)):
        if input_array[i]==a[1]:
            return i