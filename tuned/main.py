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

            url             Stream this YouTube URL
            ''',
            epilog='This is test epilog'
        )
        parser.add_argument('command',
                            help='Subcommands to run [url]')
        parser.add_argument('--version',
                            action='version',
                            version=__version__)
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()


    def url(self):
        parser = argparse.ArgumentParser(
            description='Download or stream this URL',
            usage='''
            --download Download audio of this URL
            '''
        )
        parser.add_argument('urls',
                            nargs='+')
        parser.add_argument('--download',
                            action='store_true',
                            help='Download songs')
        parser.add_argument('--path',
                            action='store',
                            type=str,
                            default='~/Music',
                            help='Download songs directory (default: ~/Music)')
        parser.add_argument('--stream', )
        args = parser.parse_args(sys.argv[2:])
        urls = ValidateURLs().validate_url(args.urls)

        # call download function here
        if args.download:
            stream_link = YoutubeHelper(urls).download_audio(args.path)
            #print(stream_link)
