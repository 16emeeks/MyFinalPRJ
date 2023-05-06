# download audio file from youtube
# Resources Chat_GPT
from youtube_search import YoutubeSearch
from pytube import YouTube
from API import current_track
import os
import glob
import moviepy.editor as mp
from pydub import AudioSegment
import time

# Perform a YouTube search
my_search = current_track() # search term for the particular song
results = YoutubeSearch(my_search, max_results=10).to_dict()

# Iterate through the search results and download the audio for the first video
def download_audio():
    for video in results:
        try:
            yt = YouTube(f"https://www.youtube.com/watch?v={video['id']}", use_oauth=True, allow_oauth_cache=False)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path='./MP4', filename_prefix='audio_')
            time.sleep(1)
            break
        except Exception as e:
            print(e)


def delete_audio(directory):
    directory = directory
    # Get a list of the files in the directory
    file_list = os.listdir(directory)
    # Delete the first file in the list
    if file_list:
        file_path = os.path.join(directory, file_list[0])
        os.remove(file_path)

def convert_to_wav():
    download_audio()
    print("converting to wav")
    mp4_files = glob.glob('./MP4/*.mp4')
    first_mp4_file = mp4_files[0]
    audio = AudioSegment.from_file(first_mp4_file)
    audio.export('./songs/converted_audio.wav', format='wav')
    delete_audio('./MP4')
