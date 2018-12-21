try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Receive args and print it out.',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex4'],
    'scripts': [],
    'name': 'ex4'
}

setup(**config)