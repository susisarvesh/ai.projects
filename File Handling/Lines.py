with open("example_file.txt","r") as f:
    content = f.read()
print(len(content.splitlines()))