from src.detect_patterns import detect_pattern


from src.detect_patterns import detect_pattern

def test_glossary():
    assert detect_pattern("corpus/glossary.txt") == "D"

def test_faq():
    assert detect_pattern("corpus/faq/programming.txt") == "C"

def test_sorting():
    assert detect_pattern("corpus/howto/sorting.txt") == "A"