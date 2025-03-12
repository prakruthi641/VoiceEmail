try:
    from gtts import gTTS
    from playsound import playsound
    import speech_recognition as sr
    import random
    import os
    import SignUp as s
    import Login as l
except ModuleNotFoundError as e:
    print(f"Module not found: {e}. Please install missing dependencies using 'pip install gtts playsound SpeechRecognition'.")

def process():
    try:
        tts = gTTS(text="Welcome to Voice based Email System", lang='en')
        ran = random.randint(0, 999)
        ttsname = f"name{ran}.mp3"
        tts.save(ttsname)

        playsound(ttsname)
        os.remove(ttsname)

        print("Login")
        tts = gTTS(text="Say Login", lang='en')
        ran = random.randint(0, 999)
        ttsname = f"hello1{ran}.mp3"
        tts.save(ttsname)

        playsound(ttsname)
        os.remove(ttsname)

        tts = gTTS(text="Your choice ", lang='en')
        ran = random.randint(0, 999)
        ttsname = f"hello2{ran}.mp3"
        tts.save(ttsname)

        playsound(ttsname)
        os.remove(ttsname)

        text = ""
        while text == "":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Your choice:")
                audio = r.listen(source)
                print("ok done!!")

            try:
                text = r.recognize_google(audio)
                print("You said : " + text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

            if text == "":
                tts = gTTS(text="Error in Message. Please Give Input Again ", lang='en')
                ran = random.randint(0, 999)
                ttsname = f"err{ran}.mp3"
                tts.save(ttsname)
                playsound(ttsname)
                os.remove(ttsname)

        if text.lower() in ['1', 'one', 'o n e', 'login', 'signin']:
            print("Login")
            l.process()

    except Exception as e:
        print(f"An error occurred: {e}")

process()

