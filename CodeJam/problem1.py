t = int(input())
for _ in range(t):
    n = int(input())
    m = [[0 for j in range(n)] for i in range(n)]
    trace = 0
    row = 0
    column = 0
    for i in range(n):
        m[i] = list(map(int, input().split()))
        trace += m[i][i]
    for i in range(n):
        dict_1 = {}
        for j in range(n):
            if dict_1.get(m[i][j]):
                dict_1[m[i][j]] += 1
            else:
                dict_1[m[i][j]] = 1 
        if(max(dict_1.values()) > 1):
            row += 1

    for i in range(n):
        dict_1 = {}
        for j in range(n):
            if dict_1.get(m[j][i]):
                dict_1[m[j][i]] += 1
            else:
                dict_1[m[j][i]] = 1 
        if max(dict_1.values()) > 1:
            column += 1
    print("Case #"+str(_ + 1)+":",trace,row,column)