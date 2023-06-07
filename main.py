data = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Invalid command. Please try again."
        except ValueError:
            return "Error: Invalid input format. Please try again."
        except IndexError:
            return "Error: Contact not found. Please try again."
    return wrapper


def hello(args):
    return "How can I help you?"



def add(args):

    splited_args = args.split()

    if len(splited_args) != 2:
        raise ValueError
    name, phone = splited_args
    data[name] = phone

    return f"Contact {name} with phone number {phone} has been added."



def change(args):
    splited_args = args.split()

    if len(splited_args) != 2:
        raise ValueError
    name, phone = splited_args
    if name in data:
        data[name] = phone

    return f"The phone number for contact {name} has been changed to {phone}."


def get_phone_number(args):
    

    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in data:
        return f"The phone number for contact {name} is {data[name]}."
    else:
        raise IndexError



def show_all_contacts(args):
    

    if data:
        output = "Contacts:\n"
        for name, phone in data.items():
            output += f"{name}: {phone}\n"
        return output


COMMANDS = {
    add: ["add",],
    hello: ["hello"],
    change: ["change"],
    get_phone_number: ["phone"],
    show_all_contacts: ["show all"] 
    }


@input_error
def get_handler(func, args):
    return func(args)


def main_loop():

    while True:
        succesfull_run = False
        user_input = input(">>> ")
        user_input = user_input.lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        for func, key_words in COMMANDS.items():
            for key in key_words:
                if user_input.startswith(key):
                    args = user_input.replace(key, "").strip()
                    
                    
                    result = get_handler(func, args)
                    succesfull_run = True
                    print(result)
                    break
        if not succesfull_run:
            print("Invalid command")

if __name__ == "__main__":
    main_loop()


