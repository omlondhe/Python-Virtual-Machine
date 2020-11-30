import speech_recognition as sr
import pyttsx3
import random
from tkinter import *


op1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
op = ["plus", "minus", "multiplied by", "divided by"]
op2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bot = pyttsx3.init('sapi5')
bot.setProperty('voice', bot.getProperty('voices')[0].id)


def check_quit():
    if str(ans.lower()) == "exit" or str(ans.lower()) == "quit" or str(ans.lower()) == "stop":
        say("Okay , Exiting the game !!!")
        quit()


def say(a):
    bot.say(a)
    bot.runAndWait()


def voice_command():
    recognize = sr.Recognizer()
    with sr.Microphone() as mic:
        say("equals to ?")
        hear = recognize.listen(mic)
        try:
            recognize.adjust_for_ambient_noise(mic)
            inp = recognize.recognize_google(hear, language="en-in")
            print(inp)
            if inp == "zero":
                return "0"
            elif inp == "tu" or inp == "Tu":
                return "2"
            else:
                return inp
        except:
            return "1"


say("Let's get started !!!")

while True:
    first = random.choice(op1)
    operator = random.choice(op)
    second = random.choice(op2)

    say(str(first) + " " + str(operator) + " " + str(second))
    # command = voice_command().lower()
    while True:
        ans = voice_command()
        if operator == 'plus':
            check_quit()
            if ans == str(first + second):
                print(ans, " ", str(first + second))
                say("Right answer .... ")
                break
            else:
                say("Solve again")
                say(str(first) + " " + str(operator) + " " + str(second))
                continue
        elif operator == 'minus':
            check_quit()
            if ans == str(first - second):
                print(ans, " ", str(first - second))
                say("Right answer .... ")
                break
            else:
                say("Solve again")
                say(str(first) + " " + str(operator) + " " + str(second))
                continue
        elif operator == 'multiplied by':
            check_quit()
            if ans == str(first * second):
                print(ans, " ", str(first * second))
                say("Right answer .... ")
                break
            else:
                say("Solve again")
                say(str(first) + " " + str(operator) + " " + str(second))
                continue
        elif operator == 'divided by':
            check_quit()
            if ans == str(int(first / second)):
                print(ans, " ", str(first / second))
                say("Right answer .... ")
                break
            else:
                say("Solve again")
                say(str(first) + " " + str(operator) + " " + str(second))
                continue
