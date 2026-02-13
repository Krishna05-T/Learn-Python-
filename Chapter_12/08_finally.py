
def main():
    try:
        a = int(input("Enter the number : "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am always without carry about return ")


main()