sum=0
i=1
while i<=11:
    user=int(input("Enter weight"))
    sum=sum+user
    average=sum//i
    i=i+1
if average%5==0:
    print(average,"This is divisiale by five")
else:
    print(average,"it is not divisible")
    

