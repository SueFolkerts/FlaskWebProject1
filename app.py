"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
app = Flask(__name__)
from flask import render_template
import os
import random
import base64
from win32printing import Printer


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

def SetHairName():
    global hairName, Hair
    newHair = Hair
    while newHair == Hair:
        newHair = random.randint(1,NumberHair)
    Hair = newHair
    hairName = r'/images/Hair/Hair' + str(Hair) + '.png'

def SetEarsName():
    global earsXName,earsYName, Ears
    newEars = Ears
    while newEars == Ears:
        newEars = random.randint(1,NumberEars)
    Ears = newEars
    earsXName = r'/images/Ears/EarsX' + str(Ears) + '.png'
    earsYName = r'/images/Ears/EarsY' + str(Ears) + '.png'

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
NumberHair = 2

Head = random.randint(1,NumberHeads)
Eyes = 0
Noses = 0
Mouths = 0
Ears = 0
Hair = 0
fileName = ""
eyesName = r'/images/NoImage.png'
nosesName = r'/images/NoImage.png'
mouthsName = r'/images/NoImage.png'
earsXName = r'/images/NoImage.png'
earsYName = r'/images/NoImage.png'
hairName = r'/images/NoImage.png'
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
        elif request.form.get('Hair') == 'Hair':
            SetHairName()
    else:
        SetFileName()

    return render_template("Main.html", fileName = fileName, eyesName = eyesName, nosesName = nosesName, mouthsName = mouthsName, 
                           earsXName = earsXName, earsYName = earsYName, hairName = hairName)  


#def contact():


if __name__ == '__main__':
    
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
