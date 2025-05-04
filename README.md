# C 语言和 Python 语言源代码的合并

- 该项目可以实现一个神奇的效果：将一个 C 语言的源代码和另一个 Python 语言的源代码合并到一个文件里，并且能让这个新的文件能够同时在
  gcc 的编译和 python 的解释下都能正常运行。
- 使用方法如下：

```
使用方法：程序名 <C / C++ 源文件> <Python 源文件> [输出文件]
示例：程序名 script.c script.py output.c
若第三条（结果目录）未指定，则默认输出到该项目的 output/ 目录下，并随机生成一个 UUID 作为结果的文件名，后缀为 .c（或 .cpp）。
```

_PS：直接使用 `python ./main.py` 可以输出这个使用方法。_

- 什么意思呢？举个例子就知道了。
- 例如在 D:\hello.py 中写了这样一段代码：

```python
def main():
    print("Hello from Python! ")
if __name__ == "__main__":
    main()
```

- 又在 D:\hello.c 中写了这样一段代码：

```c
#include <stdio.h>
int main() {
    printf("Hello from C! ");
    return 0;
}
```

通过该项目，会生成这样一个代码：

```python
#if false
"""
#endif
#include <stdio.h>
int main() {
    printf("Hello from C! ");
    return 0;
}
#if false
"""
def main():
    print("Hello from Python! ")
if __name__ == "__main__":
    main()
#endif
```

以上代码用 Python 解释器来看是这样的：

- 第 1 行：一个单行注释，不必理会。
- 第 2 ~ 10 行：全是多行注释，不必理会。
- 第 11 ~ 14 行：一段正常的代码，解释执行。
- 第 15 行：一个单行注释，不必理会。
- 因此最终会是原 Python 代码的效果。

而在 C 语言编译器来看是这样的：

```c
#if false
"""
#endif
#include <stdio.h>
int main() {
    printf("Hello from C! ");
    return 0;
}
#if false
"""
def main():
    print("Hello from Python! ")
if __name__ == "__main__":
    main()
#endif
```

- 第 1 行：预处理命令，如果否则执行下一行。
- 第 2 行：因为上面判断表达式为否，所以永远不会被执行。
- 第 3 行：预处理命令，表示第 1 行中如果语句块的结束。
- 第 4 ~ 8 行：正常的包含标准库、主函数，正常编译。
- 第 9 ~ 15 行：原理同 1 ~ 3 行。

灵感来源：[这段C++代码可以在Python上运行……](https://www.bilibili.com/video/BV1CUGqztE7U?spm_id_from=333.788.player.switch&vd_source=5d264f3a9523a65727db28a2c0a79e7e "Bilibili：sally4953")