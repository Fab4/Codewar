def tower_builder(n_floors):
  n_floors += 1
  result = []
  for n in range(1, n_floors):
    floor = ''
    spaces = ''
    stars = ''
    
    # Spaces
    n_spaces = n_floors - n
    for j in range(1, n_spaces):
      spaces += ' '

    # Stars
    n_stars = 1 + (n - 1) * 2
    for j in range(n_stars):
      stars += '*'
    
    floor = spaces + stars + spaces
    result.append(floor)
      
  return result

# print(tower_builder(1))
# print(tower_builder(2))
# print(tower_builder(3))

n_etages = input('Combien d\'étages ? ')

tower = tower_builder(int(n_etages))
for i in tower:
  print(i)
