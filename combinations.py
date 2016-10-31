def combinations_inner(index, choices, number, selection):
    """ give index as zero, a list, number of selections and
    an empty list to get the combinations """
    if number > len(choices) or number < 0:
        raise InputError()
    if len(selection) == number:
        print selection
        return

    start = index;
    end = len(choices) - (number - len(selection)) + 1
    while start < end:
        selection.append(choices[start])
        start+=1
        combinations_inner(start, choices, number, selection)
        selection.pop()

def combinations(choices, number):
    combinations_inner(0,choices, number,[])


if __name__ == '__main__':
    combinations([1,2,3,4,5,6,7],4)
