

with open("example.txt", "+a") as f:
    f.write("This is new content.")

with open("example.txt") as f:
    print(f.readline())