"""

Find cutsites in FASTA data

Finds pairs of restriction enzyme cut sites that are 80-120 kbp apart in a given FASTA file

- Accepts a FASTA file path and a cutsite sequence
- Reads FASTA and saves sequence to variable without whitespace
- Find all occurences of the cutsite
- Find all pairs of cutsite locations that are 80-120 kbp apart
- Print total number of cutsite pairs found and positions of the first 5 pairs
- Save summary of results

Command line input: python find_distant_cutsites.py data/random_sequence.fasta "G|GATCC"

"""

import argparse
import re
import os

# reads FASTA file and returns DNA sequence as a string with no whitespace
def read_fasta_file(file_path):
    with open(file_path,"r") as file:
        sequence = "".join(line.strip() for line in file)
    return sequence 

# find the cutsites in the sequence
def find_cut_sites(sequence, cutsite):
    # remove | from the cutsite
    cutsite = cutsite.replace('|', '')
    cutsite_positions = [m.start() for m in re.finditer(cutsite, sequence)]
    return cutsite_positions

# finds pairs of cutsites that are 80-120 kbp apart
def find_distant_cutsite_pairs(cutsite_positions):
    pairs = []
    for i in range(len(cutsite_positions)):
        for j in range(i+1, len(cutsite_positions)):
            distance = abs(cutsite_positions[j] - cutsite_positions[i])
            if 80000 <= distance <= 120000:
                pairs.append((cutsite_positions[i], cutsite_positions[j]))
    return pairs

# saves summary of cutsite pairs
def summary(pairs, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(f"Total cut site pairs: {len(pairs)}\n")
        file.write(f"First 5 pairs:\n")
        for i, pair in enumerate(pairs[:5]):
            file.write(f"{i+1}. {pair[0]} - {pair[1]}\n")

# main
parser = argparse.ArgumentParser()
parser.add_argument("fasta_file", help = "Path to input FASTA file")
parser.add_argument("cutsite", help = "Restriction enzyme cutsite, G|GATCC")
args = parser.parse_args()

# read DNA sequence from FASTA file
sequence = read_fasta_file(args.fasta_file)

# find all cutsites in the sequence
cutsite_positions = find_cut_sites(sequence, args.cutsite)

# find pairs of cutsites
cutsite_pairs = find_distant_cutsite_pairs(cutsite_positions)

print(f"Analyzing cut site: {args.cutsite.replace('|', '')}")
print(f"Total cut sites found: {len(cutsite_positions)}")
print(f"Cut site pairs 80-120 kbp apart: {len(cutsite_pairs)}")
print("First 5 pairs:")
for i, pair in enumerate(cutsite_pairs[:5]):
    print(f"{i+1}. {pair[0]} - {pair[1]}")

output_path = 'results/distant_cutsite_summary.txt'
summary(cutsite_pairs, output_path)
print(f"Results saved to {output_path}")