
import random
import string

# Erlaubte Zeichen
zeichen = string.ascii_letters + string.digits + "_"

# 18.000 eindeutige Wörter mit genau 3 Zeichen generieren
woerter = set()

while len(woerter) < 18000:
    wort = "".join(random.choices(zeichen, k=3))
    woerter.add(wort)

# In Datei speichern
with open("woerter.txt", "w", encoding="utf-8") as datei:
    datei.write("\n".join(woerter))

print(f"{len(woerter)} Wörter wurden erfolgreich erstellt!")
