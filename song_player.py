#play song and form video
import cv2
from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import pyglet
import time

cap = cv2.VideoCapture('output.mp4')  # Replace with the path to your video file
time = 60
#automaticly plays fft video after formulation
#doesnt work, at least on my machine
def play_song():
    combine()
    time.sleep(1)
    # Check if the video was loaded successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit(1)

    # Get the frames per second (FPS) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):  # Use FPS to determine wait time between frames
            break

    cap.release()
    cv2.destroyAllWindows()

#combines all gernrated fft pngs to create a mp4 viseo
def combine():
    # Load the video and audio clips
    video_clip = VideoFileClip('fft_video.mp4').subclip(0, time)  # Replace with the path to your video file and set the subclip to the first 10 seconds
    audio_clip = AudioFileClip('./songs/converted_audio.wav').subclip(0, time)  # Replace with the path to your audio file and set the subclip to the first 10 seconds

    # Set the duration of the video clip to match the duration of the audio clip
    video_clip = video_clip.set_duration(audio_clip.duration)

    # Combine the video and audio clips
    final_clip = concatenate_videoclips([video_clip.set_audio(audio_clip)])

    # Write the final combined clip to a new video file
    final_clip.write_videofile('output.mp4', codec='libx264')
