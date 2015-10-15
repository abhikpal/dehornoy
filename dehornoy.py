from braid import Braid

def get_first_handle(braid):
    """
    Finds and returns the first handle of the given braid.

    return:
        (p, q) : Where p, q are the start and end points of the handle.
    """
    def is_handle(braid, (p, q)):
        """
        Checks if (p, q) is a valid handle in the given braid.

        return:
            True/False
        """
        if braid.generators[p] + braid.generators[q] == 0:
            v = braid.generators[(p+1):q]
            j = abs(braid.generators[p])
            for k in v:
                if not (abs(k) < (j - 1) or abs(k) > j):
                    return False
            else:
                return True
            # if (j-1) in v or -1*(j-1) in v:
            #     return False
            # elif (j in v) or (-1*j in v):
            #     return False
            # else:
            #     return True
        else:
            return False
    p, q = 0, 0
    for q in xrange(len(braid.generators)):
        for k in xrange(q, (p-1), -1):
            if is_handle(braid, (k, q)):
                return (k, q)
    else:
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

def fully_reduce(braid, print_output=True):
    """
    Ffully reduces the given braid.
    """
    chain = []
    reduced_brd = braid
    while True:
        handle = get_first_handle(reduced_brd)
        chain.append((reduced_brd, handle))
        if handle == None:
            if print_output:
                print str(reduced_brd)
            break
        p, q = handle
        if print_output:
            if reduced_brd.pref_notation == 'alpha':
                print str(reduced_brd)[:p] + '[' + \
                      str(reduced_brd)[p:q+1] + ']' \
                    + str(reduced_brd)[q+1:]
            else:
                print str(reduced_brd)
        reduced_brd = reduce(reduced_brd, handle)
    return (reduced_brd, chain)

def compare(b1, b2, print_output=True):
    """
    Compares two braids b1 and b2. Returns true if equal.
    """
    if print_output:
        print 'b1: ', str(b1)
        print 'b2: ', str(b2)
        print 'b1*inv(b2): ', str(b1*b2.inverse())
        print 'Reducing b1 * inv(b2)...'
        print 
    reduced, chain = fully_reduce(b1*b2.inverse(), print_output)
    if reduced.generators == []:
        if print_output:
            print 'b1 == b2 :)'
            return True
    else:
        if print_output:
            print 'b1 != b2'
        return False

a = Braid([2, 2, -1, -2, 3,  2, -1, -2, -3, 2, 3, 2, 2, -1, -2, -3], 'artin')
b = Braid([-1, -2, 1, 3, -2, -3, -2, 1, -3, 2, 1, 1], 'artin')
compare(a, b, True)
