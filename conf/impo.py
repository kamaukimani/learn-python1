# from os import name
# print(name)
import os
import locale
import random
print(os)
if os.name == "posix":
    print("Running on Linux or macOs or Unix")
elif os.name == "nt":
    print("Running on windows")
else:
    print("Running on jython")

# print(from os import *)
# import os
# print(dir(os))
print(locale.getpreferredencoding())
print(os.path.exists("/home/paul/moringa/python/49.pdf"))

# text_file=open("/home/paul/moringa/python/49.pdf",encoding='utf-8')
# text_file.read()

with open("/home/paul/moringa/python/49.pdf","rb") as pdf:
    data=pdf.read()
    print(type(data))

print(os.path.exists("/home/paul/moringa/learn-python1/classes/song1.py"))
with open("/home/paul/moringa/learn-python1/classes/song1.py") as file:
    content=file.read()
    #for line in file:
        #print(line)
print(content)
print(".........................................PROGRAMMING..................................................")
print(os.path.exists("/home/paul/Desktop/mindset/mindset.txt"))
with open("/home/paul/Desktop/mindset/mindset.txt",encoding="utf-8") as file:
    for line in file:
        print(line)

with open("log_file.txt",mode="w",encoding="utf-8") as log_file:
    log_file.write("Hello file 1.\n")

with open("log_file.txt",mode="a",encoding="utf-8") as log_file:
    log_file.write("Append this text to file")

with open("log_file.txt",mode="w",encoding="utf-8") as log_file:
    log_file.write("I have overwritten this file..............")

words=[
    "python",
    "learning",
    "success",
    "discipline",
    "practice",
    "curiosity",
    "algorithm",
    "growth"
]
with open("random_text.txt","w") as file:
    for _ in range(100):
        sentence=" ".join(random.choices(words,k=10))
        file.write(sentence+"." + "\n")



sentences=[
    "Learning everyday builds confidence.",
    "Programming improves problem-solving skills.",
    "Consistency beats motivation over time.",
    "Practice is more important than talent.",
    "Curiosity leads to discovery.",
    "Failure is part of the learning process"
]
with open("text.txt","w") as file:
    for _ in range(50):
        file.write(random.choice(sentences) + "\n")