count = 0

def permutations_rodstephens_norep(choices, index, number, selection, used):
    """ give index as zero, a list, number of selections and
    an empty list to get the combinations """
    global count
    if len(selection) == number:
        print [choices[i-1] for i in selection]
        count+= 1
        return

    i=1
    while i <= len(choices):
        if i not in used:
            selection.append(i)
            used.add(i)
            permutations_rodstephens_norep(choices,
                                           index+1, number, selection, used)
            selection.pop()
            used.remove(i)
        i+=1

def permutations(choices, number):
    if number > len(choices) or number < 0:
        raise Exception("Invalid Input")
    permutations_rodstephens_norep(choices, 0, number, [], set())


if __name__ == '__main__':
    permutations([1,2,3,4,5,6,7],4)
    print count
