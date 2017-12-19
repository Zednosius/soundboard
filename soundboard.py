from flask import Flask
from flask import request, render_template
from playsound import playsound
import os

app = Flask(__name__)

#Gets filenames of sounds
sound_filenames = list(os.walk("sounds"))[0][2]
cache = {"sounds" : list(zip(map(lambda x: os.path.splitext(x)[0], sound_filenames), sound_filenames))}
print("Cache:", cache)
@app.route("/", methods=["POST","GET"])
def hello():
    print(request)
    if request.method == "POST":
        print("Data",request.form)
        print("It did something!")
        playsound("sounds/beep-30b.mp3")
        return render_template("index.html", sounds=cache["sounds"])
    else:
        return render_template("index.html", sounds=cache["sounds"])