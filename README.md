# Soundboard

A very basic soundboard that can be remotely controlled.


### Dependencies
This project requires Flask and VLC to be installed.
It also requires the VLC python bindings found at https://wiki.videolan.org/python_bindings


### How to use
Download this repository, add a folder named ```sounds``` and put the audio files you want to be able to play in there.

Then start soundboard.py.

To ensure it is working visit ```localhost``` with your browser. If everything works you should see a button for each audio file.

To use it remotely simply visit the local ip of the computer hosting the soundboard.