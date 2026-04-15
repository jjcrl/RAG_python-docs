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