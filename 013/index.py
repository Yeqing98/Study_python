import time

# 上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，

def main():
    # 一次性读取整个文件内容
    with open(r'D:\旅梦代码\python\Study_python\013\readme.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open(r'D:\旅梦代码\python\Study_python\013\readme.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open(r'D:\旅梦代码\python\Study_python\013\readme.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
