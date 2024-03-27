from sys import stdin
input = stdin.readline


for i in range(int(input())):
    l = list(map(int, input().split()))
    s = l[1:]
    avg = sum(s)/l[0]
    st = 0
    for e in s:
        if e > avg:
            st += 1
    print(f"{st/l[0]*100:.3f}%")

