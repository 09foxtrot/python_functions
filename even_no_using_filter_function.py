def even(a):
    b=list(filter(lambda x:x%2==0,a))
    return b
a=list(map(int,input().split()))
print(even(a))
