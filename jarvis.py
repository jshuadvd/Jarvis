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
        url = 'https://www.redit.com/r/python'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talkToMe('I am at your service master')

    if 'email' in command:
        talkToMe('Who is the recipient')
        recipient = myCommand()

        if 'Rhiannon' in recipient:
            talkToMe('What should I say')
            content = myCommand()

            # Init SMTP To send mail with Gmail 
            mail - smtplib.SMTP('smtp.gmail.com', 587)

            # Identify to server
            mail.ehlo()

            # Encrypt Session
            mail.starttls()

            # Login
            mail.login('username', 'password')

            # Send Message
            mail.sendmail('PERSON NAME', 'emailaddress@email.com', content)

            # Close Connection
            mail.close()

            # Email Sent Confirmation
            talkToMe('Your message was sent master')
