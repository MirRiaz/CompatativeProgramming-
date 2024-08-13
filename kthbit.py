def kthbit(n, k):
    print(str(bin(n))[2:])
    if n & (1 << (k - 1 )):
       print("SET")
    else:
        print("NOT SET")

t = int(input())

while t:
    n, k = map(int,input().split())
    kthbit(n, k)
    t = t - 1