import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        ans = input()
        if ans:
            if ans == "exit 0":
                sys.exit(0)
            else:
                print(f"{ans}: command not found")



if __name__ == "__main__":
    main()
