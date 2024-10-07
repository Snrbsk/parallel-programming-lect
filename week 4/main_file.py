import other_file
from other_file import *

function_public()

try:
    _function_protected()
except Exception as e:
    print(f"An error has occured: {e} ")

#protected func usage
other_file._function_protected()

other_file.__function_private()


other_class = other_file.OtherClass()

print(other_class.public_var)
print(other_class._protected_var)

try:
    print(other_class.__private_var)
except Exception as e:
    print(f"An error has occured: {e} ")

#just static
print(other_class._OtherClass__private_var)