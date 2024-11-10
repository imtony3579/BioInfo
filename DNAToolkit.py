# DNA Toolkit file 
import collections


Nucleotides = ['A', 'C', 'G', 'T']


# Checking the sequence to make sure it's a DNA sequence
def validateSeq(dna_seq: str):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(valid_seq: str) -> dict:
    # tmp_freq = {'A':0, 'C': 0, 'G': 0, 'T':0}
    # for nuc in valid_seq:
    #     tmp_freq[nuc]+=1
    # return tmp_freq
    return dict(collections.Counter(valid_seq))