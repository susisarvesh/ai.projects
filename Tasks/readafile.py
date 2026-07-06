with open("example.txt", "r") as file:
    content = file.read()

    count_lines = len(content.splitlines())
    count_words = len(content.split())
    count_letters = len(content)

    print("Lines:", count_lines)
    print("Words:", count_words)
    print("Letters:", count_letters)