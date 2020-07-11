from .execute import ValidateURLs
import argparse, sys
from .version import __version__
from .youtube_helper import YoutubeHelper

#url = 'https://www.youtube.com/watch?v=5wyW-w1ikK0'

class TunedArguments:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='This is test description',
            usage='''tuned <command> [<args>]
            download             Download YouTube video
            stream               Stream YouTube video''',
            epilog='This is test epilog'
        )
        parser.add_argument('command',
                            help=argparse.SUPPRESS)
        parser.add_argument('--version',
                            action='version',
                            version=__version__)
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()


    def download(self):
        parser = argparse.ArgumentParser(description='Download this URL')
        parser.add_argument('--urls',
                            nargs='+',
                            help='YouTube video URLs')
        parser.add_argument('--path',
                            action='store',
                            type=str,
                            default='~/Music',
                            help='Download songs directory (default: ~/Music)')
        args = parser.parse_args(sys.argv[2:])
        urls = ValidateURLs().validate_url(args.urls)

        # call download function here
        start_download = YoutubeHelper(urls).download_audio(args.path)


    def stream(self):
        parser = argparse.ArgumentParser(description='Stream URL(s)')
        parser.add_argument('--urls',
                            nargs='+',
                            help='YouTube video URLs')
        args = parser.parse_args(sys.argv[2:])
        urls = ValidateURLs().validate_url(args.urls)
        #print('pause - p, mute audio - m')
        start_stream = YoutubeHelper(urls).start_streaming()
