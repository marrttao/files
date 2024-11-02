if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
    with open("new_text_file.txt", "w") as new_file:
        for line in lines:
            if '*' in line:
                line = line.replace('*', 'TEMP_PLACEHOLDER')
            if '&' in line:
                line = line.replace('&', '*')
            line = line.replace('TEMP_PLACEHOLDER', '&')  #без плейсхолдера почему-то не работает + прочитал что это
            new_file.write(line)