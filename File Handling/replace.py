with open("example_file.txt" , "r") as f:
    content = f.read()
content = content.replace("Convert", "SATNC")

with open("example_file.txt", "w") as f:
    f.write(content)
