data = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Error: Invalid command. Please try again.")
        except ValueError:
            print("Error: Invalid input format. Please try again.")
        except IndexError:
            print("Error: Contact not found. Please try again.")
    return wrapper


def hello(args):
    print("How can I help you?")


@input_error
def add(args):
    splited_args = args.split()
    print(splited_args)
    if len(splited_args) != 2:
        raise ValueError
    name, phone = splited_args
    data[name] = phone
    print(data)
    print(f"Contact {name} with phone number {phone} has been added.")


@input_error
def change(args):

    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in data:
        data[name] = phone
    print(data)
    print(f"The phone number for contact {name} has been changed to {phone}.")


@input_error
def get_phone_number(args):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in data:
        print(f"The phone number for contact {name} is {data[name]}.")
    else:
        raise IndexError


@input_error
def show_all_contacts(args):
    if len(args) != 1 or args[0] != "all":
        raise ValueError
    if data:
        output = "Contacts:\n"
        for name, phone in data.items():
            output += f"{name}: {phone}\n"
        print(output)


COMMANDS = {
    "add": add,
    "hello": hello,
    "change": change,
    "phone": get_phone_number,
    "show": show_all_contacts
}

#def get_handler(user_input):
    #return COMMANDS[user_input]

def main_loop():

    while True:
        user_input = input(">>> ")
        user_input = user_input.lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        try:
        
            split_string = user_input.split(maxsplit=1)
            if len(split_string) > 1:
                command = split_string[0]
                args = split_string[1]
            else:
                command = user_input
                args = ""
            COMMANDS[command](args)
        except KeyError:
            print("Incorrect command.")
        


if __name__ == "__main__":
    main_loop()
