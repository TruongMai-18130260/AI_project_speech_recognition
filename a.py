from tkinter import * 
from tkinter import messagebox 
import speak as speakagent
import json

def printa():
    data = ""
    with open("exampledata.json", "r") as outfile:
        tmp = json.dumps(json.load(outfile))
        data = tmp[1:len(tmp)-1]

    questiondata = speakagent.hearme()
    answer = speakagent.hearme()


    data += ',{"question":"' + questiondata + '","answer":"' + answer + '"}'

    with open("exampledata.json","w") as outfile:
        outfile.write("[" + data + "]")

    # with open("exampledata.json", "r") as outfile: 
    #     jo = json.load(outfile)
    #     print(jo["answer"])

    # py framedemo.py

# with open("exampledata.json", "r") as outfile: 
#         jo = json.load(outfile)
#         item = list(jo)
#         print(item[1]["question"])