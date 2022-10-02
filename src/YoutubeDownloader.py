from typing import *
from pytube import *
from tkinter import filedialog
import os, moviepy.editor as mp

class Downloader(YouTube):
    def __init__(self, url: str, on_progress_callback: Optional[Callable[[Any, bytes, int], None]] = None, on_complete_callback: Optional[Callable[[Any, Optional[str]], None]] = None, proxies: Dict[str, str] = None, use_oauth: bool = False, allow_oauth_cache: bool = True):
        super().__init__(url, on_progress_callback, on_complete_callback, proxies, use_oauth, allow_oauth_cache) # indica el enlace

    def VideoDownloader(self, file_extension:str = "mp4", output: dir = ""):
        """Descarga el video en la mayor calidad posible."""
        video = super().streams.filter(progressive=True, file_extension=f"{file_extension}").order_by("resolution").desc().first()
        
        self.destination = video.download(output)

    

    def MusicDownloader(self, output: dir = ""):
        self.VideoDownloader("mp4", output)

        out_file = self.destination
        base, ext = os.path.splitext(out_file)
        clip = mp.VideoFileClip(f'{base}{ext}')
        clip.audio.write_audiofile(f"{base}.mp3")

        clip.close()
        os.remove(out_file)

    def __del__(self):
        print(super().title, "Se ha descargado satifactoriamente.")
        

class PlaylistDownloader(Playlist):
    def __init__(self, url: str, proxies: Optional[Dict[str, str]] = None):
        super().__init__(url, proxies)
        
    def VideoDowloader(self, output: dir = ""):
        for video in super().videos:
            down = Downloader(video.watch_url)
            down.VideoDownloader("mp4", output)
            del down
    
    def MusicDownloader(self, output: dir = ""):
        for video in super().videos:
            down = Downloader(video.watch_url)
            down.MusicDownloader(output)
            del down
if __name__ == "__main__": 
    test = PlaylistDownloader("https://www.youtube.com/playlist?list=PLwV5x4pHjcTB_qNqhtclLWZ6F4GdSjxQ8")
    output = filedialog.askdirectory()
    test.MusicDownloader(output)
    




