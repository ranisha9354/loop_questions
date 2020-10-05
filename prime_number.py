i=1
while i<=100:
    a=2
    while a<i:
        if i%a==0:
            print(i," it is not priem number")
            break
        a=a+1
    else:
        print(i,"it is priem numbe")
    i=i+1         

