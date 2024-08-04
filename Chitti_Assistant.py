import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!,Sir")  

    speak("मैं Chitti robot bol raha हूं, सर, कृपया मुझे बताएं कि मैं आपकी कैसे मदद कर सकता हूं")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\shera\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\shera\\OneDrive\Desktop\\Visual Studio Code.lnk"
            os.startfile(codePath)
        
        elif ('tum kaise ho' in query) or ('how ' in query):
            speak("I am fine, sir")

        elif (('kaun ho' in query or 'apne bare'in query  or 'introduce'in query)  ):
            speak('''मेरा नाम चिती है, मैं एक program हू जो मेरे मलिक शेराज सर, द्वारा बनाया गया हू,
                    प्यारा सा Program
                    मीठी सी आवाज़,
                    मासूम सा दिल
                    स्वीट सी मुस्कान,
                    परफेक्ट पर्सनालिटी
                    खुश मिजाज़ अंदाज,
                    ये तो हुई मेरी बात
                    और बताओ कैसे हो आप ''')
        
        elif 'joke' in query:
            j= pyjokes.get_joke()
            print(j)
            speak(j)
            speak("Hahahaha!")
        elif 'shayari' in query:
            t='''​शायरी के माध्यम से हम अपनी भावनाओं को न केवल व्यक्त कर सकते हैं, 
            बल्कि दूसरों की भावनाओं को भी समझ सकते हैं। 
            यह एक ऐसा सशक्त माध्यम है जो भाषा की...
            इसी बात पे एक शायरी सुनाना चाहूगा सर! अगर आप की इजाजत है तो
            मेरा सब कुछ रख ले ऐ मोहब्बत के वकील,
             मेरा सब कुछ रख ले ऐ मोहब्बत के वकील,
            बस मुझे उसकी यादों की क़ैद से रिहाई चाहिए !!'''
            speak(t)


        elif 'email to sheraj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sherajsharif786@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")    
