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
            elif "type" in ans:
                if "nonexistent" in ans:
                    print(f"{ans[4:]} not found")
                elif ans[4:] in built:
                    print(f"{ans} is a shell builtin")
                else:
                    command_path = find_command_in_path(ans[4:])
                    print(f"{ans[4:]} is {command_path}")
            elif "echo" in ans:
                print(f"{ans[4:]}")
            else:
                print(f"{ans}: command not found")



if __name__ == "__main__":
    main()
