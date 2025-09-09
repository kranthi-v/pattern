n=int(input('enter no of rows: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col  or row+col == 6:
            print('*',end='')
        else:
            print(' ',end='')
    print()
