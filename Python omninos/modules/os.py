'''import os
import platform
cmd = "Notes"
platform.system()
os.system(cmd)
import os
import smtplib

while True:
    n = str(input("Enter The Service Name : "))
    terminal = n.lower()

    if 'make' or "made":
        cmd=os.mkdir(input('enter the value'))
        print(cmd)

    elif 'mail' or 'email':
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("example@gmail.com","ravan@123")
        message = input("Enter MSG you Want To Send : ")
        s.sendmail("example@gmail.com", "example@gmail.com" ,message)
        s.quit()

'''
import os
import sys
import subprocess
subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python', '--args', 'bb.py'])
subprocess.call('/System/Applications/Utilities')
