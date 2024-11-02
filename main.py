import string
from project_functions import is_ukrainian_letter, is_english_letter, is_russian_letter
from prigolosni_and_golosni_letters import ukrainian_letters, english_letters, russian_letters
#Скажите нормально распределил по файлам или нет, импортировать сразу весь файл не выходило или мб вызывал в коде что то не так после импорта
#Скажите нормально распределил по файлам или нет, импортировать сразу весь файл не выходило или мб вызывал в коде что то не так после импорта
#Скажите нормально распределил по файлам или нет, импортировать сразу весь файл не выходило или мб вызывал в коде что то не так после импорта
def issymbol(char):
    return char in string.punctuation

if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
    with open("new_text_file.txt", "w") as file:
        symbol_count = 0
        lines_count = 0
        vowels_count = 0
        consonants_count = 0
        digits_count = 0
        for line in lines:
            lines_count += 1
            for char in line:
                if issymbol(char):
                    symbol_count += 1
                if is_ukrainian_letter(char) or is_english_letter(char) or is_russian_letter(char):
                    if char in ukrainian_letters["голосні"] or char in english_letters["vowels"] or char in russian_letters["голосные"]:
                        vowels_count += 1
                    else:
                        consonants_count += 1
                if char.isdigit():
                    digits_count += 1
        file.write(f"Symbols: {symbol_count}, lines: {lines_count}, vowels: {vowels_count}, consonants: {consonants_count}, digits: {digits_count}")
