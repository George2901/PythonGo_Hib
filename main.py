import ctypes


def setup():
    import os 
    os.chdir('./golang')
    os.system('go build -o dlls/main.dll -buildmode=c-shared')
    os.chdir('../')
    

# setup()

def main():
    import ctypes

    # Load the DLL
    mydll = ctypes.WinDLL("golang/dlls/main.dll")

    # Define the argument and return types of the function
    mydll.Print.argtypes = [ctypes.c_char_p]
    mydll.Print.restype = ctypes.c_char_p

    # Call the function
    result = mydll.Print(b"my string argument")

    # Convert the result to a Python string
    result_str = result.decode('utf-8')
    print(result_str)

main()


