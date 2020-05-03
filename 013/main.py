# 在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。
# 最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，finally块的代码不论程序正常还是异常都会执行到

def main():
    f = None
    try:
        f = open(r'D:\旅梦代码\python\Study_python\013\readme.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()