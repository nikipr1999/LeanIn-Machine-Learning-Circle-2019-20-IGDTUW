import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as audio:
    print('Speak Anything:')
    audio=r.listen(source)
    
    try:
        text=r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print("Sorry can't show the text. :P")