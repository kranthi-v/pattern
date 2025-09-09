n=int(input('enter no of rows: '))
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end= '')
        if row <= n//2:
            stars+=2
            spaces-=1
        else:
            stars-=2
            spaces+=1
    print()