from yt_dlp import YoutubeDL
from typing import *
from pytube import Playlist
import os, moviepy.editor as mp


class Download(object):
    """Permite descargar los videos"""
    def __init__(self, url, dir:dir = '', playlist = False):
      self.url = url
      self.playlist = playlist
      self.__dir = dir
    
    def mp3_download(self):
        opts = {
            'format': 'wav/m4a/mp4',
            'ignoreerrors': True,
            "verbose": False,
            "extract-audio": True,
            "audio-format": "{ext}",
            "outtmpl": f"{self.__dir}/%(title)s.%(ext)s",
        }
        Download_obj = YoutubeDL(opts)
        __info_dict = Download_obj.extract_info(self.url, download= True)
        audio_file = Download_obj.prepare_filename(__info_dict)
        try:
            base, ext = os.path.splitext(f"{audio_file}")
            clip = mp.AudioFileClip(f'{base}{ext}')
            clip.write_audiofile(f"{base}.mp3")
            clip.close()
            os.remove(f"{audio_file}")
        except Exception as e:
            print(e)

class PlaylistDownloader(Download, Playlist):
    def __init__(self, url, dir: dir = "",playlist=False):
        for video in Playlist(url).videos:            
            dl = Download(video.watch_url, dir, playlist)
            dl.mp3_download()
            
    def mp3_download(self):
        return super().mp3_download()

    



test = PlaylistDownloader("https://www.youtube.com/playlist?list=PLwV5x4pHjcTBSOrjT7Dh-tyo9qmE2Asrb", dir = 'E:/Música')


test = PlaylistDownloader("https://www.youtube.com/playlist?list=PLwV5x4pHjcTBSOrjT7Dh-tyo9qmE2Asrb", dir = 'E:/Música')

if __name__ == "__main__": 
    url = input("Inserte el url: ")
    test = Downloader(url,use_oauth=True)
    output = filedialog.askdirectory()
    test.MusicDownloader(output)




