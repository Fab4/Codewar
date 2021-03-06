def find_even_index(arr):
    for i in range(len(arr)):
        sommeDroite = 0
        sommeGauche  = 0
        for j in range(0, i):
            sommeGauche += arr[j]
        for j in range(i+1, len(arr)):
            sommeDroite += arr[j]
        if sommeDroite == sommeGauche:
            return i
    return -1


def affiche_liste_index(liste):
  for index in range(len(liste)):
    print('index = ', index, 'élément = ', liste[index])
  print('\n')


debug = True

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))
print(find_even_index(list(range(1,100))))
print(find_even_index([0,0,0,0,0]), "Should pick the first index if more cases are valid")
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
print(find_even_index(list(range(-100,-1))))