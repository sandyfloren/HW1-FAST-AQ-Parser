# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    good_file = 'data/test.fa'
    bad_file = 'tests/bad.fa'
    blank_file = 'tests/blank.fa'

    parser_good = FastaParser(good_file)
    parser_bad = FastaParser(bad_file)
    parser_blank = FastaParser(blank_file)

    # Normal behavior
    well_formed = True
    records = 0
    seq0 = ""

    for rec in parser_good:
        if records == 0:
            header0 = rec[0] # get first header
            seq0 = rec[1] # get first sequence record 
        if rec[0] is None or rec[1] is None or rec[0].startswith('>'): # header and sequence should not be empty and '>' should have been removed
            well_formed = False
        records += 1

    assert well_formed, "Fasta parser error: header or sequence was not read correctly"
    assert records == 100, "Fasta parser error: did not read correct number of sequences" # There should be 100 sequences in test.fa
    assert header0 == 'seq0', "Fasta parser error: first header is not correct"
    assert seq0 == 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA', "Fasta parser error: first sequence is not correct"


    # Edge cases
    # Fasta with only headers should have no records
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
        [rec for rec in parser_bad]

    # Fasta with blank lines should raise ValueError on first line
    with pytest.raises(ValueError, match=r"File (.*) had 0 lines."):
       [rec for rec in parser_blank]
    




def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fasta = 'data/test.fa'
    parser = FastaParser(fasta)
    lines = [rec for rec in parser]

    assert lines[0][0] is not None, "Fasta format error: first line is empty"



def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fastq = 'data/test.fq'
    parser = FastqParser(fastq)
    records = 0
    well_formed = True 

    for rec in parser:
        if records == 0:
            header0 = rec[0] # get first header
            seq0 = rec[1] # get first sequence record 
            qual0 = rec[2] # get first read quality
        if rec[0] is None or rec[1] is None or rec[2] is None or rec[0].startswith('>'): # header and sequence should not be empty and '>' should have been removed
            well_formed = False
        records += 1

    assert well_formed, "Fastq parser error: header or sequence was not read correctly"
    assert records == 100, "Fastq parser error: did not read correct number of sequences" # There should be 100 sequences in test.fa
    assert header0 == 'seq0', "Fastq parser error: first header is not correct"
    assert seq0 == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG', "Fastq parser error: first sequence is not correct"
    assert qual0 == """*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7"94(>7='(!5"2/!%"4#32=""", "Fastq parser error: first read quality is not correct"



def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq = 'data/test.fq'
    parser = FastqParser(fastq)
    lines = [rec for rec in parser]

    assert lines[0][0] is not None, "Fastq format error: first line is empty"
