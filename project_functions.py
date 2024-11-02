from prigolosni_and_golosni_letters import ukrainian_letters, english_letters, russian_letters
def is_ukrainian_letter(char):
    return char in ukrainian_letters["голосні"] or char in ukrainian_letters["приголосні"]

def is_english_letter(char):
    return char in english_letters["vowels"] or char in english_letters["consonants"]

def is_russian_letter(char):
    return char in russian_letters["голосные"] or char in russian_letters["согласные"]
