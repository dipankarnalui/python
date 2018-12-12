with open('out.txt', 'w') as f:
    print >> f, 'Filename:', filename  # Python 2.x
    print('Filename:', filename, file=f)  # Python 3.x