def permuatation_inner(elements, number, selection):
    if(len(selection) == number):
        print selection
        return
    for i in elements:
        selection.append(i)
        permuatation_inner(elements-{i}, number, selection)
        selection.pop()
    

def permuatation(elements, number=None):
    if number == None:
        number = len(elements)
    permuatation_inner(set(elements), number,[])


if __name__ == '__main__':
    permuatation([1,2,3,4,5,6,7],4)
