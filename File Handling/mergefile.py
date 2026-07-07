with open("NewFile.txt","a") as dest , open("example_file.txt","r") as src:
    dest.write(src.read())
