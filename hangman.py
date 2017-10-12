import random

naam = input("Hallo wat is je naam? ")
print("Hallo " + naam, "welkom bij galgje!")

list = [' banaan', 'soep', 'woord', 'coderclass', 'issam', 'codercrackers', 'huis', 'boom', 'midas', 'baggerbusters', 'python', 'html', 'css', 'javascript']
woord = random.choice(list)
print (woord)

countfouten = + 1
geraden = + 1
rondes = 5
goedeletter = ''

def galg1(galg1):
    print(--------)
print(galg1(galg1)






while True:
    letter = input("Geef een letter op of raad het woord raden met ? ")
    raad = input("Raad het woord")

    if letter in woord:
        print("Goedzo dat was de goede letter")
        goedeletter = (goedeletter + letter)
    elif letter == "?":
        if raad in woord:
            print("Goedzo je hebt het goed!")
            print(geraden)
    else:
        print("Jammer niet de goede letter")
        aantalfouten = + 1












