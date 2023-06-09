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


def spliting(args):
    return args.split()


def hello(args):
    return "How can I help you?"


def add(args):

    args = spliting(args)

    if len(args) != 2:
        raise ValueError
    name, phone = args
    data[name] = phone

    return f"Contact {name} with phone number {phone} has been added."


def change(args):

    args = spliting(args)

    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in data:
        data[name] = phone

    return f"The phone number for contact {name} has been changed to {phone}."


def get_phone_number(args):

    args = spliting(args)
    
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
    else:
        return "You don't have contacts in your phone book."


COMMANDS = {
    add: ["add",],
    hello: ["hello"],
    change: ["change"],
    get_phone_number: ["phone"],
    show_all_contacts: ["show all"] 
    }



@input_error
def get_func(user_input):
    succesfull_run = False
    for func, key_words in COMMANDS.items():
            for key in key_words:
                if user_input.startswith(key):
                    args = user_input.replace(key, "").strip()
                    result = func(args)
                    succesfull_run = True
                    break
    if not succesfull_run:
        raise KeyError                
    return result


def main_loop():

    while True:
        
        user_input = input(">>> ")
        user_input = user_input.lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        result = get_func(user_input)
        print(result)
        

if __name__ == "__main__":
    main_loop()


