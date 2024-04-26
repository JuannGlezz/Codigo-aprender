def warn_the_sheep(queue):
    if queue[-1]=="wolf":
        return "Pls go away and stop eating my sheep"
    else:
        queue.reverse()
        return "Oi! Sheep number " + str(queue.index("wolf")) + "! You are about to be eaten by a wolf!"
#Si introduces array de ovejas y lobos y el último es lobo dices pls go away y sino avisa contando desde el final el número
#de oveja que va a ser comida por un lobo
