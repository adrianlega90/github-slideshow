"""Librerías importadas"""
import subprocess
import getpass
import socket
import sys
import shlex
import os

# Inicialización de las variables de entorno
os.environ["DAMSH_PS1"] = "\\u@\\h \\p (\\c) $"
os.environ["DAMSH_DEBUG"] = "0"

# Guardo en una variable el directorio de trabajo actual de un proceso
cwd = os.getcwd()


# Función main que sirve como punto de partida para la ejecución del programa
def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-h':  # Comprueba la lista de argumentos de comandos para mostrar o no el menú de ayuda
        command_help()
        exit()
    subprocess.run("touch ~/.damsh_history", shell=True)
    # Comprueba la lista de argumentos de comandos para mostrar o no el menú de ayudaBucle infinito donde dependiendo de lo que introducirá
    # Comprueba la lista de argumentos de comandos para mostrar o no el menú de ayudael usuario, el programa acturá de una manera u otra.
    # Comprueba la lista de argumentos de comandos para mostrar o no el menú de ayuda
    # Salir del bucle supone la salida del programa
    try:
        while True:
            user_input = input(parse_prompt())
            append_history(user_input)
            user_input_parsed = parse_commmands(user_input)
            log_user_input_parsed(user_input_parsed)

            if len(user_input_parsed) == 0:
                print("Comando vacío")
                continue

            if user_input_parsed[0] == "builtins":
                command_builtins(user_input_parsed)

            elif user_input_parsed[0] == "cd":
                commmand_cd(user_input_parsed)

            elif user_input_parsed[0] == "set":
                command_set(user_input_parsed)

            elif user_input_parsed[0] == "dam":
                print("Has descubierto un comando secreto")

            elif user_input_parsed[0] == "exit":
                print("La consola finalizó")
                exit()

            else:
                subprocess_output = subprocess.check_output(user_input_parsed, shell=True, cwd=cwd)
                subprocess_output = subprocess_output.decode("utf-8")
                print(subprocess_output)
    except EOFError:
        print("La consola finalizó")
        exit()


# Función donde si la varible DEBUG contiene un valor
# distinto de 0, muestra el mensaje de depuración
def log_user_input_parsed(user_input_parsed):
    if os.environ["DAMSH_DEBUG"] == "0":
        return
    print("User input parsed: " + str(user_input_parsed))


# Función que adjunta un comando que introduce el usuario
# al final del fichero de historia
def append_history(text):
    subprocess.run("echo " + text + " >> ~/.damsh_history", shell=True)


# Función donde se imprime la lista de builtins
def command_builtins(user_input_parsed=None):
    print("builtins")
    print("cd")
    print("set")
    print("dam")
    print("exit")


# Función donde establecemos las variables de entorno
def command_set(user_input_parsed=None):
    if len(user_input_parsed) != 4:
        print("Parámetros de comando incorrecto")
        return
    var_name = user_input_parsed[1]
    var_value = user_input_parsed[3]
    os.environ[var_name] = var_value


# Función que muestra el menú de ayuda
def command_help():
    print("damsh - The DAM shell \n\nUsage:\n  damsh              Enter the interactive shell \n  damsh -h           Print this help and exit \n  damsh -c COMMAND   Execute the given command and exit \n  damsh FILE.dsh     Execute commands in the script file and exit")


# Función que devuelve una lista en la que se ha guardado
# la cadena dividida de los datos introducidos por el usuario
def parse_commmands(user_input):
    s = shlex.shlex(user_input, punctuation_chars=True)
    s.whitespace_split = True
    return list(s)


# Función para sustituir la información que se encuentra
# antes del cursor, es decir donde empezamos a escribir
# los comandos que ingresamos a la shell
def parse_prompt():
    prompt_template = os.environ.get("DAMSH_PS1")
    last_error_code = 0 if os.environ.get("?") is None else os.environ.get("?")
    user_name = getpass.getuser()
    host_name = socket.gethostname()
    current_path = cwd
    prompt = prompt_template.replace("\\u", user_name)
    prompt = prompt.replace("\\h", host_name)
    prompt = prompt.replace("\\p", current_path)
    prompt = prompt.replace("\\c", str(last_error_code))
    return prompt


# Función donde se consigue mover de un directorio de trabajo
# a otro, siempre que exista
def commmand_cd(user_input_parsed=None):
    if not os.path.exists(user_input_parsed[1]):
        print("No existe")
        return
    global cwd
    cwd = user_input_parsed[1]


# Para estar seguro de que ese bloque solo se ejecutará
# si tu módulo es el programa principal
if __name__ == "__main__":
    main()
