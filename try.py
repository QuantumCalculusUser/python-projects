from itertools import permutations

num=[1,2,3]
a=tuple(num)
num.sort()
l=list(permutations(num))
print(num,a)
print(l)
print("excute 1")
if a==l[-1]:
    print("excute 2.1")
    print(l[0])
else:
    print("excute 2.2")
    for i in range(len(l)):
        if a==l[i]:
            print("exutee 2.21")
            print(l[i+1])
print("excute complete")