"""
Code for describing braids.
"""

class Braid(object):
    """
    Describes a braid word and some basic operations on it.
    """
    
    def __init__(self, generators, pref_notation='default'):
        """
        A 'null string' should be input as [0]

        pref_notation: preferred notation for output as a string
        """
        assert type(generators) == type([]), "Braid should be input as a list"
        assert len(generators) > 0, "No braid generators given"
        self.generators = generators
        self.pref_notation = pref_notation

    def main_generator(self):
        """
        Main Generator: generator with the lowest index in the braid word.
        """
        main_generator = None
        for g in self.generators:
            if main_generator == None or abs(g) < main_generator:
                main_generator = abs(g)
        return main_generator

    def is_reduced(self):
        """
        Checks if the braid word is reduced.

        A braid word is reduced if the main generator occurs ONLY positively
        or negatively.
        """
        if len(self.generators) == 1:
            return True
        else:
            m_gen = self.main_generator()
            if ((-1)*m_gen in self.generators) and (m_gen in self.generators):
                return False
            else:
                return True

    def inverse(self):
        """
        Returns the inverse of the braid.
        """
        return Braid([-1*k for k in  reversed(self.generators)])

    def __mul__(self, other):
        return Braid(self.generators + other.generators)

    def change_notation(self, target):
        """
        Changes from the internal notation to the target notation.
        Possible values for target:
         'alpha', 'artin', 'default'
        The artin representationn can also be used in a latex file.

        The nullstring is 'e' for the Artin representation and '#' for alpha.
        """
        if target == 'artin':
            return ' '.join('s_{' + str(abs(g)) + '}^{' + str(abs(g)/g) + '}'\
                            if g != 0 else 'e' for g in self.generators)
        elif target == 'alpha':
            m = self.main_generator()
            alp = lambda g: chr(ord('Q') + (abs(g) / g) * 16 + abs(g) - 1)
            return ''.join(alp(g) if g != 0 else '#' for g in self.generators)
        else:
            return ':'.join(str(g) for g in self.generators)

    def __str__(self):
        return self.change_notation(self.pref_notation)

    __repr__ = __str__
