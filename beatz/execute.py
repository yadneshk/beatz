import subprocess
import validators
import sys


class BackgroundActions:
    def execute(self, command):
        cmd = command.strip()
        output, error = subprocess.Popen(
            cmd.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE).communicate()
        output = output.decode('utf-8').strip()
        error = error.decode('utf-8').strip()
        return (output, error)


class ValidateURLs:
    def validate_url(self, urls):
        if urls:
            urls = [url.strip() for url in urls]
            for index, url in enumerate(urls):
                if not validators.url(url):
                    print("Excluding \'%s\' - Invalid url" % url)
                    urls.remove(url)
                    break
                if '&list' in url:
                    urls[index] = url.split('&')[0]
            if urls:
                return urls
            else:
                exit(1)
        if not url:
            return 'Empty URL'


    def validate_song_input(self, input, max_results):
        opts = input.split(',')
        cnf = []
        for opt in opts:
            try:
                cnf.append(int(opt))
            except ValueError:
                if '-' not in opt:
                    print(f"{opt} does not seem to be an integer")
                    sys.exit(1)
                vals = opt.split('-')
                if len(vals) != 2:
                    print(f"{opt} has incorrect syntax")
                    sys.exit(1)
                try:
                    for a in vals:
                        int(a)
                except ValueError:
                    print(f"'{opt}' does not seem to an integer")
                    sys.exit(1)
                if int(vals[1]) < int(vals[0]):
                    print(f"{opt} has incorrect syntax")
                    sys.exit(1)
                for i in range(int(vals[0]), int(vals[1])+1):
                    cnf.append(i)
        _cnf = []
        for no in cnf:
            if no <= max_results:
                _cnf.append(no)
            else:
                print(f"[{no}] does not lie in the result. Ignoring..")
        return _cnf
