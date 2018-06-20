secret = 72

while True:
    guess = int(raw_input("Unesi i probaj pogoditi broj: "))

    if guess == secret:
        print "Bravo, uspio si."
        break

    elif guess < secret:
        print "Nisi pogodio, tvoj broj je manji od tajnog."

    else:
        print "Nisi pogodio, tvoj broj je veci od tajnog."