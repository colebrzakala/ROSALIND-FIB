def rabbitpairs(n,k):
    if ((n==1) or (n==2)):
        return 1
    else:
        return (rabbitpairs(n-1,k)) + (k*rabbitpairs(n-2,k))
