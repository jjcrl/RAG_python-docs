from lib.chunks import * 

def test_glossary():
    filepath = "corpus/glossary.txt"
    chunks = chunk_glossary(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["heading"] == '">>>"'

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
    assert chunks[0]["heading"] == "abs(number, /)"

def test_C():
    filepath = 'corpus/faq/programming.txt'
    chunks = chunk_C(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["heading"] == "Is there a source code-level debugger with breakpoints and single-stepping?"

def test_E():
    filepath = 'corpus/tutorial/appetite.txt'
    chunks = chunk_E(filepath)
    assert isinstance(chunks,list)
    assert len(chunks) == 1
    assert "appetite" in chunks[0]["text"].lower()


def test_chunk_file():
    filepath = 'corpus/glossary.txt'
    chunks = chunk_file(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]['pattern'] == 'D'