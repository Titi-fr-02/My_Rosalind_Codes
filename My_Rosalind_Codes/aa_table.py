# aa_table library
# aa_table.py

CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y',
    'UAA': '',  'UAG': '',  'UGA': '',  # Stop codons
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S',
    'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

REVERSE_CODON_TABLE = {
    'A': 4,  # Alanine
    'R': 6,  # Arginine
    'N': 2,  # Asparagine
    'D': 2,  # Aspartic Acid
    'C': 2,  # Cysteine
    'Q': 2,  # Glutamine
    'E': 2,  # Glutamic Acid
    'G': 4,  # Glycine
    'H': 2,  # Histidine
    'I': 3,  # Isoleucine
    'L': 6,  # Leucine
    'K': 2,  # Lysine
    'M': 1,  # Methionine / Start codon
    'F': 2,  # Phenylalanine
    'P': 4,  # Proline
    'S': 6,  # Serine
    'T': 4,  # Threonine
    'W': 1,  # Tryptophan
    'Y': 2,  # Tyrosine
    'V': 4,  # Valine
    'Stop': 3  # Stop codons
}

aa_weight = {
    'A' : 71.03711,
    'C' : 103.00919,
    'D' : 115.02694,
    'E' : 129.04259,
    'F' : 147.06841,
    'G' : 57.02146,
    'H' : 137.05891,
    'I' : 113.08406,
    'K' : 128.09496,
    'L' : 113.08406,
    'M' : 131.04049,
    'N' : 114.04293,
    'P' : 97.05276,
    'Q' : 128.05858,
    'R' : 156.10111,
    'S' : 87.03203,
    'T' : 101.04768,
    'V' : 99.06841,
    'W' : 186.07931,
    'Y' : 163.06333
}