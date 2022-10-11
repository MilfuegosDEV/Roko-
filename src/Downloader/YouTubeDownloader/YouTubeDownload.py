from yt_dlp \
    import YoutubeDL

class Downloader(object):
    """Permite descargar los videos"""
    def __init__(self, url, output):
        self.url = url      
        self.__dir = output

    def mp3_download(self):
        """Descarga el audio del video"""
        # opts = {
        #     'writethumbnail': True,
        #     'format': 'bestaudio/best',
        #     'fixup': 'detect_or_warn',
        #     "verbose": False,
        #     "extract-audio": True,
        #     "audio-format": "mp3",            
        #     "nocheckcertificate": True,
        #     "quiet": True,
        #     "no_warnings": True,
        #     "ignoreerrors": True,
        #     "noplaylist": False,
        #     "outtmpl": f"{self.__dir}/%(title)s.%(ext)s",
        #     "postprocessors": [{
        #         "key": "FFmpegExtractAudio",
        #         "preferredcodec": "mp3",},
        #     {'key': 'EmbedThumbnail',},]
        # }
        opts = {
            "verbose": True,
            "fixup"  : "detect_or_warn",
            "format" : "bestaudio[ext=m4a]",
            "postprocessors" : [{
                "key": "FFmpegExtractAudio",
                "preferredcodec"  : "m4a",
                "preferredquality"  : 1411
            }],
            "extractaudio": False,
            "outtmpl"     : self.__dir + "/%(title)s.%(ext)s",
            "noplaylist"  : False, 
            "ignoreerrors": True,
            "quiet": True, 
            "no_warnings": True
        }

        download_obj = YoutubeDL(opts)
        info_dict = download_obj.extract_info(self.url, download= True)
        name = download_obj.prepare_filename(info_dict)

    def mp4_download(self):
        """Descarga el video"""
        opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "verbose": False,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "fixup": "never",
            "ignoreerrors": True,
            "noplaylist": False,
            "outtmpl": f'{self.__dir}/%(title)s.%(ext)s'
        }
        download_obj = YoutubeDL(opts)
        info_dict = download_obj.extract_info(self.url, download= True)
        name = download_obj.prepare_filename(info_dict)


