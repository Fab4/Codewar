def queue_time(customers, n):
  
  # Initialise les n caisses avec t = 0.
  caisses = []
  for i in range(n):
    caisses.append(0)

  # pour chaque valeur de la liste "customers"
  for i in customers:
    # Classe les caisses de la plus petite à la plus grande
    caisses.sort()
    # Ajoute à la première de ces caisses (donc celle dont la valeur est la plus petite) le temps)
    caisses[0] += i

  # Classe les caisses de la plus grande à la plus petite.
  caisses.sort(reverse=True)
  # Renvoie la première caisse de la liste, donc celle qui a la plus grande valeur.
  return caisses[0]



print(queue_time([], 1))
print(queue_time([5], 1))
print(queue_time([2], 5))
print(queue_time([1,2,3,4,5], 1))
print(queue_time([1,2,3,4,5], 100))
print(queue_time([2,2,3,3,4,4], 2))