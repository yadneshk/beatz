from beatz.youtube_helper import YoutubeHelper, YoutubeSearch
from beatz.player import Player


class Process:
    def __init__(self, query=None, max_results=None):
        self.query = query
        self.max_results = max_results


    def search_and_play(self):
        results = YoutubeSearch(self.query, self.max_results).to_dict()
        if not results:
            print(f"No results found for '{self.query}'")
            exit(0)
        Player().play_from_search_results(results, self.max_results)
