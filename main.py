if __name__ == "__main__":
    symbol = input("Enter a symbol: ")
    count = 0
    with open("text_file.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        words = line.split()
        for word in words:
            if symbol in word:
                count += 1
    print(f"Symbol '{symbol}' was found {count} times ")