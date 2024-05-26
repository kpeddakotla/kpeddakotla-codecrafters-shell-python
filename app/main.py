import sys
import os


def search_in_path(program):
    path = os.environ.get("PATH", "")
    if path:
        for location in path.split(":"):
            if os.path.isdir(location):
                if program in os.listdir(location):
                    return True, os.path.join(location, program)
    return False, ""

def main():
    
    built = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        if ans := input().strip():
            if ans == "exit 0":
                sys.exit(0)
            elif ans.startswith("type"):
                command = ans[4:].strip()
                if command in built:
                    print(f"{command} is a shell builtin")
                    continue
                elif search_in_path(command)[0]:
                    print(f"{command} is {search_in_path(command)[1]}")
                    continue
                else:
                    print(f"{command} not found")
            elif ans.startswith("echo"):
                print(ans[4:])
            else:
                found = False
                command_args = ans.split(" ")

                if os.path.exists(f"{ans[0]}"):
                    os.system(f"{command_args[0]} {' '.join(command_args[1:])}")
                    found = True
                if not found:
                    sys.stdout.flush()
                    command = ans[4:].strip()
                    output = f"{command}: command not found"
                    sys.stdout.write(output)


if __name__ == "__main__":
    main()
