#smtp
import smtplib
sender_email = "anju500918@gmail.com"
rec_email = "anju500918@gmail.com"
password = input(str("please enter ur password"))
message = input(str("please enter ur message"))


server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, rec_email, message)
print("email has been sent to ", rec_email)

