# ShellAdder

> Is this a Python file? No... Why is there binary data inside?

<p align="center">English | <a href="./docs/README_zh.md">简体中文</a></p>

A Python tool that packages files into a Python script and automatically extracts and runs the specified file at runtime (similar to packing/adding a shell).

## Installation

Via Python package manager: (using pip as an example)

```sh
pip install ShellAdder
```

From source:

```sh
git clone https://github.com/XiaoshuDeXiaowo/ShellAdder.git
pip install .
```

## Usage

```
ShellAdder [-h] [-V] [-v] input_file_or_folder output executable_name

A tool to "pack" files into a Python script.

Positional arguments:
  input_file_or_folder  The zip file or folder to be "packed"
  output                The output Python filename
  executable_name       The Python script or executable file to run

Options:
  -h, --help            Show this help message and exit
  -V, --version         Show the version number and exit
  -v, --verbose         Output more information
```