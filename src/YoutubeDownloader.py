from yt_dlp import YoutubeDL
from typing import *
from pytube import Playlist
import os, moviepy.editor as mp


class Downloader(object):
    """Permite descargar los videos"""
    def __init__(self, url, dir:dir = ''):
        self.url = url      
        self.__dir = dir
        if "playlist?list=" in self.url or "index=" in self.url:
            del self.mp3_download
            del self.mp4_download

    def mp3_download(self):
        """Descarga el audio del video"""

        opts = {
            "format": 'bestaudio/best',
            "verbose": False,
            "extract-audio": True, 
            "fixup": 'never',
            "ignoreerrors": True,
            "noplaylist": True,
            "outtmpl": f'{self.__dir}/%(title)s.%(ext)s'
        }
        Download_obj = YoutubeDL(opts)
        __info_dict = Download_obj.extract_info(self.url, download= True)
        self.__file = Download_obj.prepare_filename(__info_dict)
        self.__fixup()

    def mp4_download(self):
        """Descarga el video"""
        opts = {
            "verbose": False,
            "fixup": "never",
            "ignoreerrors": True,
            "noplaylist": False,
            "outtmpl": f'{self.__dir}/%(title)s.%(ext)s'
        }
        YoutubeDL(opts).download(self.url)



    def __fixup(self):
        """Cambia el formato del audio a .mp3"""
        try:
            base, ext = os.path.splitext(f"{self.__file}")
            clip = mp.AudioFileClip(f'{base}{ext}')
            clip.write_audiofile(f"{base}.mp3",)
            clip.close()
            os.remove(self.__file)
        except OSError:
            os.remove

    def __del__(self):
        pass


class PlaylistDownloader:
    """Permite la descarga de las playlist"""
    def __init__(self, url, dir: dir = ""):
        """Obtiene el enlace de cada uno de los videos
        que se encuentren en la playlist"""
        try:
            self.__url = url
            self.__dir = dir
            self.__playlist = Playlist(self.__url)
        except:
            pass

    def mp3_download(self):
        for video in self.__playlist.videos:            
            Downloader(video.watch_url, self.__dir).mp3_download()

    def mp4_download(self):
        for video in self.__playlist.videos:            
            Downloader(video.watch_url, self.__dir).mp4_download()


if __name__ == "__main__":
    test = PlaylistDownloader("https://www.youtube.com/watch?v=ltO7uyLImGg","/src")
    test.mp4_download()

    






