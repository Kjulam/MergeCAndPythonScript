import sys, os, uuid
from print_help import print_help
def main():
    try:
        args = sys.argv
        result_script = "#if false\n\"\"\"\n#endif\n"
        if len(args) < 3:
            print("错误：传入参数错误。")
            print_help()
            return 1
        else:
            c_or_cpp = os.path.splitext(args[1])[1][1:]
        if c_or_cpp != "c" and c_or_cpp != "cpp":
            print("错误：第一个应当是 C / C++ 语言的源代码文件（.c / .cpp）。")
            print_help()
            return 1
        if os.path.splitext(args[2])[1] != ".py":
            print("错误：第二个应当是 Python 语言的源代码文件（.py）。")
            print_help()
            return 1
        try:
            output_file = args[3]
        except IndexError:
            output_file = ""
            for i in __file__.split("\\" if os.name == "nt" else "/")[:-1]:
                output_file += f"{i}{"\\" if os.name == "nt" else "/"}"
            output_file += f"output{"\\" if os.name == "nt" else "/"}{{{str(uuid.uuid4())}}}.{c_or_cpp}"
            if not os.path.exists("output"):
                os.mkdir("output")
        with open(args[1], "r+", encoding="utf-8") as file:
            for lines in file.readlines():
                result_script += lines
        result_script += "\n#if false\n\"\"\"\n"
        with open(args[2], "r+", encoding="utf-8") as file:
            for lines in file.readlines():
                result_script += lines
        result_script += "\n#endif\n"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result_script)
        print(f"成功合并 \"{args[1]}\" 和 \"{args[2]}\" 到 {output_file}。")
    except PermissionError:
        print("错误：权限不够。")
    return 0

if __name__ == "__main__":
    main()


