from gtts import gTTs
import speech_recognition as sr
import os
import webbrowser
import smtplib


def talkToMe(audio):
    print(audio)
    tts = gTTs(text=audio, languae='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


# Listen for commands
def myCommand(parameter_list):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command master')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print('You said: ' + command + '/n')

        # Loop back to continue listening for commands
        except sr.UnknownValueError:
            assistant(myCommand())

        return command

# If Statement
def assistant(command);

    if 'open Reddit python' in command:
        chrome_path = '/Applications/Google Chrome.app'