from django.shortcuts import redirect, render 
import speech_recognition as sr
import pyttsx3

def home(request):
    if request.method == "POST":
        r = sr.Recognizer()
        engine = pyttsx3.init()

        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                
                result = text
                rate = engine.getProperty("rate")
                engine.setProperty("rate", 100)
                engine.say(text)
                engine.runAndWait()
                return render(request, "home.html", {"result": result})

            except:
                global error
                error = "Sorry, can't read"
                engine.say(error)
                engine.runAndWait()
                return render(request, "home.html", {"error": error})

    else:
        return render(request, "home.html")

