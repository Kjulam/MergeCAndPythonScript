def print_help():
    print("使用方法：程序名 <C / C++ 源文件> <Python 源文件> [输出文件]")
    print("示例：程序名 script.c script.py output.c")
    print("若第三条（结果目录）未指定，则默认输出到该项目的 output/ 目录下，并随机生成一个 UUID 作为结果的文件名，后缀为 .c（或 .cpp）。")
