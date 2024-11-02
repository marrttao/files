if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
        word = input("Word ")
        word_count = 0
        for line in lines:
            words = line.split()
            word_count += words.count(word)
        print(f"Word {word} was found {word_count} times.")