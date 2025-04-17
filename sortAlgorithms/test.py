def rueckwaerts_zaehlen(n):
    if n == 0:
        print("Fertig")
        return
    print(n)
    rueckwaerts_zaehlen(n-1)

def fakultaet(n):
    if n==0:
        return 1
    return n * fakultaet(n-1)

print(fakultaet(3))

def fakultaet(n, tiefe=0):
    einzug = "  " * tiefe
    print(f"{einzug}>> Aufruf: fakultaet({n})")

    if n == 0:
        print(f"{einzug}<< Rückgabe: 1 (Abbruchbedingung)")
        return 1

    ergebnis = n * fakultaet(n - 1, tiefe + 1)

    print(f"{einzug}<< Rückgabe: {n} * fakultaet({n - 1}) = {ergebnis}")
    return ergebnis

# Test
#fakultaet(3)