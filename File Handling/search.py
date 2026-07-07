with open("example_file.txt","r") as f:
    content = f.read()
    if "Sar" in content:
        print("It is there")
    else:
        print("No it is not here")