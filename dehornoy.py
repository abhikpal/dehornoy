from braid import Braid

def get_first_handle(some_braid):
    """
    Finds and returns the first handle of the given braid.

    return:
        (p, q) : Where p, q are the start and end points of the handle.
    """

    gens = some_braid.generators
    print 'p\tq\tk\ttemp_p'
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
