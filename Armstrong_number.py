a=int(input("Enter the num:"))
i=0
sum=0
n=a
while i<3:
    b=a%10
    var=b**3
    sum=sum+var
    a=a//10
    i=i+1
if sum==n:
    print("it is armstrong num")
else:
    print("it is not armstrong num")


# slove second way:--

number = int(input("Enter the number : "))
sum = 0
i = 0
var = number
while var != 0:
    var =int(var / 10)
    i = i + 1
var = number
while var != 0:
    remainder = var % 10
    sum = sum + pow(remainder, i)
    var = int(var/10)
if sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# third_type_slove:-

a=int(input("Enter the num:"))
i=0
sum=0
n=a
l=len(str(a))
while i<l:
    b=a%10
    var=b**(l)
    sum=sum+var
    a=a//10
    i=i+1
if sum==n:
    print("it is armstrong num")
else:
    print("it is not armstrong num")

