from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import time 

def download_mp4(url,output_path,resolution='720p'):
    yt = YouTube(url)

    video = yt.streams.filter(res=resolution,file_extension='mp4').first()

    video.download(output_path)
    
    mp4_path = os.path.join(output_path, video.default_filename)
    base, ext = os.path.splitext(video.default_filename)
    base = base+".mp3"
    mp3_path = os.path.join(output_path,base)
    
    convert_mp4_to_mp3(mp4_path,mp3_path)
    
    os.remove(mp4_path)

def convert_mp4_to_mp3(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)
    video_clip.close()
    audio_clip.close()

def download_mp3(url,output_path,resolution='720p'):
    download_mp4(url,output_path)

    
#download_mp4("https://www.youtube.com/watch?v=hCTsObd8mpE","C:\\Users\\excalibur\\Desktop\\test\\mp3")

#convert_mp4_to_mp3("C:\\Users\\excalibur\\Desktop\\test\\mp3\\video.mp4","C:\\Users\\excalibur\\Desktop\\test\\mp3\\video.mp3")