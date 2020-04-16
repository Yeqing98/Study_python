python不需要声明变量，直接进行赋值即可：
因为在其他语言中，给a进行赋值，那么a就是一个实实在在的量；
而在python中，给a赋值，仅仅是赋予a一个内存地址，而不是一个量，这个地址可以指向任何类型数据的存储空间。


type()函数的作用: 可以对变量的类型进行检查
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>


input()函数的作用：可以获取键盘输入

int()函数的作用：将参数转化为整数