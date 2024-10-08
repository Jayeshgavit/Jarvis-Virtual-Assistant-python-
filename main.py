import speech_recognition as sr
import pyttsx3 as tts
import webbrowser as browser
import musicLibrary as musiclib
from openai import OpenAI
import requests
import sys

recognizer = sr.Recognizer()
engine = tts.init()
newsapi = "d7d5d70d9dca43ba8754fb833bf1a4fe"
url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d7d5d70d9dca43ba8754fb833bf1a4fe"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key = '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'
    )
    
    completion = client.chat.completions.create( # type: ignore
        model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful vistual assistant named Jarvis skilled in tasks like alexa and google "},
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

    return (completion.choices[0].message.content)
    
def procesecommand(c):
    
    if 'open google' in c.lower():
        speak('opening google')
        browser.open("http://google.com")

    elif 'open stackoverflow' in c.lower():
        speak('opening stackoverflow')
        browser.open("http://stackoverflow.com")

    elif 'open github' in c.lower():
        speak('opening github')
        browser.open("http://github.com")

    elif 'open youtube' in c.lower():
        speak('opening youtube')
        browser.open("http://youtube.com")

    elif 'open facebook' in c.lower():
        speak('opening facebook')
        browser.open("http://facebook.com")

    elif 'open twitter' in c.lower():
        speak('opening twitter')
        browser.open("http://twitter.com")
    elif 'open instagram' in c.lower():
        speak('opening instagram')
        browser.open("http://instagram.com")
    elif 'open linkedin' in c.lower():
        speak('opening linkedin')
        browser.open("http://linkedin.com")

    elif 'open reddit' in c.lower():
        speak('opening reddit')
        browser.open("http://reddit.com")
    elif 'open pinterest' in c.lower():
        speak('opening pinterest')
        browser.open("http://pinterest.com")
   
    elif 'open amazon' in c.lower():
        speak("opening Amazon")
        browser.open("http://amazon.com")
    elif 'open ebay' in c.lower():
        browser.open("http://ebay.com")
    elif 'open netflix' in c.lower():
        browser.open("http://netflix.com")
    elif 'open hulu' in c.lower():
        browser.open("http://hulu.com")
    elif 'open disney' in c.lower():
        browser.open("http://disney.com")
    elif 'open walmart' in c.lower():
        browser.open("http://walmart.com")
    elif 'open cnn' in c.lower():
        browser.open("http://cnn.com")
    elif 'open bbc' in c.lower():
        browser.open("http://bbc.com")
    elif 'open forbes' in c.lower():
        browser.open("http://forbes.com")
    elif 'open techcrunch' in c.lower():
        browser.open("http://techcrunch.com")
    elif 'open wired' in c.lower():
        browser.open("http://wired.com")
    elif 'open theverge' in c.lower():
        browser.open("http://theverge.com")
    elif 'open nytimes' in c.lower():
        browser.open("http://nytimes.com")
    elif 'open guardian' in c.lower():
        browser.open("http://theguardian.com")
    elif 'open quora' in c.lower():
        browser.open("http://quora.com")
    elif 'open medium' in c.lower():
        browser.open("http://medium.com")
    elif 'open codewithharry' in c.lower():
        browser.open("http://codewithharry.com")
    elif 'open udemy' in c.lower():
        browser.open("http://udemy.com")
    elif 'open coursera' in c.lower():
        browser.open("http://coursera.org")
    elif 'open edx' in c.lower():
        browser.open("http://edx.org")
    elif 'open khan academy' in c.lower():
        browser.open("http://khanacademy.org")
    elif 'open codecademy' in c.lower():
        browser.open("http://codecademy.com")
    elif 'open pluralsight' in c.lower():
        browser.open("http://pluralsight.com")
    elif 'open lynda' in c.lower():
        browser.open("http://lynda.com")
    elif 'open skillshare' in c.lower():
        browser.open("http://skillshare.com")
    elif 'open mit open courseware' in c.lower():
        browser.open("http://ocw.mit.edu")
    elif 'open data camp' in c.lower():
        browser.open("http://datacamp.com")
    elif 'open udacity' in c.lower():
        browser.open("http://udacity.com")
    elif 'open codewars' in c.lower():
        browser.open("http://codewars.com")
    elif 'open hackerrank' in c.lower():
        browser.open("http://hackerrank.com")
    elif 'open leetcode' in c.lower():
        browser.open("http://leetcode.com")
    elif 'open topcoder' in c.lower():
        browser.open("http://topcoder.com")
    elif 'open project euler' in c.lower():
        browser.open("http://projecteuler.net")
    
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        browser.open(link)

    elif 'news' in c.lower():
        r = requests.get(url)

        r.raise_for_status()
        
        # Parse the JSON response
        data = r.json()
        
        # Extract articles from the response
        articles = data.get('articles', [])
        
        # List to store article titles
        for article in articles:
            title = article.get('title', 'No title available')
            description = article.get('description', 'No description available')
            news_info = f"Title: {title}. Description: {description}"
            speak(news_info)

    elif 'stop' in c.lower():
        speak("Goodbye")
        sys.exit()


    else:
        
        output = aiprocess(c)
        speak(output)

if __name__ == '__main__':
    speak("Initializing Jarvis....")

    while True:
        # Listen for the wake word "Jarvis"
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                audio = recognizer.listen(source,timeout=3)

                command = recognizer.recognize_google(audio)
                if (command.lower() == 'jarvis'):
                    speak("yes")

                    #listen for user command 
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    procesecommand(command)

        except Exception as e:
            print(f"Error  {e}")
