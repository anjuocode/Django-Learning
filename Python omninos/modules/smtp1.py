import smtplib
sender_email="anju500918@gmail.com"
rec_email="anjukargwaal@gmail.com"
password=input(str("Enter your password"))
message="Hii, How are you?"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email,password)
print("Log in Success")
server.sendmail(sender_email,rec_email,message)
print("Email has been sent to",rec_email)
