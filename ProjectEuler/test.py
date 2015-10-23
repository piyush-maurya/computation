__author__ = 'piyush'

k = int(input())

n = []
for i in range(k):
    n.append(int(input()))

for i in range(k):
    n1 = int((n[i]-1)/3)
    n2 = int((n[i]-1)/5)
    n3 = int((n[i]-1)/15)
    sum1 = (n1*(6+(n1-1)*3))>>1
    sum2 = (n2*(10+(n2-1)*5))>>1
    sum3 = (n3*(30+(n3-1)*15))>>1
    sum4 = sum1+sum2-sum3
    print(sum4)