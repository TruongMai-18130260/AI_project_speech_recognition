import pyttsx3
import speech_recognition

from tkinter import *



def hearme():
    engine = pyttsx3.init()
    engine.say("tell me something?")
    engine.runAndWait()
    robot_ear = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("question...")
        audio = robot_ear.listen(mic)
    question = robot_ear.recognize_google(audio,language="vi-VI")
    
    print(question)

    # engine.say("tell me answer ?")
    # with speech_recognition.Microphone() as mic:
    #     print("answer...")
    #     audio = robot_ear.listen(mic)
    # answer = robot_ear.recognize_google(audio)
    # print(answer)
    
    return question




