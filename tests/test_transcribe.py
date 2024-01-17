# write tests for transcribe functions
import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe('ACTG') == 'UGAC', "Transcription failed"
    assert transcribe('ACTG', reverse=True) == reverse_transcribe('ACTG'), "Reverse transcription failed"

    with pytest.raises(ValueError, match="Invalid sequence.* base 1"):
        transcribe('XCTG')

    with pytest.raises(ValueError, match="Invalid sequence.* base 2"):
        transcribe('AXTG')

    with pytest.raises(ValueError, match="Invalid sequence.* base 3"):
        transcribe('ACXG')
    
    with pytest.raises(ValueError, match="Invalid sequence.* base 4"):
        transcribe('ACTX')


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe('ACTG') == 'CAGU', "Reverse transcription failed"

    with pytest.raises(ValueError, match="Invalid sequence.* base 1"):
        reverse_transcribe('XCTG')

    with pytest.raises(ValueError, match="Invalid sequence.* base 2"):
        reverse_transcribe('AXTG')

    with pytest.raises(ValueError, match="Invalid sequence.* base 3"):
        reverse_transcribe('ACXG')
    
    with pytest.raises(ValueError, match="Invalid sequence.* base 4"):
        reverse_transcribe('ACTX')