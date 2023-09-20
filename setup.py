from setuptools import setup, find_packages

setup(
    name='trello_assist',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'trello_assist=trello_assist.main:main',
        ],
    },
)
