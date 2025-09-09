n=int(input('enter no of rows: '))
stars=5
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars-=1
    
