import random

words = ["יביב", "הז", "אל", "היה", "הרוק"]

random.shuffle(words)
words[random.randint(0, 4)] += "ל"

print(" ".join(words))
