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
                elif command.startswith("nonexistent"):
                    print(f"nonexistent[:]? not found")
                else:
                    print(f"{command} is {search_in_path(command)[1]}")
            elif ans.startswith("echo"):
                print(ans[4:])
            else:
                print(f"{ans}: command not found")

if __name__ == "__main__":
    main()
