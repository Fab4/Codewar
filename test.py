#%%
# %%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet: print(i)

# %%
for i in range(1114111): print(chr(i))
# %%
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(list(enumerate(alphabet)))

# %%
def inc(x):
  return x+1

def dec(x):
  return x-1

def operate(func, x):
  result = func(x)
  return result

print(operate(inc, 3))
print(operate(dec, 3))
# %%
def alfabet_position(text):
  result = ''
  for c in text.lower():
    if c.isalpha():
      result += ' '.join(str(ord(c) - 96))
  return result

print(alfabet_position('Portez ce vieux whisky au juge blond qui fume'))
print(alfabet_position("The sunset sets at twelve o' clock."))
print(alfabet_position("The narwhal bacons at midnight."))
# %%
def alfabet_position(texte):
  result = []
  for c in texte.lower():
    if c.isalpha():
      cc = str(ord(c)-96)
      print(c, cc)
      # result.append(cc)
  return ' '.join(result)

# print(alfabet_position('Portez ce vieux whisky au juge blond qui fume'))
# print(alfabet_position("The sunset sets at twelve o' clock."))
# print(alfabet_position("The narwhal bacons at midnight."))
print(alfabet_position('abcdefghijklmnopqrstuvwxyz'))
# %%
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('%'.join(alfabet))
# %%
def title_case(title, minor_words=''):
    result = []
    for word in title.lower().split(' '):
      if word not in minor_words.lower().split():
          result.append(word.capitalize())
      else:
          result.append(word)
    result[0] = result[0].title()
    return (' '.join(result))


print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))
print(title_case('First a of in', 'an often into'))

# %%
def stock_list(listOfArt, listOfCat):
    # pass
    result =[]
    for i in listOfCat:
      total = 0
      for j in listOfArt:
        if j.index(i):
          liste = j.split(' ')
          total += int(liste[1])
      result.append(total)
    
    return total

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
# %%
def stock_list(listOfArt, listOfCat):
    for i in listOfCat:
        print(i)
        for j in listOfArt:
            # if j.split(' ')[0] == i:
            #     print(j.split()[1])
          print(j.split()[0][0])
          print(j.split()[1])


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
# %%
def stock_list(listOfArt, listOfCat):
    result = ""
    for i in listOfCat:
      total = 0
      for j in listOfArt:
        if j.split(' ')[0][0] == i:
            total += int(j.split()[1])
      if result != "": result += " - "
      if total != 0: result += "(" + i + " : " + str(total) + ")"
    if result != "": return result

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "Z"]
print(stock_list(b, c))
# %%
# Calcul suite de Fibonacci.
a = 0
b = 1
c = 0
print(a)
print(b)
while c < 1E100:
  c = a + b
  a = b
  b = c
  print(c)
# %%
# Calcul du facteur des termes 2 à 2 des éléments de la suite de Fibonacco.
a = 0
b = 1
c = 0
print('{} * {} = {}'.format(a, b, a * b))
while c < 1E6:
  c = a + b
  a = b
  b = c
  print('{} * {} = {}'.format(a, b, a * b))

# %%
a = 5
b = 4.8

print('a={} et b={}'.format(a, b))

# %%
