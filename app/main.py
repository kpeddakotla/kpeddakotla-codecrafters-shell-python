import sys

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
                else:
                    print(f"/usr/local/{command}")
            elif ans.startswith("echo"):
                print(ans[4:])
            else:
                print(f"{ans}: command not found")

if __name__ == "__main__":
    main()
