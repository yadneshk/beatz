from .execute import BackgroundActions as bkg_actions
import validators, subprocess
import youtube_dl, sys

class YoutubeHelper:
    def __init__(self, urls):
        self.urls = urls


    def start_streaming(self):
        for url in self.urls:
            youtube_dl_obj = youtube_dl.YoutubeDL({'quiet': True})
            song_title = youtube_dl_obj.extract_info(url, False)['title']
            print(f'Now streaming %s ' % song_title, end='\r')
            cmd = 'mpv {} --really-quiet -no-video --audio-display=no'.format(url)
            subprocess.Popen(cmd.split()).wait()


    def download_audio(self, path):
        print('Saving into %s' % path)
        for url in self.urls:
            cmd = 'youtube-dl -o %(title)s.%(ext)s {} --get-filename'.format(url)
            output, error = bkg_actions().execute(cmd)
            song_name = output.split('.')[0]
            print('Downloading %s ' % song_name)
            cmd = 'youtube-dl -o {path}/%(title)s.%(ext)s -q -x --audio-format mp3 {url}'.format(path=path, url=url)
            output, error = bkg_actions().execute(cmd)
            if error != '':
                return error
