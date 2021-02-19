"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
app = Flask(__name__)
from flask import render_template
from PIL import Image
import os
import random
import base64

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


def SetEarsName():
    global mouthsName, Ears
    newEars = Ears
    while newEars == Ears:
        newEars = random.randint(1,NumberEars)
    Ears = newEars
    mouthsName = r'/images/Ears/Ear' + str(Ears) + '.png'

def SetMouthsName():
    global mouthsName, Mouths
    newMouths = Mouths
    while newMouths == Mouths:
        newMouths = random.randint(1,NumberMouths)
    Mouths = newMouths
    mouthsName = r'/images/Mouths/Mouth' + str(Mouths) + '.png'

def SetNosesName():
    global nosesName, Noses
    newNoses = Noses
    while newNoses == Noses:
        newNoses = random.randint(1,NumberNoses)
    Noses = newNoses
    nosesName = r'/images/Noses/Nose' + str(Noses) + '.png'

def SetEyesName():
    global eyesName, Eyes
    newEyes = Eyes
    while newEyes == Eyes:
        newEyes = random.randint(1,NumberEyes)
    Eyes = newEyes
    eyesName = r'/images/Eyes/Eyes' + str(Eyes) + '.png'

def SetFileName():
    global fileName, Head
    newHead = Head
    while newHead == Head:
        newHead = random.randint(1,NumberHeads)
    Head = newHead
    fileName = r'/images/Heads/Head' + str(Head) + '.jpg'

NumberHeads = 16
NumberEyes = 2
NumberNoses = 2
NumberMouths = 2
NumberEars = 2

Head = random.randint(1,NumberHeads)
Eyes = 0
Noses = 0
Mouths = 0
Ears = 0
fileName = ""
eyesName = ""
nosesName = ""
mouthsName = ""
earsName = ""

@app.route('/', methods=['GET', 'POST'])

def art():
    global fileName
    if request.method == 'POST':
        if request.form.get('Head') == 'Head':
            SetFileName()
        elif request.form.get('Eyes') == 'Eyes':
            SetEyesName()
        elif request.form.get('Noses') == 'Noses':
            SetNosesName()
        elif request.form.get('Mouths') == 'Mouths':
            SetMouthsName()
        elif request.form.get('Ears') == 'Ears':
            SetEarsName()
    else:
        SetFileName()
        SetEyesName()
        SetNosesName()
        SetMouthsName()
        SetEarsName()

    return render_template("Main.html", fileName = fileName, eyesName = eyesName, nosesName = nosesName, mouthsName = mouthsName, earsName = earsName)  


#def contact():


if __name__ == '__main__':
    
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
