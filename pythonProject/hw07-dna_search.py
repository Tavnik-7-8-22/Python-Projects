"""
Filename: hw07-dna_search.py

This file contains a class for searching for a pattern in a DNA sequence.

Name: Samuel Rabinor

Date: 11/29/22
"""


# -------------------------------------------------------------------------------

import logging
logging.basicConfig(level=logging.DEBUG, filename='debug2.log')


class SearchDNA:

    def __init__(self):
        print("Starting program...")
        self.genome = ''

    def read_genome(self, filename):
        """
        Open a file containing genome data and read all its contents.
        :param filename: the path and name of the genome file
        :return: the string containing the DNA data read from the file
        """
        genome = ''
        with open(filename, 'r') as f:
            for line in f:
                # ignore header line with genome information
                if not line[0] == '>':
                    genome += line.rstrip()
        return genome

    def find_pattern(self, pattern, text):
        """
        Creates a loop that increments an index, i, from 0 to the length of the text minus the length of the pattern plus 1 and finds where a pattern repeats.
        :param pattern: the pattern we are looking
        :param text: the text we're searching for the pattern in
        :return: the position at which the pattern was found
        """
        occurance = []  # hold the list of offsets where the pattern matches in the text.
        # search for the pattern in the text
        for i in range(len(text) - len(pattern) + 1):
            match = True
            for j in range(len(pattern)):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                occurance.append(i)
        return occurance

    def find_pattern_mm(self, pattern, text, max_mismatches):
        """
        Creates a loop that increments an index, i, from 0 to the length of the text minus the length of the pattern plus
        1 and finds where a pattern repeats allowing for input mismatches.
        :param pattern: the pattern we are looking for
        :param text: the text we're searching for the pattern in
        :param max_mismatches: the position at which the pattern with up to two mismatches was found
        :return:
        """
        occurance = []  # hold the list of offsets where the pattern matches in the text.
        # search for the program in the text
        for i in range(len(text) - len(pattern) + 1):
            match = True
            max_mismatch = 0
            for j in range(len(pattern)):
                if pattern[j] != text[i + j]:
                    max_mismatch = max_mismatch + 1
                    if max_mismatch > max_mismatches:
                        match = False
                        break
            if match:
                occurance.append(i)
        logging.debug("Find pattern mm returned pattern {}".format(occurance))
        return occurance

    def count_bases(self, genome):
        """
        Calculates the total number of times each base occurs in a genome
        :param genome: the genome
        :return: the amount of times that each letter appeared
        """
        bases = {'C': 0, 'G': 0, 'A': 0, 'T': 0}
        for ch in genome:
            if ch in bases:
                bases[ch] += 1
        print(bases)

    def process(self):
        """
        reads the Lambda virus genome file and saves the genome sequence to a variable.
        :return: nothing
        """
        print('Starting the process method')
        self.genome = self.read_genome('virus_genomes/lambda_virus.txt')


if __name__ == "__main__":
    search_dna = SearchDNA()
    search_dna.process()

    t = 'CAGGTTTGGACTCGAGGCTATTTGGCCTCTGTCGTTTCCTTTCTCTGTGTTTGGCCTTCCTGGAACAATATGGCCACA'
    p = 'TTTGGCCT'
    print(search_dna.find_pattern(p, t))

    p2 = 'AGGT'
    p3 = 'ACTAAGT'
    print(len(search_dna.find_pattern(p2, search_dna.genome)))
    print(search_dna.find_pattern(p3, search_dna.genome)[:1])

    t = 'CAGGTTTGGACTCGAGGCTATTTGGCCTCTGTCGTTTCCTTTCTCTGTGTTTGGCCTTCCTGGAACAATATGGCCACA'
    p = 'TTTGGCCT'
    print(search_dna.find_pattern_mm(p, t, 2))

    p4 = 'AGGT'
    p5 = 'ACTAAGT'
    print(len(search_dna.find_pattern_mm(p4, search_dna.genome, 2)))
    print(search_dna.find_pattern_mm(p5, search_dna.genome, 2)[:1])

    print(search_dna.count_bases(search_dna.genome))

    sequence = "CATTGCTGTTATAGAAGGGAGAAGTTGAGTCAATTAAGAAGCAGATGAACAGGCAAAATATCAGCATATCCACCCTGGAAGGACAACTCTCAAGCAT"
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/hepatitis_b_virus.txt'), 3))
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/lambda_virus.txt'), 3))
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/measles_virus.txt'), 3))
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/mumps_virus.txt'), 3))
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/nipah_virus.txt'), 3))
    print(search_dna.find_pattern_mm(sequence, search_dna.read_genome('virus_genomes/rubella_virus.txt'), 3))
