def decorator(say_hello):
    def wrap():
        print("=======")
        say_hello()
        print('=======')
    return wrap


@decorator
def say_hello():
    print("Hello world!")
    
    
say_hello()