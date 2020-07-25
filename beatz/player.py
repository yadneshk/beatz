from beatz.execute import ValidateURLs as validate
import youtube_dl
import sys
import subprocess
import re
import time


TYELLOW = '\033[33m'
TWHITE = '\033[37m'
BASE_URL = "https://youtube.com"


class Player:
    def play_song(self, url):
        youtube_dl_obj = youtube_dl.YoutubeDL({'quiet': True})
        song_title = youtube_dl_obj.extract_info(url, False)['title']
        print(TYELLOW + f'  ♫ %s ' % song_title + TWHITE, end='\r')
        cmd = 'mpv {} --really-quiet -no-video --audio-display=no'.format(url)
        subprocess.Popen(cmd.split()).wait()
        print(f"\r    %s" % song_title)


    def print_results(self, songs_dict):
        for song_id, song_details in songs_dict.items():
            print(f"[{song_id}] {song_details['title']} ({song_details['duration']})")


    def play_songs(self, songs_list):
        print("Pause p, Mute m, Prev <, Next >, Vol(+) *, Vol(-) /, Quit q")
        for id in songs_list:
            self.play_song(f"{BASE_URL}{self.songs_dict[id]['url_suffix']}")


    def play_from_search_results(self, songs_dict, max_results):
        self.songs_dict = songs_dict
        self.print_results(songs_dict)
        which_to_play = input("\nChoose which to play: 1, 1-3 or 2,3 (Quit: q or Q)\n")
        if which_to_play in ['q', 'Q']:
            sys.exit(0)
        songs_list = validate().validate_song_input(which_to_play, max_results)
        self.play_songs(songs_list)
