import builtins
import shlex

def main():
    try:
        while True:
            user_input = input("")
            user_input_parsed = parse_commmands(user_input)

            if len(user_input_parsed) == 0:
                print("Comando vacío")
                pass

            if user_input_parsed[0] == "builtins":
                command_builtins(user_input_parsed)

            elif user_input_parsed[0] == "cd":
                print("Has llamado a cd")
            elif user_input_parsed[0] == "set":
                print("Has llamado a set")
            elif user_input_parsed[0] == "dam":
                print("Has llamado a dam")
            elif user_input_parsed[0] == "exit":
                print("Has llamado a exit")
            else:
                print("Has llamado a un proceso no soportado")

                

    except EOFError:
        print("LA CONSOLA SE CERRARÁ")
        exit()

def command_builtins(user_input_parsed = None):
    print("builtins")
    print("cd")
    print("set")
    print("dam")
    print("exit")


def parse_commmands(user_input):
    s = shlex.shlex(user_input, punctuation_chars=True)
    s.whitespace_split = True
    return list(s)

if __name__ == "__main__":
    main()

