import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "JShoter",
    version = "1.0",
    author = "Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    license = "MIT",
    keywords = ["JShoter", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/DevanshRaghav75/grepX",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'bs4',
        'requests',
    ],

    entry_points={
        'console_scripts': [
            'jshoter = JShoter.__main__:main'
        ]
    },
)
