"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Martin Směták
email: smetakmartin@seznam.cz
"""

import random

# úvodní text hry
oddelovac = "_" * 47

print(f"""
Hi there!
{oddelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovac}
Enter a number: """
)

# vygenerování náhodného 4místného čísla, nesmí začínat 0 a nesmí obsahovat duplicity
while True:
    vygenerovane_cislo = str(random.randint(1000,9999))
    if len(set(vygenerovane_cislo)) == 4:
        break

# definice funkce - kontrola řádného vstupu uživatele
def kontrola_vstupu(hodnota):

    # musí obsahovat pouze číslice
    if not hodnota.isdigit():
        zneni_chyby = "Hodnota obsahuje nečíselné znaky."
    # musí obsahovat přesně 4 znaky
    elif len(hodnota) != 4:
        zneni_chyby = "Hodnota neobsahuje 4 čísla."
    # nesmí začínat 0
    elif hodnota.startswith("0"):
        zneni_chyby = "Hodnota nesmí začínat 0."
    # nesmí obsahovat duplicity (kontrola počtu unikátních znaků)
    elif len(set(hodnota)) < 4:
        zneni_chyby = "Hodnota nesmí obsahovat duplicity."
    # jinak je hodnota ok
    else:
        zneni_chyby = None

    return zneni_chyby

# definice funkce - vyhodnocení vstupu uživatele
def hadani(tip):
    
    # množina číslic ve vygenerovaném čísle - pro následný propočet cows
    znaky_hadane_cislo = set(vygenerovane_cislo)
    
    # identifikace počtu bulls a cows
    bulls = 0
    cows = 0
    
    for x, y in zip(tip, vygenerovane_cislo):
        if x == y:
            bulls += 1
        elif x in znaky_hadane_cislo:
            cows += 1
    
    # vyhodnocení počtu bulls a cows
    if bulls == 1:
        text_bulls = (f"""{bulls} bull""")
    else:
        text_bulls = (f"""{bulls} bulls""")
    
    if cows == 1:
        text_cows = (f"""{cows} cow""")
    else:
        text_cows = (f"""{cows} cows""")
    
    finalni_text = (f"""{text_bulls}, {text_cows}""")
    
    return finalni_text

# nastavení výchozího počtu tipů
pocet_tipu = 1

# nastavení smyčky, dokud uživatel neuhodne správné číslo
while True:

    # nastavení vstupu uživatele
    tip_uzivatele = input()

    # podmínka, když číslo bude uhodnuto; smyčka se ukončí
    if tip_uzivatele == vygenerovane_cislo:
        print(f"""
Correct, you've guessed the right number
in {pocet_tipu} guesses!
{oddelovac} 
That's amazing!"""
)
        break
    
    # pokud není číslo uhodnuto, roste počet tipů; smyčka pokračuje
    else:
        pocet_tipu += 1

        # přes funkci "kontrola_vstupu" probíhá kontrola, zda byly u vstupu dodrženy všechny požadavky, případně se vypíše charakter chyby
        chyba = kontrola_vstupu(tip_uzivatele)

        if chyba:
            print(f"""
{chyba}
{oddelovac}"""
)
                  
        # pokud je vstup zadán správně, dochází přes funkci "hadani" k vyhodnocení počtu bulls a cows
        else:
            print(f"""
{hadani(tip_uzivatele)}
{oddelovac}"""
)
