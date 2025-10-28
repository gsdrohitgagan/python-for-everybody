#Print all the prime numbers below a given number

x=int(input('Enter Range:'))
count=0
for y in range(2,x+1):
    k=1
    for z in range(2,y):
        if y%z==0:
            k=0
            break
    if k!=0:
        print(y)
        count=count+1
print('Total Prime Numbers', count)
        
