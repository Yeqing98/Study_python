def mydecorator(f):# f is the function passed to us from python
    def log_f_as_called():
        print(f'{f} was called.') 
    f()
    return log_f_as_called

@mydecorator
def hello():
    print('hello')


hello()