"""

DNA operations file that does the following:

complement(sequence): Returns the complement of a DNA sequence 
(A -> T, C -> G, G -> C, T -> A; e.g., "CCTCAGC" -> "GGAGTCG").

reverse(sequence): Returns the reverse of a sequence (e.g. "CCTCAGC" -> "CGACTCC").

reverse_complement(sequence): Returns the reverse complement of a DNA sequence (e.g. "CCTCAGC" -> "GCTGAGG"); 
i.e. the reverse of the complement (apply complement then reverse, or vice versa).

Command line input: python dna_operations.py GAATTC

"""

import argparse

complements = {
    "A":"T", 
    "T": "A",
    "G":"C",
    "C": "G"
}

def complement(sequence): # returns complement of DNA sequence
    sequence.upper()
    complement_sequence = ""
    sequence.upper()
    for n in sequence:
        complement_sequence += complements[n]
    return complement_sequence

def reverse(sequence): # returns reverse of DNA sequence
    sequence.upper()
    reverse_sequence = sequence[::-1] 
    return reverse_sequence

def reverse_complement(sequence): # returns reverse complement of DNA sequence
    sequence.upper()
    complement_sequence = complement(sequence)
    reverse_of_comp = reverse(complement_sequence)
    return reverse_of_comp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    args = parser.parse_args()

    complement_sequence = complement(args.sequence)
    reverse_sequence = reverse(args.sequence)
    reverse_of_comp = reverse_complement(args.sequence)
    
    print(f"Original sequence: {args.sequence}") 
    print(f"Complement sequence: {complement_sequence}") 
    print(f"Reverse sequence: {reverse_sequence}") 
    print(f"Reverse of complement sequence: {reverse_of_comp}")