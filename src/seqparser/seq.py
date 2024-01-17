# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # initialize rna transcript as empty string

    rna = ""
    pos = 0
    for base in seq.strip().upper():
        if base in ALLOWED_NUC: # check if input sequence is valid
            rna += TRANSCRIPTION_MAPPING[base] # transcribe base and concatenate with rna
            pos += 1
        else:
            raise ValueError(f"Invalid sequence: {base} @ base {pos + 1}")
        
    if not reverse:
        return rna
    else:
        return rna[::-1]

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True) # transcribe and reverse
     