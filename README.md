# TEAM
Elliott Meeks

# Description
This program creates an audio visualization of the current song playing from my Spotify
It also publishes the current song name and artist to an MQTT server

# Instructions
Unfortunaty this will only work from my Spotify account. The access tokens are unique to a particular user
so I have to be playing a song for this program to work. I did not have time to make this code work for everyone's account.
oauth2 is a pain to work with, I am happy I got it to work at all. I am almost always playing music so it may
happen to work, or email me (emeeks@usc.edu). However I think the demo video should suffice.

To start the application, navigate to the directory containing the scripts and execute the following command:

```console
$ python3 main.py'''

to subscribe to the MQTT server from another node, ensure sub.py is downloaded in the current directory and
execute the following command:

```console
$ python3 sub.py'''

#Library's
spotipy
requests
spotipy.oauth2
youtube_search
pytube
os
glob
moviepy.editor
pydub
cv2
matplotlib.pyplot
numpy
random
paho.mqtt
time
librosa.display
