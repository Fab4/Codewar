def high(x):
  listemots =[]
  mot = ''
  score = 0
  scoresmots = []
  # créer une liste avec les mots.
  for i in x:
    if i.isalpha():
      mot += i
    else:
      listemots.append(mot)
      mot=''
  listemots.append(mot)
# Créer la liste des scores.
  for mot in listemots:
    for i in mot:
      score += ord(i) - 96
    scoresmots.append(score)
    score = 0
# Cherche la position (l'index) du score le plus élevé (max)
# Avec cette index renvoie le mot de 'listemots' concerné.
  return listemots[scoresmots.index(max(scoresmots))]

print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))