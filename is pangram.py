def is_pangram(s):
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for i in alphabet:
        if i not in s :
            return False
    return True



pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))


liste_pangramme = ['machin', 'Portez ce vieux whisky au juge blond qui fume', 'Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre', 'bizarre']

for test in liste_pangramme:
  print(test, ' : ', is_pangram(test))