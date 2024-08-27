for x in range(2,20):
    t=2
    for y in range(2,x):
        t=y
        if x%y==0:
            break
    if t==x-1:
        print(x)        