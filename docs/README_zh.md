# ShellAdder

> 这是一个 Python 文件？不对，里面怎么还有二进制的东西……

<p align="center"><a href="./../README.md">English</a> | 简体中文</p>

使用 Python 将一些文件打包成 Python 文件并在运行时自解压并运行指定的文件（类似于加壳）

## 安装

通过 Python 包管理器：（以 pip 为例）

```sh
pip install ShellAdder
```

从源代码：

```sh
git clone https://github.com/XiaoshuDeXiaowo/ShellAdder.git
pip install .
```

## 用法

```
ShellAdder [-h] [-V] [-v] input_file_or_folder output executable_name

一个为一些文件“加壳”成 Python 文件的工具。

位置参数:
  input_file_or_folder  要“加壳”的 zip 文件或文件夹
  output                输出的 Python 文件名
  executable_name       要执行的 Python 文件或可执行文件名

选项:
  -h, --help            显示此帮助信息并退出
  -V, --version         显示版本号并退出
  -v, --verbose         输出更多信息
```

