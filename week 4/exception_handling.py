try: 
    number = int(input("Please enter a number: "))
    result =  1/ number
except Exception as e:
    print(f"An error has occured: {e} ")
    print(f"An error has occured: {repr(e)} ")
    print(type(e).__name__)
else: 
    print(f"Everyting is allright {result}")
finally: 
    print("Everything ok.")