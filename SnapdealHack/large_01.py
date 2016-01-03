k = [int(i) for i in input().split()]
n = [int(i) for i in input().split()]
q = [[0 for i in range(3)]for j in range(k[1])]
for j in range(int(k[1])):
    q[j] = [int(i) for i in input().split()]
for i in range(int(k[1])):
    x = int(q[i][0])
    m = int(q[i][1])
    t = int(q[i][2])
    for j in range(k[0]):
        if t == 0:
            if n[j] > x:
                if int(k[0])-j < m:
                    print(-1)
                else:
                    print(n[j+m-1])
                break
        if t == 1:
            if n[j] >= x:
                if j < m:
                    print(-1)
                else:
                    print(n[j-m])
                break


