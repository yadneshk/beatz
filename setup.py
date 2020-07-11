from setuptools import setup

setup(
name='tuned',
packages=['tuned'],
install_requires=
[
    "youtube_dl",
    "requests",
    "beautifulsoup4",
    "selenium",
    "lxml",
    "validators"
],
entry_points={'console_scripts': ['tuned=tuned.main:TunedArguments']}
)
