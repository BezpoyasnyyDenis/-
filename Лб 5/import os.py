import os

text = "Vedmak.txt"

def words_1(text_file):
    with open(text_file, encoding = "utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words1 = text.split()
    words1.sort()
    return words1


def words_2(words_1):
    words2 = dict()
    for word in words_1:
        if word in words2:
            words2[word] = words2[word] + 1
        else:
            words2[word] = 1
    return words2


def symbols_1(text_file):
    with open(text, encoding="utf8") as file:
        symbols1 = file.read()
    symbols1 = symbols1.replace("\n", " ")
    symbols1 = symbols1.lower()
    return symbols1


def symbols_2(text_file):
    with open(text, encoding="utf8") as file:
        symbols2 = file.read()
    symbols2 = symbols2.replace("\n", " ")
    symbols2 = symbols2.lower()
    symbols2 = symbols2.replace(" ", "")
    return symbols2

 
def main(): 
    text_file = "Vedmak.txt"
    words1 = words_1(text_file)
    words2 = words_2(words_1)
    symbols1 = symbols_1(text_file)
    symbols2 = symbols_2(text_file) 
    print("Слова: %d" % len(words1))
    print("Слова, що не повторюються: %d" % len(words2))
    print("Символи: %d" % len(symbols1))
    print("Cимволи без пропусків: %d" % len(symbols2))
    
    
if __name__ == "__main__":
        main()
input()