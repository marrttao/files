if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()

    word_to_replace = input("Enter the word to replace: ")
    replacing_word = input("Enter the replacing word: ")

    with open("text_file.txt", "w") as file:
        for line in lines:
            words = line.split()
            new_words = []
            for word in words:
                if word_to_replace in word:
                    word = word.replace(word_to_replace, replacing_word)
                new_words.append(word)
            new_line = ' '.join(new_words)
            file.write(new_line + '\n')