i=1
while i <=10:
    if i%2==0:
        i+=1
        continue
    a=i*'*'
    print(a.center(30,' '))
    i+=1
