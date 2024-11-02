if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
    if lines:
        del lines[-1]
    with open("new_text_file.txt", "w") as newfile:
        newfile.writelines(lines)