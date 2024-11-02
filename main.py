if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()

    with open("new_text_file.txt", "w") as new_file:
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) >= 7:
                    new_file.write(word + "\n")
