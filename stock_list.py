def stock_list(listOfArt, listOfCat):
    if listOfArt == [] or listOfCat == []: return ''
    result = ''
    sub_total = []
    flag = False
    for i in listOfCat:
      total = 0
      for j in listOfArt:
        if j.split(' ')[0][0] == i:
            total += int(j.split()[1])
            if total != 0: flag = True
      if result != '': result += ' - '
      result += '(' + i + ' : ' + str(total) + ')'
    if result != '': 
      if flag == True: return result
      else: return ''


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "Z"]
print(stock_list(b, c))
b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = []
print(stock_list(b, c))
b = []
c = []
print(stock_list(b, c))