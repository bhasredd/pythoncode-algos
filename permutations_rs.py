count = 0

def permutations_rodstephens(choices, index, number, selection):
    """ give index as zero, a list, number of selections and
    an empty list to get the combinations """
    global count
    if len(selection) == number:
        print [choices[i-1] for i in selection]
        count+= 1
        return

    i=1

    while i <= len(choices):
        selection.append(i)
        i+=1
        permutations_rodstephens(choices, index+1, number, selection)
        selection.pop()

def permutations(choices, number):
    if number > len(choices) or number < 0:
        raise Exception("Invalid Input")
    permutations_rodstephens(choices, 0, number, [])


if __name__ == '__main__':
    permutations([1,2,3,4,5,6,7],4)
    print count
