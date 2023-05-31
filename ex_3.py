data = {}

def hello():
    print("hello")



def add(args):
    tokens = args.split()

    if len(tokens) != 2:
        raise 
    name, phone = tokens
    data[name] = phone
    print()