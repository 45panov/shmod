au0 = (('Abb', 'Ab'), ('Ab', 'A'), ('A', 'A#'), ('A#', 'Ax'),  # augmented primas
       ('Bbb', 'Bb'), ('Bb', 'B'), ('B', 'B#'), ('B#', 'Bx'),
       ('Cbb', 'Cb'), ('Cb', 'C'), ('C', 'C#'), ('C#', 'Cx'),
       ('Dbb', 'Db'), ('Db', 'D'), ('D', 'D#'), ('D#', 'Dx'),
       ('Ebb', 'Eb'), ('Eb', 'E'), ('E', 'E#'), ('E#', 'Ex'),
       ('Fbb', 'Fb'), ('Fb', 'F'), ('F', 'F#'), ('F#', 'Fx'),
       ('Gbb', 'Gb'), ('Gb', 'G'), ('G', 'G#'), ('G#', 'Gx'),
       )

mi2 = (('Abb', 'Bbbb'), ('Ab', 'Bbb'), ('A', 'Bb'), ('A#', 'B'), ('Ax', 'B#'),  # minor seconds
       ('Bbb', 'Cbb'), ('Bb', 'Cb'), ('B', 'C'), ('B#', 'C#'), ('Bx', 'Cx'),
       ('Cbb', 'Dbbb'), ('Cb', 'Dbb'), ('C', 'Db'), ('C#', 'D'), ('Cx', 'D#'),
       ('Dbb', 'Ebbb'), ('Db', 'Ebb'), ('D', 'Eb'), ('D#', 'E'), ('Dx', 'E#'),
       ('Ebb', 'Fbb'), ('Eb', 'Fb'), ('E', 'F'), ('E#', 'F#'), ('Ex', 'Fx'),
       ('Fbb', 'Gbbb'), ('Fb', 'Gbb'), ('F', 'Gb'), ('F#', 'G'), ('Fx', 'G#'),
       ('Gbb', 'Abbb'), ('Gb', 'Abb'), ('G', 'Ab'), ('G#', 'A'), ('Gx', 'A#')
       )

ma2 = (('Abb', 'Bbb'), ('Ab', 'Bb'), ('A', 'B'), ('A#', 'B#'), ('Ax', 'Bx'),  # major seconds
       ('Bbb', 'Cb'), ('Bb', 'C'), ('B', 'C#'), ('B#', 'Cx'), ('Bx', 'Cx#'),
       ('Cbb', 'Dbb'), ('Cb', 'Db'), ('C', 'D'), ('C#', 'D#'), ('Cx', 'Dx'),
       ('Dbb', 'Ebb'), ('Db', 'Eb'), ('D', 'E'), ('D#', 'E#'), ('Dx', 'Ex'),
       ('Ebb', 'Fb'), ('Eb', 'F'), ('E', 'F#'), ('E#', 'Fx'), ('Ex', 'Fx#'),
       ('Fbb', 'Gbb'), ('Fb', 'Gb'), ('F', 'G'), ('F#', 'G#'), ('Fx', 'Gx'),
       ('Gbb', 'Abb'), ('Gb', 'Ab'), ('G', 'A'), ('G#', 'A#'), ('Gx', 'Ax')
       )

au2 = (('Abb', 'Bb'), ('Ab', 'B'), ('A', 'B#'), ('A#', 'Bx'), ('Ax', 'Bx#'),  # augmented seconds
       ('Bbb', 'C'), ('Bb', 'C#'), ('B', 'Cx'), ('B#', 'Cx#'), ('Bx', 'Cxx'),
       ('Cbb', 'Db'), ('Cb', 'D'), ('C', 'D#'), ('C#', 'Dx'), ('Cx', 'Dx#'),
       ('Dbb', 'Eb'), ('Db', 'E'), ('D', 'E#'), ('D#', 'Ex'), ('Dx', 'Ex#'),
       ('Ebb', 'F'), ('Eb', 'F#'), ('E', 'Fx'), ('E#', 'Fx#'), ('Ex', 'Fxx'),
       ('Fbb', 'Gb'), ('Fb', 'G'), ('F', 'G#'), ('F#', 'Gx'), ('Fx', 'Gx#'),
       ('Gbb', 'Ab'), ('Gb', 'A'), ('G', 'A#'), ('G#', 'Ax'), ('Gx', 'Ax#')
       )



modes = {'ionian': '221222',  # natural major modes below
         'dorian': '212221',
         'phrygian': '122212',
         'lydian': '222122',
         'mixolydian': '221221',
         'aeolian': '212212',
         'locrian': '122122',
         'melodic minor': '212222',  # melodic minor modes below
         'dorian b2': '122221',
         'lydian augmented': '222212',
         'lydian dominant': '222121',
         'aeolian dominant': '221212',  # aka hindu
         'hindu': '221212',  # aka aeolian dominant
         'half diminished': '212122',  # aka locrian #2
         'locrian #2': '212122',  # aka half diminished
         'super locrian': '121222',  # aka diminished wholetone aka altered dominant
         'diminished wholetone': '121222',  # aka super locrian aka altered dominant
         'altered dominant': '121222',  # aka diminished wholetone aka super locrian
         'harmonic minor': '212213', # harmonic minor modes below
         'locrian #6': '122131',
         'ionian #5': '221312',
         'dorian #4': '213121',
         'phrygian #3': '131212',
         'lydian #2': '312122',
         'mixolydian #1': '121221',
         'wholetone': '222222',  # bonus ;)
         'cromatic': '01011010101',
         }
