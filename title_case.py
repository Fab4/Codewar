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