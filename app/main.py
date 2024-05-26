import sys
import os

def find_command_in_path(command):
        path_dirs = os.environ.get("PATH", "").split(os.pathsep)
        for dir in path_dirs:
            potential_path = os.path.join(dir, command)
            if os.path.isfile(potential_path) and os.access(potential_path, os.X_OK):
                return potential_path
        return None
    
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #sys.stdout.write("$ ")
    #sys.stdout.flush()
    built = ["exit", "echo", "type"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        if ans := input().strip():
            if ans == "exit 0":
                sys.exit(0)
            if ans[4:] in built:
                sys.stdout.write(f"{ans[4:]} is a shell builtin\n")
            elif "echo" in ans:
                print(f"{ans[4:]}")
            else:
                print(f"{ans[4:]}: command not found")
                paths = os.getenv("PATH").split(":")
                for path in paths:
                    if os.path.exists(f"{path}/{ans[4:]}"):
                        sys.stdout.write(f"{ans[4:]} is {path}/{ans[4:]}\n")
                        sys.stdout.flush()
                        return
                else:
                    print(f"{ans[4:]}: command not found")



if __name__ == "__main__":
    main()
