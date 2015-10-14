from braid import Braid

def get_first_handle(some_braid):
    """
    Finds and returns the first handle of the given braid.

    return:
        (p, q) : Where p, q are the start and end points of the handle.
    """

    gens = some_braid.generators
    # print 'p\tq\tk\ttemp_p'
    p, q = 0, 0
    for pos in xrange(len(gens)):
        q = pos
        temp_p = p
        for k in xrange(temp_p, q):
            # print str(p) + '\t' + str(q) + '\t' + str(k) + '\t' + str(temp_p)
            if (gens[k] + gens[q]) == 0:
                return (k, q)
            elif (abs(gens[k]) - abs(gens[q])) == 1 or \
                 (abs(gens[q]) - abs(gens[k])) == 0:
                    p += 1
    return None

def reduce(braid, (p, q)):
    """
    Applies one step of the alphabetical homomorphism on the given handle.

    Returns a new reduced braid.
    """
    new_handle = []
    j = abs(braid.generators[p])
    e = j/braid.generators[p]
    for letter in braid.generators[p:q+1]:
        exp = abs(letter)/letter
        idx = abs(letter)
        if (idx != j) and (idx != (j + 1)):
            new_handle.append(exp*idx)
        elif idx == (j + 1):
            new_handle.append(-1*e*idx)
            new_handle.append(exp*j)
            new_handle.append(e*idx)
    new_generators = braid.generators[:p] + new_handle + \
                        braid.generators[q + 1:]
    return Braid(new_generators, braid.pref_notation)


a = Braid([2, -1, -2, -1, 2, 1], 'alpha')
b = Braid([-1, -2, 1, 3, -2, -3, -2, 1, -3, 2, 1, 1], 'alpha')
brd = b
while True:
    print 'Braid: ', str(brd),
    first_handle = get_first_handle(brd)
    print '\tHandle: ' + str(first_handle)
    print ' '
    if first_handle == None:
        break
    brd = reduce(brd, first_handle)
print 'Reduced!'

# handle = get_first_handle(a)
# print 'a: ' + str(a)
# print 'first_handle: ' + str(handle)
# b = reduce(a, handle)
# print 'reduced: ' + str(b)
