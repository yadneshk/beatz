import youtube_dl, sys, subprocess


class Player:
    def play_song(self, url):
        youtube_dl_obj = youtube_dl.YoutubeDL({'quiet': True})
        song_title = youtube_dl_obj.extract_info(url, False)['title']
        print(f'Now streaming - %s ' % song_title, end='\r')
        cmd = 'mpv {} --really-quiet -no-video --audio-display=no'.format(url)
        subprocess.Popen(cmd.split()).wait()
