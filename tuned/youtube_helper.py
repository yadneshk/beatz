from .execute import BackgroundActions as bkg_actions
import validators, subprocess

from .player import Player

class YoutubeHelper:
    def __init__(self, urls):
        self.urls = urls


    def start_streaming(self):
        for url in self.urls:
            Player().play_song(url)


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
