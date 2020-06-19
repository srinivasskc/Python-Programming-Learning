import random

def getAnswer(number):
    if number==1:
        return "Yes..It is One"
    elif number == 2:
        return "Hmm.. It is Two"
    elif number==3:
        return "Ahh...It is Three"
    elif number==4:
        return "Finally, It is Four"
    elif number==5:
        return "Are you sure? It is Five"

print(getAnswer(random.randint(1,5)))
