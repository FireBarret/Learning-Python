def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 >dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    tot = 0
    for nuc in dna:
        if nucleotide in nuc:
            tot = tot + 1
        else:
            tot = tot
    return tot

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool
    Return True if and only if the DNA sequence is valid. (contains only ATCG)

    >>> is_valid_sequence('ABC')
    False
    >>> is_valid_sequence('TATA')
    True
    """
    valid_char = "ATCG"
    result = True
    for nuc in dna:
        if nuc not in valid_char:
            result = False
    return result

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    The first two parameters are DNA sequences and the third parameter is an index.
    Returns the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence
    at the given index.

    >>>insert_sequence('TTTAG','CGCG', 0)
    CGCGTTTAG
    >>>insert_sequence('CCGG','AT', 2)
    CCATGG
    """
    newdna = dna1[:index] + dna2 + dna1[index:]
    return newdna    
def get_complement(nucleotide):
    """ (str) -> str
    Returns the nucleotide's complement.
    >>>get_complement('A')
    T
    >>>get_complement('G')
    C
    """
    result = ''
    if nucleotide == 'A':
        result = 'T'
    if nucleotide == 'T':
        result = 'A'
    if nucleotide == 'C':
        result = 'G'
    if nucleotide == 'G':
        result = 'C'
    return result
def get_complementary_sequence(dna):
    """ (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence
    >>>get_complementary_sequence('TATA')
    'ATAT'
    >>>get_complementary_sequence('ATCG')
    'TAGC'
    """
    result_sequence = ''
    for nucleotide in dna:
        result = ''
        if nucleotide == 'A':
            result = 'T'
        if nucleotide == 'T':
            result = 'A'
        if nucleotide == 'C':
            result = 'G'
        if nucleotide == 'G':
            result = 'C'
        result_sequence = result_sequence + result
    return result_sequence
