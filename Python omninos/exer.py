import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("listening")
    r.pause_thresold=0.5
    audio=r.listen(source)
try:
    print("recongnise")
    query=r.recognize_google(audio,language='en-in')
    print(f'user said:{query}\n')
except Exception as e:
    print('say that again')
pip2.7 install pyaudio