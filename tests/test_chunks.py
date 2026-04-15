from lib.chunks import * 

def test_glossary():
    filepath = "corpus/glossary.txt"
    chunks = chunk_glossary(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["term"] == '">>>"'

def test_A():
    filepath = 'corpus/howto/sorting.txt'
    chunks = chunk_A(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]['heading'] == "Sorting Basics"
    assert len(chunks) == 10

def test_B():
    filepath = 'corpus/library/functions.txt'
    chunks = chunk_B(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["signature"] == "abs(number, /)"


def test_C():
    filepath = 'corpus/faq/programming.txt'
    chunks = chunk_C(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["sub-heading"] == "Is there a source code-level debugger with breakpoints and single-stepping?"