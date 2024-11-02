if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if ',' not in line:
            lines[i] = line + "************\n"
    with open("new_text_file.txt", "w") as newfile:
        newfile.writelines(lines)