class DecoratorClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def decorator(*args, **kwargs):
            print(f"The arguments are: {self.arg1}, {self.arg2}")
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            print("After the function")
        return decorator

@DecoratorClass("Bora", "Canbula")
def my_function(s):
    print(s)

my_function("Parallel Programming")
