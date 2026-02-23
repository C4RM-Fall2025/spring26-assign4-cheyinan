def FizzBuzz(start, finish):
    mylist = []
    for i in range(start, finish + 1):
        if i % 15 == 0:
            mylist.append("fizzbuzz")
        elif i % 3 == 0:
            mylist.append("fizz")
        elif i % 5 == 0:
            mylist.append("buzz")
        else:
            mylist.append(i)
    return mylist
