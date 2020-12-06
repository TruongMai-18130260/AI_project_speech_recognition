from tkinter import * 
from tkinter import messagebox 
import speak as speakagent
import json

def printa():
    data = ""
    with open("exampledata.json", "r") as outfile:
        data = json.dumps(json.load(outfile))

    questiondata = list(speakagent.hearme())
    data += '{"question":"' + str(questiondata[0]) + ',"answer":"' + str(questiondata[1]) + '"}'

    with open("exampledata.json","w") as outfile:
        outfile.write("[" + data + "]")

    with open("exampledata.json", "r") as outfile: 
        jo = json.load(outfile)
        print(jo["answer"])

    # py framedemo.py

with open("exampledata.json", "r") as outfile: 
        jo = json.load(outfile)
        item = list(jo)
        print(item[1]["question"])