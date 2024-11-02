if __name__ == "__main__":
    lines = ["That cool!", "idk why", "but its cool", "dumb text xD", "And again, thats cool"]
    with open("text_file.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")
