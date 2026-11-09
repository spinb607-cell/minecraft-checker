
import random
import string

# Erlaubte Zeichen
zeichen = string.ascii_letters + string.digits + "_"

# Deine gewünschten Namen
woerter = {
    "2sa", "zs7", "vel", "fck", "nig", "fkc",
    "fik", "ejc", "fag", "gjv", "yi2", "2_b",
    "ukl", "h03", "49m", "6x_", "9zx", "uxg",
    "2v6", "jji", "tb9", "8c9", "G3b", "pi8",
    "lg_"
}

# Weitere eindeutige Wörter generieren
while len(woerter) < 18000:
    wort = "".join(random.choices(zeichen, k=3))
    woerter.add(wort)

# Durchmischen
woerter = list(woerter)
random.shuffle(woerter)

# In words.txt speichern
with open("words.txt", "w", encoding="utf-8") as datei:
    datei.write("\n".join(woerter))

print("Erfolgreich!")
print(f"{len(woerter)} Wörter wurden in words.txt gespeichert.")
