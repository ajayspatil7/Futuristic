import speech_recognition as sr
from gtts import gTTS
import os


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio)
            print("You said: " + recognized_text)
            return recognized_text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def text_to_speech(text):
    tts = gTTS(text)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")

if __name__ == '__main__':
    text = speech_to_text()
    if text:
        text_to_speech(text)
