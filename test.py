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
      result.append(cc)
  return ' '.join(result)

# print(alfabet_position('Portez ce vieux whisky au juge blond qui fume'))
# print(alfabet_position("The sunset sets at twelve o' clock."))
print(alfabet_position("The narwhal bacons at midnight."))
# %%
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('%'.join(alfabet))
# %%
