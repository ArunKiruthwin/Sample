row=1
num=5
while row<=5:
    column=5
    while column>=row:
        print(num,end='')
        column=column-1
    print()
    row+=1
    num-=1