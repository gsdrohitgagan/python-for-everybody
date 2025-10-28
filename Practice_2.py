#To count number of characters in a text using Tuples

inp=input('Enter the text:')
c=''
char=''
max=0
list=[]
for a in inp:
    n=0
    k=1
    for x in c:
        if x==a:
            k=0
            #quit()
    if k==1:
        for b in inp:
            if a==b:
                n=n+1

            if n>max:
                max=n
                char=b
        c=c+a
        list.append((a,n))
        
        
print('Most repeated letter is:',char,'Repeated:',max)    
list= sorted(list)
#print(list)
for i,j in list:
    print(i,j)
