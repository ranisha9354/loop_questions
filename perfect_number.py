a=int(input("Enter the number:"))
i=1
sum=0
while i<a:
    if a%i==0:
        sum=sum+i
    i=i+1
if sum==a:
    print("it is perfect number")
else:
    print("it is not perfect number")