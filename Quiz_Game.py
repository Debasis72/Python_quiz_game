print("(:------Well come to my gaming world--------:)")

game=input("Are you ready for play game Yes/No.?: ")

if game.lower() != 'yes':
    quit("Thank you")

print("Ok! Let's start the game:) ")
correct=0

quest=input("1. Who developed Python Programming Language?\n a) Wick van Rossum \n b) Rasmus Lerdorf \n c) Guido van Rossum \n d) Niene Stom \n enter answar:")

if quest.lower() =="c":
    print("Correct!")
    correct+=1
else:
    print("Incorrect!")

quest=input("""2. Which type of Programming does Python support?\n
a) object-oriented programming\n
b) structured programming\n
c) functional programming\n
d) all of the mentioned\n
enter answar:""")
if quest.lower() =="d":
    print("Correct!")
    correct+=1
else:
    print("Incorrect!")

quest=input("""3. Is Python case sensitive when dealing with identifiers?\n
a) no\n
b) yes\n
c) machine dependent\n
d) none of the mentioned \n enter answar:""")
if quest.lower() =="b":
    print("Correct!")
    correct+=1
else:
    print("Incorrect!")

quest=input("""5. Is Python code compiled or interpreted?\n
a) Python code is both compiled and interpreted\n
b) Python code is neither compiled nor interpreted\n
c) Python code is only compiled\n
d) Python code is only interpreted \n enter answar:""")

if quest .lower() =="a":
    print("Correct!")
    correct+=1
else:
    print("Incorrect!")

quest=input(""" 6. All keywords in Python are in _________\n
a) Capitalized\n
b) lower case\n
c) UPPER CASE\n
d) None of the mentioned\n enter answar:""")

if quest .lower() =="d":
    print("Correct!")
    correct+=1
else:
    print("Incorrect!")
print("---------------------")
print("You have score: " + str(correct)+ "Out of 6")