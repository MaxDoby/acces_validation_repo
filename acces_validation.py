incercari = 0
maximum_incercari = 3
parola = 'pixel700'

while incercari < maximum_incercari:
    user_input = input('\nIntroduceti parola: ')
    if user_input == parola:
        print('Acces permis!\nBine ati venit!')
        break
    incercari += 1

    incercari_ramase = maximum_incercari - incercari

    if incercari_ramase > 1:
        print('\n\tParola incorecta!')
        print('\tIncercari ramase:', incercari_ramase)
    elif incercari_ramase == 1:
        print('\n\tParola incorecta!'
              '\n\tAtentie! Ultima incercare, accesul va fi blocat!')
else:
    print('\n\tParola incorecta!'
          '\n\tAcces blocat! Contactati administratorul.')
