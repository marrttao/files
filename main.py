if __name__ == "__main__":
    with open("first_text_file.txt", "r") as file:
        lines_one = file.readlines()
    with open("second_text_file.txt", "r") as file:
        lines_two = file.readlines()
    printed_lines = set()
    for line_one in lines_one:
        for line_two in lines_two:
            #тут скажете что лишние строки но без них результат дублировался (без проверки есть ли строка в списке строк которые мы записали)
            #тут скажете что лишние строки но без них результат дублировался (без проверки есть ли строка в списке строк которые мы записали)
            #тут скажете что лишние строки но без них результат дублировался (без проверки есть ли строка в списке строк которые мы записали)
            if line_one != line_two:
                if line_one not in printed_lines:
                    print(line_one)
                    printed_lines.add(line_one)
                if line_two not in printed_lines:
                    print(line_two)
                    printed_lines.add(line_two)