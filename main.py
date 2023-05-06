from get_audio import convert_to_wav
from viz import fft_plots
from song_player import play_song, combine

#Downloads mp3 and converts it to a wave file
convert_to_wav()

#gererates descrete fft plots from .wav file
fft_plots()
#play_song()

#combines fft plots to make a video
combine()
