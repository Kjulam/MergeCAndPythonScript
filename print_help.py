def print_help():
    print("用法：python ./main.py /Path/to/your/c/script.c /Path/to/your/python/script.py /Path/to/the/result")
    print("说明：若为 Windows 系统，则应当替换为正确的路径，如 C:\\Users\\Administrator\\Desktop\\Script.py。")
    print("若第三条（结果目录）未指定，则默认输出到该项目的 output/ 目录下，并随机生成一个 UUID 作为结果的文件名，后缀为 .c。")
