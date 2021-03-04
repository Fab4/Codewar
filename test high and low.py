def high_and_low(numbers):

    list = []
    car = ""
    n = numbers + " "
    for i in n:
        if i != " ":
            car = car + i
        else:
            list.append(int(car))
            car = ""

    if len(list) == 1:
        numbers = str(list[0]) + " " + str(list[0])
        return numbers

    min = list[0]
    max = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
        if max < list[i]:
            max = list[i]
    
        numbers = str(max) + " " + str(min)
    
    return numbers


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
print(high_and_low("1 -1"), "1 -1")
print(high_and_low("1 1"), "1 1")
print(high_and_low("-1 -1"), "-1 -1")
print(high_and_low("1 -1 0"), "1 -1")
print(high_and_low("1 1 0"), "1 0")       
print(high_and_low("-1 -1 0"), "0 -1")
print(high_and_low("42"), "42 42")