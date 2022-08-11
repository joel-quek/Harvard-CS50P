def sq_in_rect(side1, side2):
    dim = [side1, side2]
    dim.sort()
    small = dim[0]
    large = dim[1]

    square_list = []

    if small == large:
        return None

    else:
        while small > 0:

            square_list.append(small)
            new = large - small
            newrect = [new, small]
            newrect.sort()
            small = newrect[0]
            large = newrect[1]

        square_list.sort(reverse= True)
        return square_list