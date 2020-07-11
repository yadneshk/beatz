from .execute import BackgroundActions as bkg_actions
import validators

class YoutubeHelper:
    def __init__(self, urls):
        self.urls = urls


    def get_stream_links(self):
        cmd = 'youtube-dl -g {url}'.format(url=self.url)
        output, error = bkg_actions().execute(cmd)
        if error != '':
            return 'Something went wrong!'
        streaming_urls = output.split('\n')
        for url in streaming_urls:
            if 'mime=audio' in url:
                return url


    def download_audio(self, path):
        print('Saving into %s' % path)
        for url in self.urls:
            cmd = 'youtube-dl -o %(title)s.%(ext)s {url} --get-filename'.format(url=url)
            output, error = bkg_actions().execute(cmd)
            song_name = output.split('.')[0]
            print('Downloading %s ' % song_name)
            cmd = 'youtube-dl -o {path}/%(title)s.%(ext)s -q -x --audio-format mp3 {url}'.format(path=path, url=url)
            output, error = bkg_actions().execute(cmd)
            if error != '':
                return error
