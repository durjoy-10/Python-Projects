# import smtplib 
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
# # obj= s.SMTP('smtp.gmail.com',587) #connect to gmail surver
# # obj.ehlo() #surver connection
# # obj.starttls() #another surver connection
#     Sender_address=input("Enter your mail address:")
#     Sender_mail_pass=input("Enter your mail pass:")
#     server.login("Sender_address","Sender_mail_pass")
#     subject=input("Enter the subject of your mail: ")
#     body=input("Enter the mail body:")
#     message="subject:{}\n\n{}:".format("subject","body")
#     n=input("How many persons do you want to send the mail?")
#     receiver_list=[]
    
#     for i in range(0,n):
#         receiver_address=input("Enter"+(i+1)+"th mail address:")
#         receiver_list.append(receiver_address)
    
#     server.sendmail(Sender_address,receiver_list,message)
    
#     print("Mail send successfully")
#     server.quit()

import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('ug2102017@cse.pstu.ac.bd','UG2102017@cse.pstu.ac.bd')
subject="test python"
body="I love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=[
    'prajapatgaurav08@gmail.com',
    'prajapatgaurav601@gmail.com'
]
ob.sendmail('ug2102017@cse.pstu.ac.bd',listadd,message)
print("Mail send successfully")
ob.quit()