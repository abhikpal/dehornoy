# Dehornoy's Braid Reduction Algorithm

This repository is a collection of python scripts that implement Patrick Dehornoy's braid reduction algorithm introduced in his [*A Fast Method for Comparing Braids*](http://www.math.unicaen.fr/~dehornoy/Papers/Dfo.pdf) paper.

The internal data type uses a special representation of the braid word. This is unlike the representation proposed by E. Artin and is very different from the alphabetical representation often used for ease of writing.

For example, the following braid word:

```
s_1 s_2^{-1} s_1^{-1} s_2 s_3 s_1 (aBAaca)
```

will be represented using the following list:

```
[(1), (-2), (-1), (2), (3), (1)]
```

In general, ```s_a^{+/- 1}``` will be encoded as an integer of the form ```(+/- 1) * a```

Utilities that help generate LaTeX source from the internal representation have also been included. Some of this can also be used with the ```braids``` ```tikz``` library for LaTeX.

All of the code in this repository was written as a part of my Extended Essay on braid comparison Algorithms required for the completion of the two year [International Baccalaureate](http://www.ibo.org/) Diploma Program at [UWC India](http://uwcmahindracollege.org/). The code here is released under the [Apache License](http://www.apache.org/licenses/LICENSE-2.0) (see ```LICENSE``` for details.)
