data = {}


def hello(args):
    print(data)


def add(args):
    print(f"add{args}")

    if len(args) != 2:
        print(args)
        return
    name, phone = args
    data[name] = phone
    print()


COMMANDS = {
    "add": add,
    "hello": hello
}


def main_loop():
    
    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
        splitted = user_input.split()
        if len(splitted) == 0:
            continue
        print(splitted)
        command = splitted[0]
        args = splitted[1:]
        print(args)
        try:
            COMMANDS[command](args)
        except KeyError:
            print("Incorrect commands")


if __name__ == "__main__":
    main_loop()

