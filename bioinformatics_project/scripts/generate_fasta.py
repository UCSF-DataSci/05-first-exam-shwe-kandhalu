"""

Generate FASTA file of random DNA sequence of 1 million base pairs (ATCG)

Command line input: python generate_fasta.py

"""

import random
import textwrap

# function to generate random dna sequence and save as fasta file with 80 bases per line
def generate_random_dna_seq(length = 1000000):
    base = ['A', 'T', 'C', 'G'] # base options
    sequence = "".join(random.choices(base, k = length)) # keep picking random bases till defined length of 1000000
    
    with open('/workspaces/05-first-exam-shwe-kandhalu/bioinformatics_project/data/random_sequence.fasta', 'w') as file:
        for bases in range(0, len(sequence), 80): # makes sure there are 80 bases per line
            line = sequence[base:base+80]
            file.write(line + '\n')

    print(f"Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")

if __name__ == "__main__":
    generate_random_dna_seq()