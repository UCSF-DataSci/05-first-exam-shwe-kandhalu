#!/bin/bash

# create main project directory
mkdir bioinformatics_project

# go into  project directory
cd bioinformatics_project

# make subdirectories: data, scripts, and results
mkdir data scripts results

# create empty files inside scripts
touch scripts/generate_fasta.py scripts/dna_operations.py scripts/find_cutsites.py

# create empty file inside results
touch results/cutsite_summary.txt

# create empty file inside data
touch data/random_sequence.fasta

# create a README.md file with description of project structure
cat <<EOL > README.md

# Bioinformatics project: This project has main directory called bioinfrmatics_project. There are 3 
# subdirectories, called data, scripts, and results. The data subdirectory has 1 file called 
# random_sequences.fasta. The scripts subdirectory has 3 files called dna_operations.py, find_cutsites.py, 
# and generate_fasta.py. The results subdirectory has one file called cutsite_summary.txt. 

EOL

# print a message indicating setup is complete
echo "Bioinformatics project setup is complete."
