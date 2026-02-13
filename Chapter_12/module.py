def Myfun():
    print("Hello world!!")

Myfun()
print(__name__)

if __name__ == "__main__":
    print("if this code is directly executed by running the file its present in ")
else:
    print("exected form the module")


# __name show main when we execute form it file or it show module when we import this code and exceute from their 