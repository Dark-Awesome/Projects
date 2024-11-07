import smtplib as smt 


def sendmail(sender_mail,sender_password,message,receiver_mail):
    #senders id should have security on less safe app ON.

    #here server s is only for gmail servers 
    s = smt.SMTP("smtp.mail.yahoo.com", 465)
    s.starttls
    s.login(sender_mail, sender_password)
    s.sendmail(sender_mail, receiver_mail , message)
    s.quit()

def send_to_all(sender_mail, sender_password,message,listofrecievers):
    for i in range(len(listofrecievers)):
        sendmail(sender_mail, sender_password,message,receiver_mail=listofrecievers[i])

sendmail("----------","-----------","hello shubhu", "________")

# Server name: smtp.mail.yahoo.com

# Port: 465

# SSL or TLS: ON

