from setuptools import setup
from beatz.version import __version__

setup(
name='beatz',
packages=['beatz'],
install_requires=
[
    "youtube_dl",
    "validators"
],
entry_points={'console_scripts': ['beatz=beatz.main:BeatzArguments']},
author='yadneshk',
author_email='yadnesh45@gmail.com',
version=__version__,
description='Download & stream music on your terminal'
)
