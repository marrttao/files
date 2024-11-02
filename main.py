if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
        longest_line = ""
        for line in lines:
            if len(line) > len(longest_line):
                longest_line = line
        print(longest_line)