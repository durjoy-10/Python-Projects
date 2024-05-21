email=input("Enter your Email:") #g@g.in
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):#XOR operator
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i==i.isalpha():
                        j=1
                    elif i==i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d==1 
                if k==1 or j==1 or d==1:
                     print("Wrong email 5")
                else:
                    print("Right email")
            else:
                print("Wrong email 4")
        else:
            print("Wrong Email 3")
    else:
        print('Wrong Email 2')        
else:
    print("Wrong Email 1")