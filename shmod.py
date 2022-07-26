import dogma

root_note = str(input('Input root note: '))  # retrieve root note of mode

mode = str(input('Input mode name: '))  # retrieve name (type) of mode


def interval(bottom, intrvl):  # returns top note of interval by its bottom note and name 'intrvl'

    if str(intrvl) == 'au0':

        for i in range(len(dogma.au0)):

            if bottom in dogma.au0[i] and dogma.au0[i].index(bottom) == 0:
                return dogma.au0[i][1]


    elif str(intrvl) == 'mi2':

        for i in range(len(dogma.mi2)):

            if bottom in dogma.mi2[i] and dogma.mi2[i].index(bottom) == 0:
                return dogma.mi2[i][1]


    elif str(intrvl) == 'ma2':

        for i in range(len(dogma.ma2)):

            if bottom in dogma.ma2[i] and dogma.ma2[i].index(bottom) == 0:
                return dogma.ma2[i][1]

    elif str(intrvl) == 'au2':

        for i in range(len(dogma.au2)):

            if bottom in dogma.au2[i] and dogma.au2[i].index(bottom) == 0:
                return dogma.au2[i][1]


def make_mod(root, mod_name):  # returns list of defined music mode

    mod_struct = list(dogma.modes[mod_name])  # got structure of mode from dict by its name and listing it

    res_row = []  # result row of mode notes

    res_row.append(root)  # set root note as 0-element of result list

    next_step = root

    for step in mod_struct:

        if step == '0':

            next_step = interval(next_step, 'au0')

            res_row.append(next_step)

        elif step == '1':

            next_step = interval(next_step, 'mi2')

            res_row.append(next_step)

        elif step == '2':

            next_step = interval(next_step, 'ma2')

            res_row.append(next_step)

        elif step == '3':

            next_step = interval(next_step, 'au2')

            res_row.append(next_step)

    return res_row


print(make_mod(root_note, mode))
