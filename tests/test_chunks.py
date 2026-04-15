from lib.chunks import * 

def test_glossary():
    filepath = "corpus/glossary.txt"
    chunks = chunk_glossary(filepath)
    assert isinstance(chunks,list)
    assert chunks[0]["term"] == '">>>"'