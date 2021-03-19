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
