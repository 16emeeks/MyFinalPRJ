# Generates FFT's every 0.1 sec to compile into a video

import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import moviepy.editor as mp
import time
from green_screen import png_background

def fft_plots():
    start_time1 = time.time()
    print("Generating FFTs")

    # Load the audio file
    audio_file = './songs/converted_audio.wav'
    y, sr = librosa.load(audio_file)
    sr = sr // 3

    # Define the time intervals for which to compute the FFTs
    start_time = 0  # starting time in seconds
    end_time = 60   # ending time in seconds
    interval_duration = .12  # duration of each time interval in seconds (120ms)
    num_intervals = int((end_time - start_time) / interval_duration)

    # Create a figure and axis for plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('black')
    # Remove x and y axis ticks
    plt.subplots_adjust(bottom=0.3)
    # remove the border box
    ax.set_frame_on(False)

    # Precompute the necessary portion of FFT frequencies
    max_len = len(np.arange(0, int(interval_duration * sr), step=2))
    xf = np.fft.fftfreq(max_len, 1 / sr)[:max_len // 2]

    # Loop through each time interval and compute the FFT
    print(f'eta {end_time} sec')
    for i in range(num_intervals):
        # Extract the audio samples for the current time interval
        start_sample = int(start_time * sr)
        y_interval = y[start_sample:start_sample + max_len]

        # Compute the FFT
        yf = np.abs(np.fft.fft(y_interval))[:max_len // 2]
        # Plot the FFT
        ax.clear()
        ax.plot(xf, 0.5*(yf), color='purple')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, sr / 2)
        ax.set_ylim(0, np.max(yf) * .7)

        # Save the current figure as an image
        plt.savefig(f'./pngs/fft_{i+1}.jpg', format='jpg', dpi=120)

        #converts background to a kool png, long process
        png_background(f'./pngs/fft_{i+1}.jpg')

        # Increment the start time for the next interval
        start_time += interval_duration


    # Close the figure
    plt.close(fig)
    print('working...')

    # Create a movie from the saved images
    video_clip = mp.ImageSequenceClip(['./pngs/fft_{}.jpg'.format(i+1) for i in range(num_intervals)], fps=1 / interval_duration)
    video_clip.write_videofile('fft_video.mp4', codec='libx264')

    end_time = time.time()  # Record the end time

    elapsed_time = end_time - start_time1  # Calculate the elapsed time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))
