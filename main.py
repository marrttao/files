if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()

    word_to_replace = input("Enter the word to replace: ")
    replacing_word = input("Enter the replacing word: ")

    with open("text_file.txt", "w") as file:
        for line in lines:
            if word_to_replace in line:
                line = line.replace(word_to_replace, replacing_word)
            file.write(line)