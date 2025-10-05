inp= input('Enter File Name:')
hand= open(inp)
for line in hand:
    if line.startswith('From:'):
        line=line.replace('From:','') #to print just the email
        line=line.upper() #make it uppercase
        line=line.strip() #to remove the new line or space
        name=line.split('@')
        x=name[0]
        y=x.split('.')
        print('Email ID is:',line)
        print('First Name is:',y[0])
        if len(y)>1: #some don't have last name
            print('Last Name is:',y[1])
        
        