def d1(func):
    def _d1(*args, **kwargs):
        print(f"d1 here for start of {func.__name__}")
        func(*args,**kwargs)
        print(f"d1 here for end of {func.__name__}")
    return _d1

def d2(func):
    def _d2(*args, **kwargs):
        print(f"d2 here for start of {func.__name__}")
        func(*args,**kwargs)
        print(f"d2 here for end of {func.__name__}")
    return _d2

@d1
@d2
def fd(x):
    print(f"f says {x}")

if __name__ == "__main__":
    fd(5)