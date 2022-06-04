import ety
import string

letters = string.ascii_lowercase
# You can easily change the shift, by adjusting variable.
def cezar(word, shift=1):
    res = ""
    for letter in word:
        res += letters[(letters.index(letter) + shift) % len(letters)]
    return res

print(cezar("zzz"))

cezared_words = []
with open("./data/words_alpha.txt") as file:
    for line in file:
        line = line.strip()
        if ety.origins(cezar(line)):
            cezared_words.append(line)
            print(len(cezared_words))

with open("./data/cezared_words.txt", "w") as file:
    for word in cezared_words:
        file.write(f"{word} -> {cezar(word)}\n")
