def intToBin(n):
    return str(bin(n))[2:]


def binToInt(s):
    return int(s,2)


#kth bit set from right
def kthbit(n, k ):
    print(str(bin(n))[2:])
    if n & (1 << (k - 1)):
        print('SET')
    else:
        print('NOT SET')

#[5,3,2,3,2,1,5]
# Every number occurs twice
# we need to find the number which occurs only once
# n ^ n = 0
# n ^ 0 = n
def findsingleoccur(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = result ^ arr[i]
    return result

t = int(input())
while t:
    # n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    #binstring = intToBin(n)
    #integer = binToInt(binstring)
    #print(n,binstring,integer, n == integer)
    print(findsingleoccur(arr))

    t = t - 1