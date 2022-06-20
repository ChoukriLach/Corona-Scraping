import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os 
import random
import re
from Data import Data



def record_audio() :
    r = sr.Recognizer()
    with sr.Microphone() as source : 
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  
        except sr.UnknownValueError: 
            return 'Sorry , I did not get that can you repeat your question ?'
        except sr.RequestError:
            return 'Sorry , the service is down can you try again ?'
    return str(voice_data).lower()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') 
    r = random.randint(1,200000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) 
    print(audio_string) 
    playsound(audio_file) 
    os.remove(audio_file) 


def main():
    data = Data("https://www.worldometers.info/coronavirus/")
    
    PATTERNS = {
					re.compile("[\w\s]+ cases [\w\s]+"): lambda country: data.get_total_country_cases(country),
                    re.compile("[\w\s]+ deaths [\w\s]+"): lambda country: data.get_total_country_death_cases(country),
                    re.compile("[\w\s]+ recovered [\w\s]+"): lambda country: data.get_total_country_recovered_cases(country)
					}
    
    print('What is your question ?')

    while True : 
        voice_data = record_audio()
        audio_string = voice_data

        if 'exit' in voice_data :
            exit()
    
        for pattern , func in PATTERNS.items() :
            if pattern.match(voice_data):
                words = set(voice_data.split(" "))
                for country in data.data['Countries'] :
                    if str(country).lower() in words :
                        audio_string = func(country)
                        break

        speak(audio_string)
    
    
if __name__ == '__main__':
    main()

