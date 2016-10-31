count = 0

def combinations_rodstephens(choices, index, number, selection):
    """ give index as zero, a list, number of selections and
    an empty list to get the combinations """
    global count
    if number > len(choices) or number < 0:
        raise Exception("Invalid Input")
    if len(selection) == number:
        print [choices[i-1] for i in selection]
        count+= 1
        return

    start = 1;
    if index > 0:
        start = selection[index -1]
    i = start
    while i <= len(choices):
        selection.append(i)
        i+=1
        combinations_rodstephens(choices, index+1, number, selection)
        selection.pop()

def combinations(choices, number):
    combinations_rodstephens(choices, 0, number, [])


if __name__ == '__main__':
    combinations([1,2,3,4,5,6,7],4)
    print count
