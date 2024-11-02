if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
    with open("new_text_file.txt", "w") as new_file:
        for line in lines:
            words = line.split()
            new_words = []
            for word in words:
                if '*' in word:
                    word = word.replace('*', '&')
                elif '&' in word:
                    word = word.replace('&', '*')
                new_words.append(word)
            new_line = ' '.join(new_words)
            new_file.write(new_line + '\n')