def solution(num):
    x = [4, 16, 37, 58, 89, 145, 42, 20]
    while True:
        s = 0
        for i in str(num):
            s += int(i)**2
        if s in x:
            return False
        elif s == 1:
            return True
        num = s 

n = int(input())
print(solution(n))