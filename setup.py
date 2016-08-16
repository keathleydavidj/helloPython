try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Hello world app, written in Python',
    'author': 'David Keathley',
    'author_email': 'keathleydavidj@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['app'],
    'scripts': [],
    'name': 'helloPython'
}

setup(**config)