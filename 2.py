a=eval(input())
count=0
c=0
while count < a:
    b=eval(input())
    c=(b+c*count)/(count+1)
    count=count+1
else :
    c=(c*count-1)/(count+1)
print (c)
