def max_sum(a,n):
    arrSum = sum(a)
    init ,res = 0, 0
    for i in range(n):
        init += i*a[i]
    res = init
    for i in range(1, n):
        init = init - (arrSum - a[i - 1]) + ((n-1)*a[i-1])
        res = max(res, init)
    return res
