def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if ValueError():
      print ("add args")
    elif name in contacts:  
      contacts[name] = phone
    return "Contact updated successfully"

def show_contact(args, contacts):
    name, _ = args
    return contacts[name]

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add" and len(args) == 2:
            print(add_contact(args, contacts))

        elif command == "change" and len(args) == 2:
            print(change_contact(args, contacts))

        elif command == "show" and len(args) == 1:
            print(show_contact(args, contacts))

        elif command == "phone" and len(args) == 1:
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))


        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()