with open("file1.txt", "r") as file1:
    lines = []
    for i in range(2):
        line = file1.readline()
        if line:  
            lines.append(line)


with open("file2.txt", "w") as file2:
    file2.writelines(lines)


with open("file2.txt", "r") as file2:
    content = file2.read()
    print(content)
