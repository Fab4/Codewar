def open_or_senior(data):
    result = []
    for i in range(len(data)):
        print(data[i])
        for j in range(len(data[i])):
            print(data[i][j])

    result = []
    for i in range(len(data)):
      if data[i][0] >= 55 and data[i][1] > 7:
        result.append('Senior')
      else:
        result.append(('Open'))
    return result


print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))