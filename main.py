import string
def issymbol(char): #сделал функцию что бы скоротить код (мог бы сделать паттерном либо словарем)
    return char in string.punctuation
if __name__ == "__main__":
    with open("text_file.txt", "r") as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            count += 1
        print(count)