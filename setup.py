from setuptools import setup

setup(
    name = 'pyxeoma',
    packages = ['pyxeoma'],
    version = '0.1',  # Ideally should be same as your GitHub release tag varsion
    description = 'Python wrapper for Xeoma web server API',
    author = 'Jerad Meisner',
    author_email = 'jerad.meisner@gmail.com',
    url = 'https://github.com/jeradM/pyxeoma',
    download_url = 'https://github.com/jeradM/pyxeoma/archive/0.1.tar.gz',
    keywords = ['Xeoma'],
    install_requires=[
          'aiohttp'
    ],
    classifiers = [],
)