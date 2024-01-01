from pytube import YouTube


def download_mp4(url,output_path,resolution='720p'):
    yt = YouTube(url)

    video = yt.streams.filter(res=resolution,file_extension='mp4').first()

    video.download(output_path)

    
#download_mp4("https://www.youtube.com/watch?v=k9Y9-xueg5M","C:\\Users\\excalibur\\Desktop\\test\\mp4")



