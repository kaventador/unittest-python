def main():
    name = input("Enter Your Name : ")
    print(hello(name))


def hello(n='world'):
    return f"hello {n}"


if __name__ == '__main__':
    main()
