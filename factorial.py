n=int(input("Your number :"))
if n<0:
    print("Only integers can give factorials")
elif n==0:
    print("Only integers can give factorials")
elif n==1:
    print("Its factoral is 1")
else :
    n>=1
    fact=1
    while n >1:
     fact=fact*n
     n=n-1
print("Your factorial is ", fact)