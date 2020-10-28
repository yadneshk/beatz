from beatz.execute import BackgroundActions as bkg_actions
from beatz.player import Player
import validators
import subprocess
import requests
import urllib.parse
import json


class YoutubeHelper:
    def __init__(self, urls):
        self.urls = urls

    def start_streaming(self):
        player = Player()
        for url in self.urls:
            player.play_song(url)

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


class YoutubeSearch:
    def __init__(self, search_terms: str, max_results=None):
        self.search_terms = search_terms
        self.max_results = max_results
        self.videos = self.search()

    def search(self):
        encoded_search = urllib.parse.quote(self.search_terms)
        BASE_URL = "https://youtube.com"
        url = f"{BASE_URL}/results?search_query={encoded_search}"
        response = requests.get(url).text
        trimmed_content_start = response[response.find('ytInitialData')+16:]
        final_trimmed_content = trimmed_content_start[:trimmed_content_start.find('};')+1]
        results = self.parse_html(final_trimmed_content)
        return results

    def parse_html(self, response):
        results = {}
        data = json.loads(response)
        videos = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
            "sectionListRenderer"
        ]["contents"][0]["itemSectionRenderer"]["contents"]
        for count, video in enumerate(videos):
            res = {}
            if "videoRenderer" in video.keys() and (count+1 <= self.max_results):
                video_data = video.get("videoRenderer", {})
                res["title"] = video_data.get("title", {}).get("runs", [[{}]])[0].get("text", None).strip()
                res["duration"] = video_data.get("lengthText", {}).get("simpleText", 0).strip()
                res["url_suffix"] = video_data.get("navigationEndpoint", {}).get("commandMetadata", {}).get("webCommandMetadata", {}).get("url", None).strip()
                results[count+1] = res
        return results

    def to_dict(self):
        return self.videos
