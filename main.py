import random
import string
Letters=string.ascii_letters
c=""
while c!="w":
    c=random.choice(Letters)
    print(f"la lettre choisie est {c}")
