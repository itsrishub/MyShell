import os
import getpass
import subprocess

def _execute(command):
    try:
        subprocess.run(command.split(" "))
    except:
        print(f"command not found: {command}")

def _cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except:
        print(f"cd: no such file or directory: {path}")

def main():
    user = getpass.getuser( )
    while True:
        dir = os.getcwd()
        inp = input(f"{user}@MyShell {dir} ~> ")
        if inp == "exit" or inp == "quit":
            break
        elif "cd " in inp:
            _cd(inp.strip("cd "))
        else:
            _execute(inp)

if __name__ == "__main__":
    main()
