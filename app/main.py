import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    #print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    #sys.stdout.write("$ ")
    #sys.stdout.flush()

    # Wait for user input
    while True:
        ans = input()
        print(f"{ans}: command not found\n")
        sys.stdout.write("$ ")



if __name__ == "__main__":
    main()
