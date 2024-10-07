class OtherClass:
    public_var =1
    _protected_var =2
    __private_var =3


def function_public():
    print("I am public func")

# '_' should be protected a little bit
def _function_protected():
    print("I am protected func")

def __function_private():
    print("I am private func")