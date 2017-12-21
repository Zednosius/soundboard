from flask import Flask
from flask import request, render_template
from flask import jsonify
from collections import OrderedDict
import os
import vlc
from pprint import pprint
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

app = Flask(__name__)

#Gets filenames of sounds
sound_filenames = list(os.walk("sounds"))[0][2]
sound_filenames = sorted(sound_filenames)
zipped_name_filenames = list(zip(map(lambda x: os.path.splitext(x)[0], sound_filenames), sound_filenames))
sound_cache = OrderedDict([(key, value) for (key,value) in zipped_name_filenames])
instance = vlc.Instance()
player = instance.media_player_new()
print("Sounds")
pprint(sound_cache)
print()

@app.route("/", methods=["POST","GET"])
def hello():
    global player
    print(request)
    if request.method == "POST":
        data = request.get_json()
        print("Data",data)

        if player is not None and data.get("stop",False):
            player.stop()
            return jsonify(success=True)
        elif data["mp3"] in sound_cache:
            player.set_media(instance.media_new_path("sounds/"+sound_cache[data["mp3"]]))
            
            player.play()
            return jsonify(success=True)
        else:
            return jsonify(success=False)
        
    else:
        return render_template("index.html", sounds=sound_cache)

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0",debug=False, port=80)