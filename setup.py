# coding: utf-8
from setuptools import setup
from ShellAdder import __version__ as ShellAdder_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read().replace('./', 'https://github.com/XiaoshuDeXiaowo/ShellAdder/')

setup(
    name='ShellAdder',
    version=ShellAdder_version,
    packages=[''],
    url='https://github.com/XiaoshuDeXiaowo/ShellAdder',
    license='The MIT License',
    author='XiaoshuDeXiaowo',
    author_email='',
    description='一个为一些文件“加壳”成 Python 文件的工具。',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ShellAdder = ShellAdder:main",
        ],
    }
)
