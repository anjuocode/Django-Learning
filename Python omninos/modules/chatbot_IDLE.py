#import pyttsx3
import os
import datetime
import webbrowser
import smtplib
'''
engine = pyttsx3.init()

def speak(audio):
    #engine.say(audio)
    engine.runAndWait()
'''
print("How May I help You ")
#speak("How May I help You !")


while True :
    #speak("Enter The Service !")
    print()
    n = str(input("Enter The Service Name : "))
    terminal = n.lower()


    if 'terminal' in terminal:
        os.system('chrome')

    elif 'facebook' in terminal:
        os.system('https://www.facebook.com')

    elif ('youtube'in cmd) or ('youtube' in cmd):
        os.system('chrome https://www.youtube.com')

    elif ('vs code' in cmd) or ('vscode' in cmd):
        os.system('code')

    elif 'folder' in cmd:
        os.system('/Users/aryan/Desktop/aryan.jpg')

    elif 'music' in cmd:
        os.system('C:/Users/ravan/Music/audio.mp3')

    elif 'browser' in cmd:
        webbrowser.open('https://www.google.co.in')
        #webbrowser.open_new('http://www.google.co.in') #open in new browser window
        #webbrowser.open_new_tab('http://www.google.co.in') # open in new tab
        

    elif 'time' in cmd:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("The Time is : {0} ".format(strTime))
        #speak("The Time IS {0} ".format(strTime))

    elif 'mail' in cmd:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("example@gmail.com","ravan@123")
        message = input("Enter MSG you Want To Send : ")
        s.sendmail("example@gmail.com", "example@gmail.com" ,message)
        s.quit()
        

    elif ('exit' in cmd ) or ('quit' in cmd ):
        print("Bye Bye You Are Out from The Program")
        break

    else:
        print("Invalid Command ")
        #speak("invalid command")
