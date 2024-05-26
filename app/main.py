import sys
import os

def search_in_path(program):
    path = os.environ.get("PATH", "")
    if path:
        for location in path.split(":"):
            if os.path.isdir(location):
                if program in os.listdir(location):
                    program_path = os.path.join(location, program)
                    if os.access(program_path, os.X_OK):
                        return True, program_path
    return False, ""

def main():
    builtins = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        if ans := input().strip():
            if ans == "exit 0":
                sys.exit(0)
            elif ans.startswith("type "):
                command = ans[5:].strip()
                if command in builtins:
                    sys.stdout.write(f"{command} is a shell builtin\n")
                else:
                    found, command_path = search_in_path(command)
                    if found:
                        sys.stdout.write(f"{command} is {command_path}\n")
                    else:
                        sys.stdout.write(f"{command}: command not found\n")
            elif ans.startswith("echo "):
                sys.stdout.write(f"{ans[5:]}\n")
            else:
                sys.stdout.write(f"{ans}: command not found\n")

if __name__ == "__main__":
    main()
